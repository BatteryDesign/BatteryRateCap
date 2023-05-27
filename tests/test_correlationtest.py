"""
This is the unit test for correlationtest.py
"""
import numpy as np
from batteryratecap.correlationtest import correlation_hypothesis
from batteryratecap.correlationtest import plot_linear_regression
from batteryratecap.correlationtest import linear_outliers


def test_correlation_hypothesis():
    '''
    This funtion tests with a knwon correlation case
    '''
    x_values = np.array([1, 2, 3])
    y_values = np.array([2, 4, 6])
    alpha = 0.1
    correlation, _ = correlation_hypothesis(x_values, y_values, alpha)
    assert np.isclose(correlation, 1), ('Correlation is not right',
                                        'for known case')


def test_plot_linear_regression():
    '''
    This function tests the input parameter length and checks
    with a case with known regression line.
    '''
    # Test with known case where slope is 2 and intercept is 0
    x_values = np.array([0, 1, 2])
    y_values = np.array([0, 2, 4])
    # Test that input parameters have the same length
    assert len(x_values) == len(y_values), 'Input arrays have \
    different lengths'
    slope, intercept, _ = plot_linear_regression(x_values, y_values,
                                                 plot=False)
    assert np.isclose(slope, 2), 'slope is not right for known case'
    assert np.isclose(intercept, 0), 'intercept is not right for known case'


def test_linear_outliers():
    '''
    This function tests the input parameter length and checks
    with a case with known regression line.
    '''
    # Test with known case where slope is 2 and intercept is 0
    x_values = np.array([0, 1, 2, 3, 4])
    y_values = np.array([0, 2, 4, 6, 20])
    num = 1
    # Assert input parameters have the same length
    assert len(x_values) == len(y_values), 'Input arrays have \
    different lengths'
    # Assert input num is an integer
    assert isinstance(num, int), 'Number of outliers must be an integer'
    x_new, y_new = linear_outliers(x_values, y_values, num)
    assert set(x_new) == set(x_values[0:4]), 'outlier is not right for \
    known case'
    assert set(y_new) == set(y_values[0:4]), 'outlier is not right for \
    known case'
