import numpy as np
from liibattery3d.correlationtest import correlation_hypothesis
from liibattery3d.correlationtest import plot_linear_regression
from liibattery3d.correlationtest import linear_outliers


def test_correlation_hypothesis():
    '''
    This funtion tests with a knwon correlation case
    '''
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    alpha = 0.1
    correlation, p = correlation_hypothesis(x, y, alpha)
    assert np.isclose(correlation, 1), ('Correlation is not right',
                                        'for known case')
    return


def test_plot_linear_regression():
    '''
    This function tests the input parameter length and checks
    with a case with known regression line.
    '''
    # Test with known case where slope is 2 and intercept is 0
    x = np.array([0, 1, 2])
    y = np.array([0, 2, 4])
    # Test that input parameters have the same length
    assert len(x) == len(y), 'Input arrays have different lengths'
    slope, intercept, stderr = plot_linear_regression(x, y, plot=False)
    assert np.isclose(slope, 2), 'slope is not right for known case'
    assert np.isclose(intercept, 0), 'intercept is not right for known case'
    return


def test_linear_outliers():
    '''
    This function tests the input parameter length and checks
    with a case with known regression line.
    '''
    # Test with known case where slope is 2 and intercept is 0
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 2, 4, 6, 20])
    num = 1
    # Assert input parameters have the same length
    assert len(x) == len(y), 'Input arrays have different lengths'
    # Assert input num is an integer
    assert isinstance(num, int), 'Number of outliers must be an integer'
    x_new, y_new = linear_outliers(x, y, num)
    assert set(x_new) == set(x[0:4]), 'outlier is not right for known case'
    assert set(y_new) == set(y[0:4]), 'outlier is not right for known case'
    return
