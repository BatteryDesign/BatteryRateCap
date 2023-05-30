"""
This is the unit test for fitcaprate.py.
"""
import os
import git
import pandas as pd
from batteryratecap.fitcaprate import fitmodel
from batteryratecap.fitcaprate import fit
from batteryratecap.fitcaprate import fitfunc

REPO = git.Repo('.', search_parent_directories=True)
GIT_PATH = REPO.git.rev_parse("--show-toplevel")
IN_PATH = os.path.join(GIT_PATH, 'doc/data')
TEST_DATA_PATH = os.path.join(GIT_PATH, 'doc/data/data_for_tests')


def test_fitmodel():
    '''
    Test case for curve fit module to all dataset of
    lithium ion battery prescribed in data dir
    first checks that input dataframe has the correct number
    of columns, then asserts output dataframe size
    '''
    # Write parameters to csv file with fit function
    df_input = pd.DataFrame({"Rate": [1, 2, 3, 4, 5]})
    out_file = os.path.join(TEST_DATA_PATH, "test_fitparameters.xlsx")
    # Test input dataframe has the correct number of columns
    try:
        fitmodel(df_input, out_file, [0.5, 1, 200])
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs \
        the incorrrect error type when input dataframe has the \
        wrong number of columns"
    # Test output size of fit parameter file
    # read output of the optimized parameters
    df_input = pd.read_excel(os.path.join(IN_PATH,
                                          "input_performancelog.xls"),
                             sheet_name='CapacityRate',
                             header=[0, 1, 2])
    fitmodel(df_input, out_file, [0.5, 1, 200])
    dframe_out = pd.read_excel(out_file)
    assert dframe_out.shape[1] == 8, "There should be \
    8 columns for the paper and set of data, \
    the optimized parameters and their standard deviations"


def test_fit():
    """
    Test case for curve fit module to lithium ion battery
    test the output size in an array of three elements corresponding
    to the optimized, desired, paramters: the characteristic time tau,
    the n fractor, and specific capacity Q
    """
    filepath = os.path.join(TEST_DATA_PATH, "test_kwarg_fit.xlsx")
    # intial guess parameter
    tau = 0.5
    exponent_n = 1
    capacity_q = 100
    params0 = [tau, exponent_n, capacity_q]
    popt, _ = fit(params0, filename=filepath)
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
    filepath = os.path.join(TEST_DATA_PATH, "test_kwarg_fit.xlsx")
    tau = 0.5
    exponent_n = 1
    capacity_q = 100
    # import data
    dframe = pd.read_excel(filepath, header=[0, 1, 2])
    rate = dframe.iloc[:, 0].values
    # estimate normalize mass Q from model
    normq = fitfunc(rate, tau, exponent_n, capacity_q)
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
