import numpy as np

import pandas as pd
from scipy.optimize import curve_fit


def fit(filepath, params0):
    '''
    A curve fitting procedure to determine the discharge
    rate constant, the n factor for the discharge rate,
    and the specific capacity. We use the model outlined
    by *R. Tian & S. Park et. al.*
    https://www.nature.com/articles/s41467-019-09792-9
    Input Arguments
    filepath : string, to filepath (csv format)
               first column is xdata, second, ydata
    params0 : 1 by 3 numpy array, with elemets, tau (the
    characteristic lifetime), n (the rate discharge coef-
    ficient), and Q the specific capacity
    Output Argument
    Return the optimized parameters tau, n, Qcapacity
    '''
    # import data
    dframe = pd.read_csv(filepath)
    Rdischarge = dframe.iloc[:, 0].to_numpy()
    normQdata = dframe.iloc[:, 1].to_numpy()

    # Fit procedure
    popt, pcov = curve_fit(fitfunc, Rdischarge, normQdata, p0=params0)
    return popt

# define fit function


def fitfunc(Rdischarge, tau, n, Qcapacity):
    '''
    Capacity versus rate discharge model outlined by
    https://www.nature.com/articles/s41467-019-09792-9
    '''
    normQ = Qcapacity * (1 -
                         (Rdischarge * tau)**n *
                         (1 - np.exp(- (Rdischarge * tau)**(- n)))
                         )
    return normQ
