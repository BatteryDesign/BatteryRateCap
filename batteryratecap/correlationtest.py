"""
This module can be used to conduct correlations tests between two variables,
plot their linear gression line (if exists), and detects outliers in the
linear relationship.
"""
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats


def correlation_hypothesis(x_array, y_array, alpha, test='pearson'):
    '''
    This function prints out the correlation and p values
    and returns the hypothesis testing results for two
    variables x and y.
    Input:
        x - nx1 array
        y - nx1 array
        alpha - alpha value for correlation testing,
                usually 0.05
        test - type of correlation test, including
               pearson and spearman test.
    Output:
        correlation - correlation value (between -1 and 1)
        p - p value
        print out hypothesis test result
    '''
    # Test that input parameters are the same length
    assert len(x_array) == len(y_array), 'Input arrays have different lengths'
    # Test that alpha is in acceptable range
    assert 0 < alpha <= 0.1, 'Alpha is not in valid range'
    # Set test type
    if test == 'pearson':
        correlation, p_value = scipy.stats.pearsonr(x_array, y_array)
    elif test == 'spearman':
        correlation, p_value = scipy.stats.spearmanr(x_array, y_array)
    else:
        print('Unknown correlation test')
        correlation = np.nan
        p_value = np.nan
    print(test, 'correlation betweeen the input variables is',
          "{:.2f}".format(correlation), 'with p value',
          "{:.2f}".format(p_value))
    if p_value <= alpha:
        print('Reject null hypothesis.The linear correlation',
              'is statistically significant')
    else:
        print('Accept null hypothesis. The linear correlation',
              ' is statistically insignificant')
    return correlation, p_value


def plot_linear_regression(x_array, y_array, plot=True):
    '''
    This function plots the linear regression line of variable x and y.
    Input:
        x - nx1 array
        y - nx1 array
        plot - default True, use False if do not need to plot
    Output:
        slope - the slope of the linear regression line
        intercept - the y axis intercept of the linear regression line
    '''
    slope, intercept, _, _, stderr = scipy.stats.linregress(x_array, y_array)
    line_label = f'Regression line: y={intercept:.2f}+{slope:.2f}x'
    if plot is True:
        plt.figure(figsize=(12, 8))
        plt.scatter(x_array, y_array,
                    marker='o', color='green',
                    label='input data')
        plt.plot(x_array, intercept+slope*x_array, label=line_label)
        plt.legend()
        plt.tight_layout()
    return slope, intercept, stderr


def linear_outliers(x_array, y_array, num):
    '''
    This function plots and highlights the outliers from the
    regression line and return lists of x,y with outliers
    removed.
    Input:
        x - nx1 array
        y - nx1 array
        num - integar, number of outliers
    Output:
        x_no_outliers - (n-num)x1 array
        y_no_outliers - (n-num)x1 array
        plot x, y data and highlights the outliers
    '''
    # Plot original data
    _, _, stderr = plot_linear_regression(x_array, y_array, plot=False)
    print('original std error is', stderr)
    # Starting x and y before outlier removal
    x_no_outliers = x_array
    y_no_outliers = y_array
    # Calculate std error with each datapoint index removed
    for _ in range(num):
        err_list = []
        for index, _ in enumerate(x_no_outliers):
            x_remove = []
            y_remove = []
            x_remove = np.append(x_no_outliers[:int(index)],
                                 x_no_outliers[int(index)+1:])
            y_remove = np.append(y_no_outliers[:int(index)],
                                 y_no_outliers[int(index)+1:])
            _, _, stderr = plot_linear_regression(x_remove,
                                                  y_remove,
                                                  plot=False)
            err_list.append(abs(stderr))
        # Sort error index from min to max and
        # get the index that returns the min stderr
        max_index = np.argsort(err_list)[0]
        print('Detect outlier at position', 'x=',
              x_no_outliers[max_index], 'y=', y_no_outliers[max_index])
        # Remove outlier
        x_no_outliers = np.append(x_no_outliers[:int(max_index)],
                                  x_no_outliers[int(max_index+1):])
        y_no_outliers = np.append(y_no_outliers[:int(max_index)],
                                  y_no_outliers[int(max_index+1):])
    # Find outlier arrays
    x_outliers = list(x_array)
    y_outliers = list(y_array)
    # Remove elements in x_outliers that match elements in x_no_outliers
    # At the end, only the outliers are left in x_outliers
    for element in list(x_outliers):
        if element in list(x_no_outliers):
            x_outliers.remove(element)
            list(x_no_outliers).remove(element)
    for element in list(y_outliers):
        if element in list(y_no_outliers):
            y_outliers.remove(element)
            list(y_no_outliers).remove(element)
    # Plot regression line without outliers
    _, _, stderr = plot_linear_regression(x_no_outliers,
                                          y_no_outliers)
    print('new std error is', stderr)
    plt.scatter(x_outliers, y_outliers, marker='o',
                color='r', label='outliers')
    plt.legend()
    return x_no_outliers, y_no_outliers
