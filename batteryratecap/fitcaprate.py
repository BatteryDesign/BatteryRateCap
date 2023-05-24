"""
This module is used to fit experimental capacitye -rate data to
Tian et al.'s empirical model, plot the fit, and return fitting parameters.
"""
import os
import re
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib
from matplotlib import pyplot as plt
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows


def fitmodel(dframe, output_xlsx, params0):
    '''
    This function fits capacity-rate dataframe and outputs
    the optimized fit parameters and covaraiances in a excel file.
    Inputs
    - dframe: capacity-rate dataframe
    - output_xlsx: string, output xlsx file path and name with extension
    - params0: a list of initial points for searching [tau, n, Qmax]
    The data fitting is done using the fit() function below in this file.
    '''
    # Fit procedure
    # define list of fit parameters and of their standard deviations
    taus = []
    sigma_taus = []
    exponenet_ns = []
    sigma_ns = []
    capacity_qs = []
    sigma_qs = []
    numdataset = range(int(len(dframe.columns) / 2))
    # fit dataset
    for i in numdataset:
        # import xdata and ydata from dataframe
        xdata = dframe.iloc[:, (2 * i)].values[0:]
        ydata = dframe.iloc[:, ((2 * i) + 1)].values[0:]
        # discard null datapoints
        # and define input and output of fit function
        rate = xdata[~pd.isnull(xdata)]
        normq = ydata[~pd.isnull(ydata)]
        # fit dataset with more than four datapoints
        # otherwise, discard
        if len(rate) >= 4:
            popt, pcov = fit(params0, xdata=rate, ydata=normq)
            tau, exponent_n, capacity = popt
            # standard deviation
            sigma_tau, sigma_n, sigma_q = np.sqrt(np.diag(pcov))
        else:
            tau = 0
            exponent_n = 0
            capacity = 0
            sigma_tau, sigma_n, sigma_q = [0, 0, 0]
        # append optimized fit parameters to list
        taus.append(tau)
        exponenet_ns.append(exponent_n)
        capacity_qs.append(capacity)
        # append standard deviation of
        # error margin on fit parameters to list
        sigma_taus.append(sigma_tau)
        sigma_ns.append(sigma_n)
        sigma_qs.append(sigma_q)

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
               exponenet_ns[index],
               capacity_qs[index],
               sigma_taus[index],
               sigma_ns[index],
               sigma_qs[index]
               ]
        row_series = pd.Series(row, index=popt_dframe.columns)
        popt_dframe = popt_dframe.append(row_series, ignore_index=True)

#     # Write dataframe of optimized parameters to csv file
#     outputpath = os.path.join(output_dir, "fitparameters.csv")
#     popt_dframe.to_csv(path_or_buf=outputpath, index=False)    
    # Export dataframe of optimized parameter to excel file
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    for row in dataframe_to_rows(popt_dframe, index=True, header=True):
        worksheet.append(row)
    workbook.save(output_xlsx)


def fit(params0, **kwargs):
    '''
    This function fits capacity-rate data to an empirical model and outputs
    the optimized fit parameters (chracteristic time,
    the exponent *n*, and the maximum capacity) and their covariances.
    Keyword Arguments
    xdata: 1D numpy array, default as 'rate'
    ydata: 1D numpy array, default as normq
    filename: string, filepath
        (excel format) first column is xdata, second, ydata
    Output Argument
    Return the optimized parameters tau, n, Q
    '''
    # import data
    if 'xdata' in kwargs:
        rate = kwargs['xdata']
        normq = kwargs['ydata']
    elif 'filename' in kwargs:
        filepath = kwargs['filename']
        dframe = pd.read_excel(filepath)
        rate = dframe.iloc[:, 0].to_numpy()
        normq = dframe.iloc[:, 1].to_numpy()
    # Fit procedure
    popt, pcov = curve_fit(fitfunc, rate, normq, p0=params0)
    return popt, pcov


def fitfunc(rate, tau, exponent_n, capacity_q):
    '''
    This is the empirical model developed by Tian et al.(2019):
    https://www.nature.com/articles/s41467-019-09792-9
    '''
    normq = capacity_q * (1 -
                          (rate * tau)**exponent_n *
                          (1 - np.exp(- (rate * tau)**(- exponent_n)))
                          )
    return normq


def plotfit(dframe, dframe_out):
    '''
    This function fits and plots capacity-rate data and their fitting
    results as a panel figure.
    '''
    # plot for predicted capacity (with optimized parameters)
    # compared to known (measured) capacity outputs
    matplotlib.rcParams.update({'font.size': 18})
    plt.figure(figsize=(20, 20))
    for i in range(int(len(dframe.columns)/2)):
        # test data
        # even columns for xdata; odd columns for ydata
        # then sort values by the even(th) columns
        data = dframe.iloc[:, [2*i, 2*i+1]].sort_values(by=dframe.columns[2*i])
        xdata = data[dframe.columns[2*i]].to_numpy()
        ydata = data[dframe.columns[2*i+1]].to_numpy()
        # Prediction
        # optimized parameters
        tau = dframe_out.loc[i, "tau"]
        exponent_n = dframe_out.loc[i, "n"]
        capacity_q = dframe_out.loc[i, "Q"]
        # error margins of optimized parameters
        sigma_tau = dframe_out.loc[i, "sigma_tau"]
        sigma_n = dframe_out.loc[i, "sigma_n"]
        sigma_q = dframe_out.loc[i, "sigma_Q"]
        # use fit parameters to predict capacity
        rate = np.linspace(min(xdata), max(xdata), 100)
        # compare predicted capacity to known capacity in ydata
        axis = plt.subplot(5, 4, (i + 1),
                           title='\nSE =' + f'{sigma_tau:.2f}' + ','
                           + f'{sigma_n:.2f}' + ','
                           + f'{sigma_q:.2f}')  # five rows and four columns
        axis.plot(xdata, ydata,
                  color='b', marker='o',
                  markersize=5, linestyle='None',
                  label='data')
        # consider only prediction of dataset with more than four data points
        if not (tau == 0 and exponent_n == 0 and capacity_q == 0):
            # call model function
            axis.plot(rate, fitfunc(rate, tau, exponent_n, capacity_q),
                      color='r',
                      linewidth=2, linestyle='--',
                      label='lsqcurvefit')
            labels = '#' + str(i) + '\ntau = ' + \
                     f'{tau:.2f}' + '\nn = ' + \
                     f'{exponent_n:.2f}' + '\nQ = ' + \
                     f'{capacity_q:.2f}'
            plt.text(0.1, 0.1, labels, transform=axis.transAxes)
        else:
            plt.text(0.1, 0.1,
                     'not enough datapoints', transform=axis.transAxes)
        plt.legend(markerscale=0.5, fontsize='xx-small', loc='upper right')
        axis.set_xlabel('discharge rate')
        axis.set_ylabel('capacity [mAh/g]')  # mass normalized capacity
        plt.tight_layout()
