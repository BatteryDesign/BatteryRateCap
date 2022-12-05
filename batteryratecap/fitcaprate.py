import numpy as np
import os
import re
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib 
from matplotlib import pyplot as plt


def fitmodel(dframe, output_dir, params0):
    '''
    This function fits capacity-rate dataframe and outputs
    the optimized fit parameters and covaraiances in a csv file.
    Inputs
    - capacity-rate dataframe
    - output directory for the csv file that contains fitting parameters 
    - params0: a list of initial points for searching [tau, n, Qmax]
    The data fitting is done using the fit() function below in this file.
    '''
    # Fit procedure
    # define list of fit parameters and of their standard deviations
    taus = []
    sigma_taus = []
    ns = []
    sigma_ns = []
    specificQs = []
    sigma_Qs = []
    numdataset = range(int(len(dframe.columns) / 2))
    # fit dataset
    for i in numdataset:
        # import xdata and ydata from dataframe
        xdata = dframe.iloc[:, (2 * i)].values[0:]
        ydata = dframe.iloc[:, ((2 * i) + 1)].values[0:]
        # discard null datapoints
        # and define input and output of fit function
        Rdischarge = xdata[~pd.isnull(xdata)]
        normQ = ydata[~pd.isnull(ydata)]
        # fit dataset with more than four datapoints
        # otherwise, discard
        if len(Rdischarge) >= 4:
            popt, pcov = fit(params0, xdata=Rdischarge, ydata=normQ)
            tau, n, specificQ = popt
            # standard deviation
            sigma_tau, sigma_n, sigma_Q = np.sqrt(np.diag(pcov))
        else:
            tau = 0
            n = 0
            specificQ = 0
            sigma_tau, sigma_n, sigma_Q = [0, 0, 0]
        # append optimized fit parameters to list
        taus.append(tau)
        ns.append(n)
        specificQs.append(specificQ)
        # append standard deviation of
        # error margin on fit parameters to list
        sigma_taus.append(sigma_tau)
        sigma_ns.append(sigma_n)
        sigma_Qs.append(sigma_Q)

    # Structure the optimized parameters into a dataframe
    # Define all column names of dataset from original dataframe
    colnames = list(dframe.columns)[1::2]
    # Turn the tuples if column names into lists
    for index, element in enumerate(colnames):
        colnames[index] = list(element[:-1])
        for subindex, string in enumerate(colnames[index]):
            # conserve numbers only
            colnames[index][subindex] = int(re.findall(r'\d+', string)[0])
        colnames[index] = tuple(colnames[index])
    # insert optimized parameters into dataframe
    popt_dframe = pd.DataFrame(columns=['Paper #', 'Set',
                                        'tau', 'n', 'Q',
                                        'sigma_tau', 'sigma_n', 'sigma_Q'])
    # Input paper, set numbers, optimized parameters and
    # their error margins into dataframe
    for index, element in enumerate(colnames):
        row = [int(element[0]),
               int(element[1]),
               taus[index],
               ns[index],
               specificQs[index],
               sigma_taus[index],
               sigma_ns[index],
               sigma_Qs[index]
               ]
        row_series = pd.Series(row, index=popt_dframe.columns)
        popt_dframe = popt_dframe.append(row_series, ignore_index=True)

    # Write dataframe of optimized parameters to csv file
    outputpath = os.path.join(output_dir, "fitparameters.csv")
    popt_dframe.to_csv(path_or_buf=outputpath, index=False)
    return

def fit(params0, **kwargs):
    '''
    This function fits capacity-rate data to an empirical model and outputs
    the optimized fit parameters (chracteristic time, 
    the exponent *n*, and the maximum capacity) and their covariances.
    Keyword Arguments
    xdata: 1D numpy array, default as 'Rdischarge'
    ydata: 1D numpy array, default as normQ
    filename: string, filepath
        (csv format) first column is xdata, second, ydata
    Output Argument
    Return the optimized parameters tau, n, specificQ
    '''
    # import data
    if 'xdata' in kwargs:
        Rdischarge = kwargs['xdata']
        normQ = kwargs['ydata']
    elif 'filename' in kwargs:
        filepath = kwargs['filename']
        dframe = pd.read_csv(filepath)
        Rdischarge = dframe.iloc[:, 0].to_numpy()
        normQ = dframe.iloc[:, 1].to_numpy()
    # Fit procedure
    popt, pcov = curve_fit(fitfunc, Rdischarge, normQ, p0=params0)
    return popt, pcov

def fitfunc(Rdischarge, tau, n, specificQ):
    '''
    This is the empirical model developed by Tian et al.(2019):
    https://www.nature.com/articles/s41467-019-09792-9
    '''
    normQ = specificQ * (1 -
                         (Rdischarge * tau)**n *
                         (1 - np.exp(- (Rdischarge * tau)**(- n)))
                         )
    return normQ

def plotfit(dframe, dframe_out):
    '''
    This function fits and plots capacity-rate data and their fitting results as a panel figure.
    '''
    # plot for predicted capacity (with optimized parameters) compared to known (measured) capacity outputs
    matplotlib.rcParams.update({'font.size': 18})
    fig2 = plt.figure(figsize=(20, 20))
    for i in range(int(len(dframe.columns)/2)):
        # test data
        # even columns for xdata; odd columns for ydata
        # then sort values by the even(th) columns
        indeven = (2 * i)
        indodd = indeven + 1
        data = dframe.iloc[:, [indeven, indodd]].sort_values(by=dframe.columns[indeven])
        xdata = data[dframe.columns[indeven]].to_numpy()
        ydata = data[dframe.columns[indodd]].to_numpy()
        #Prediction
        # optimized parameters
        tau = dframe_out.loc[i, "tau"]
        n = dframe_out.loc[i, "n"]
        specificQ = dframe_out.loc[i, "Q"]
        # error margins of optimized parameters
        sigma_tau = dframe_out.loc[i, "sigma_tau"]
        sigma_n = dframe_out.loc[i, "sigma_n"]
        sigma_Q = dframe_out.loc[i, "sigma_Q"]
        # use fit parameters to predict capacity
        Rdischarge = np.linspace(min(xdata), max(xdata), 100)
        normQopt = fitfunc(Rdischarge, tau, n, specificQ)  # call model function
        # compare predicted capacity to known capacity in ydata
        ax = plt.subplot(5, 4, (i + 1),
                         title= '\nSE =' + f'{sigma_tau:.2f}'+ ','
                         + f'{sigma_n:.2f}'+ ','
                         + f'{sigma_Q:.2f}')  # five rows and four columns
        ax.plot(xdata, ydata,
                color='b', marker='o',
                markersize=5, linestyle='None',
                label='data')
        # consider only prediction of dataset with more than four data points
        if not (tau==0 and n==0 and specificQ==0):
            ax.plot(Rdischarge, normQopt, 
                    color='r',
                    linewidth=2, linestyle='--',
                    label='lsqcurvefit')
            labels = '#'+str(i)+'\ntau = ' + \
                f'{tau:.2f}' +'\nn = ' + \
                f'{n:.2f}' + '\nQ = ' + \
                f'{specificQ:.2f}'
            plt.text(0.1, 0.1, labels, transform=ax.transAxes)
        else:
            plt.text(0.1, 0.1, 'not enough datapoints', transform=ax.transAxes)
        plt.legend(markerscale=0.5, fontsize='xx-small', loc='upper right')
        ax.set_xlabel('discharge rate')
        ax.set_ylabel('capacity [mAh/g]') # mass normalized capacity
        plt.tight_layout()
    return