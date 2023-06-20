"""
This is the unit test for visualization.py
"""
import numpy as np
import pandas as pd
from batteryratecap.visualization import feature_vs_n_tau_q


def test_feature_vs_n_tau_q():
    '''
    This function tests the raised error type when
    the column names for fitting parameters are wrong.
    This function also uses a test case to ensure the
    function returns the correct figure grid number.
    '''
    df1 = pd.DataFrame({'n': [1, 2, 3],
                        'tau': [0.1, 0.2, 0.3],
                        'Qmax': [100, 200, 300],
                        'cathode_thickness': [20, 30, 40]})
    df2 = pd.DataFrame({'n': [1, 2, 3],
                        'cathode_thickness': [20, 30, 40]})
    # Test that the function output the correct
    # error type whem missing columns 'n', 'tau', and 'Q'
    try:
        feature_vs_n_tau_q(df2, ['cathode_thickness'])
    except Exception as err:
        assert isinstance(err, AssertionError), "feature_vs_n_tau_Q() \
                           Function outputs the wrong error type \
                           when the dataframe has wrong column names."
    # Test that the function outputs the correct number of panels
    fig = feature_vs_n_tau_q(df1, ['cathode_thickness'])
    specs = fig.axes[0].get_subplotspec()
    row, col = specs.get_topmost_subplotspec().get_gridspec().get_geometry()
    assert np.isclose(row, 1) & np.isclose(col, 3), 'Unexpected \
    figure grid size'
