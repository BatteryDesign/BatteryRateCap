import numpy as np
from matplotlib import pyplot as plt
import scipy.stats


def correlation_hypothesis(x, y, alpha, test='pearson'):
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
    assert len(x) == len(y), 'Input arrays have different lengths'
    # Test that alpha is in acceptable range
    assert 0 < alpha <= 0.1, 'Alpha is not in valid range'
    # Set test type
    if test == 'pearson':
        correlation, p = scipy.stats.pearsonr(x, y)
    elif test == 'spearman':
        correlation, p = scipy.stats.spearmanr(x, y)
    else:
        print('Unknown correlation test')
        correlation = np.nan
        p = np.nan
    print(test, 'correlation betweeen the input variables is',
          "{:.2f}".format(correlation), 'with p value',
          "{:.2f}".format(p))
    if p <= alpha:
        print('Reject null hypothesis.The linear correlation',
              'is statistically significant')
    else:
        print('Accept null hypothesis. The linear correlation',
              ' is statistically insignificant')
    return correlation, p


def plot_linear_regression(x, y, plot=True):
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
    slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
    line_label = f'Regression line: y={intercept:.2f}+{slope:.2f}x'
    if plot is True:
        plt.scatter(x, y, marker='o', color='green', label='input data')
        plt.plot(x, intercept+slope*x, label=line_label)
        plt.legend()
    return slope, intercept, stderr


def linear_outliers(x, y, num):
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
    slope, intercept, stderr = plot_linear_regression(x, y, plot=False)
    print('original std errer is', stderr)
    # Starting x and y before outlier removal
    x_no_outliers = x
    y_no_outliers = y
    # Calculate std error without each outlier removed
    for item in range(num):
        err_list = []
        for x_i, index in enumerate(x_no_outliers):
            x_remove = np.append(x_no_outliers[:int(index)],
                                 x_no_outliers[int(index+1):])
            y_remove = np.append(x_no_outliers[:int(index)],
                                 x_no_outliers[int(index+1):])
            slope, intercept, stderr = plot_linear_regression(x_remove,
                                                              y_remove,
                                                              plot=False)
            err_list.append(abs(stderr))
        # Sort error index from min to max
        sorted_index = np.argsort(err_list)
        max_index = sorted_index[-1]  # outlier index
        print('Detect outlier at position', 'x=',
              x_no_outliers[max_index], 'y=', y_no_outliers[max_index])
        # Remove outlier
        x_no_outliers = np.append(x_no_outliers[:int(max_index)],
                                  x_no_outliers[int(max_index+1):])
        y_no_outliers = np.append(y_no_outliers[:int(max_index)],
                                  y_no_outliers[int(max_index+1):])
    # Find outlier arrays
    x_outliers = list(x)
    y_outliers = list(y)
    x_no_outliers_list = list(x_no_outliers)
    y_no_outliers_list = list(y_no_outliers)
    for element in list(x_outliers):
        if element in x_no_outliers_list:
            x_outliers.remove(element)
            x_no_outliers_list.remove(element)
    for element in list(y_outliers):
        if element in y_no_outliers_list:
            y_outliers.remove(element)
            y_no_outliers_list.remove(element)
    # Plot regression line without outliers
    slope, intercept, stderr = plot_linear_regression(x_no_outliers,
                                                      y_no_outliers)
    print('new std error is', stderr)
    plt.scatter(x_outliers, y_outliers, marker='o',
                color='r', label='outliers')
    plt.legend()
    return x_no_outliers, y_no_outliers
