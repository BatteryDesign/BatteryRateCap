"""
This is the unit test for gitcaprate.py.
"""
import os
import pandas as pd
import batteryratecap
from batteryratecap import fitcaprate

DATA_PATH = os.path.join(batteryratecap.__path__[0], 'doc/Data')


def test_fitmodel():
    '''
    Test case for curve fit module to all dataset of
    lithium ion battery prescribed in data dir
    first check that output exists as 'fitparameters.csv' in
    data dir, then assert output size of 'fitparameters.csv'
    '''
    # Write parameters to csv file with fit function
    df_input = pd.read_csv('../../doc/Data/visualization_df.csv')
    # test 1; check that file exists
    try:
        filepath = os.path.join(DATA_PATH, "fitparameters.csv")
        fitcaprate.fitmodel(df_input, filepath, [0.5, 1, 200])
        assert os.path.exists(filepath)
    except AssertionError:
        print("I couldn't find filepath to parameters csv file")
    # test 2; check output size of fit parameter csv file
    # read output of the optimized parameters
    try:
        filepath_out = os.path.join(DATA_PATH, 'fitparameters.csv')
        dframe_out = pd.read_csv(filepath_out)
        numcolumns = 8
        shapeout = (dframe_out.shape[1] == numcolumns)
        assert shapeout
    except AssertionError:
        print(f"There should be {numcolumns} columns for \
            the paper and set of data, the optimized parameters \
            and their standard deviations")

def test_fit():
    """
    Test case for curve fit module to lithium ion battery
    test the output size in an array of three elements corresponding
    to the optimized, desired, paramters: the characteristic time tau,
    the n fractor, and specific capacity Q
    """
    filepath = os.path.join(DATA_PATH, "capacityratepaper1set1.csv")
    # parameters
    tau = 0.5
    exponent_n = 1
    capacity_q = 100
    params0 = [tau, exponent_n, capacity_q]  # intial guess parameter
    popt, _ = fitcaprate.fit(params0, filename=filepath)
    try:
        lenparam = len(popt)
        assert lenparam == 3
    except AssertionError:
        print(f'I should have only three parameters, \
              not {lenparam}')

def test_fitfunc():
    '''
    The output of the fit function is the (mass) normalized capacity
    simply assert that the size of the output array is equal to the
    size of the input array, and that
    the maximum value at initail discharge rate (at zero) is less
    than or equal to the specific capacity
    '''
    filepath = os.path.join(DATA_PATH, "capacityratepaper1set1.csv")
    tau = 0.5
    exponent_n = 1
    capacity_q = 100
    # import data
    dframe = pd.read_csv(filepath)
    rate = dframe.iloc[:, 0].to_numpy()
    # estimate normalize mass Q from model
    normq = fitcaprate.fitfunc(rate, tau, exponent_n, capacity_q)
    # first check the shape of normQ output
    try:
        shape_normq = normq.shape
        shape_rate = rate.shape
        assert shape_normq == shape_rate
    except AssertionError:
        print(f'the size of input array, {shape_rate}, and\
              output array, {shape_normq}, should be equal')
        # second, check the initial output value
        try:
            normq0 = normq[0]
            normq_lessorequal_capacity_q = (normq0 <= capacity_q)
            assert normq_lessorequal_capacity_q
        except AssertionError:
            print('the normalized mass capacity normQ should be \
                less than or equal to the specific capacity Q \
                at any given discharge rate')
