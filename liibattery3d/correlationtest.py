import numpy as np
from matplotlib import pyplot as plt
import scipy


def correlation_test(x, y, alpha, test='pearson'):
    '''
    This function prints out the correlation and p values
    and returns the hypothesis testing results for two
    variables x and y.
    Input:
        x -
        y -
        alpha -
        test -
    Output:
    '''
    if test == 'pearson':
        correlation, p = scipy.stats.pearsonr(x, y)
    elif test == 'spearman':
        correlation, p = scipy.stats.spearmanr(x, y)
    else:
        print('Unknown correlation test')
    print(test, 'correlation betweeen the input variables is',
          "{:.2f}".format(correlation), 'with p value',
          "{:.2f}".format(p))
    if p <= alpha:
        print('Reject null hypothesis.The linear correlation',
              'is statistically significant')
    else:
        print('Accept null hypothesis. The linear correlation',
              ' is statistically insignificant')
    return


def plot_linear_regression(x, y):
    '''
    This function plots the linear regression line of variable x and y.
    '''
    slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
    line_label = f'Regression line: y={intercept:.2f}+{slope:.2f}x'
    plt.plot(x, y, linewidth=0, marker='o', color='green', label='input data')
    plt.plot(x, intercept+slope*x, label=line_label)
    plt.legend()
    return slope, intercept


def linear_outliers(x, y, num):
    '''
    This function plots and highlights the outliers from the
    regression line and return lists of x,y with outliers
    removed.
    Input:
    Output:
    '''
    slope, intercept = plot_linear_regression(x, y)
    y_line = intercept + slope * x
    err = []
    for y_i, y_line_i in zip(y, y_line):
        err.append(abs(y_line_i - y_i))
    indexes = []
    for outlier_num in range(num):
        max_index = err.index(np.max(err))
        indexes.append(max_index)
        plt.plot(x[max_index], y[max_index], marker='o',
                 color='r', label='outliers')
        print('Detect outlier at position', 'x=',
              x[max_index], 'y=', y[max_index])
        err.remove(np.max(err))
    # Create new x,y lists that don't have the outliers
    x_no_outliers = x
    y_no_outliers = y
    for item, index in enumerate(indexes):
        x_no_outliers[item] = np.nan
        y_no_outliers[item] = np.nan
    x_no_outliers = [x_i for x_i in x_no_outliers if np.isnan(x_i) is False]
    y_no_outliers = [y_i for y_i in y_no_outliers if np.isnan(y_i) is False]
    return x_no_outliers, y_no_outliers


def data_outlier(x, y, num):
    '''
    This function identifies and plots the potential outliers of the dataset.
    '''
    return
