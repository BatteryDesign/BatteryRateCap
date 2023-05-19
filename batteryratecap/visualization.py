"""
This module is used to create panel plots that visualize the relationship
between fitting parameters n, tau, and Q, and any battery design features
(geometric or material).
"""
import matplotlib
from matplotlib import pyplot as plt


def feature_vs_n_tau_q(visualization_df, features):
    '''
    This function takes in a pandas dataframe, which contains the columns "n",
    "tau", and "Q" as extracted from the curve fit components as well as any
    geometric or material features the user wish to investigate. A paneled plot
    will be created to analyze the relationship(s) between a feature and any
    fitting parameter (n, tau, and Q).
    Input:
     - visualization_df: a dataframe that contains column names specified by
                         *features*
     - features: columns in *visualization_df* to be plotted
    Output:
     - A panel plot with three columns (n, tau, and Q) and x rows, where x
       is the number of features.
    '''
    # Test that the input dataframe has the requried columns named correctly
    assert 'n' in visualization_df, 'The dataframe is missing the "n" column'
    assert 'tau' in visualization_df, 'The dataframe is missing \
    the "tau" column'
    assert 'Q' in visualization_df, 'The dataframe is missing the "Q" column'
    matplotlib.rcParams.update({'font.size': 24})
    fig = plt.figure(figsize=(36, 10*len(features)))
    axis = fig.subplots(nrows=len(features), ncols=3)
    # For analysis with more than 1 features
    if len(features) > 1:
        for i, feature in enumerate(features):
            # LEFT COLUMN (feature vs. 'n')
            axis[i, 0].scatter(visualization_df[feature].values,
                               visualization_df['n'].values,
                               color='blue', s=500)
            axis[i, 0].set_xlabel(feature)
            axis[i, 0].set_ylabel('n')
            # MIDDLE COLUMN (feature vs. 'tau')
            axis[i, 1].scatter(visualization_df[feature],
                               visualization_df['tau'],
                               color='red', s=500)
            axis[i, 1].set_xlabel(feature)
            axis[i, 1].set_ylabel('tau')
            axis[i, 1].semilogy()
            # RIGHT COLUMN (feature vs. 'Q')
            axis[i, 2].scatter(visualization_df[feature],
                               visualization_df['Q'],
                               color='green', s=500)
            axis[i, 2].set_xlabel(feature)
            axis[i, 2].set_ylabel('Q')
    # For analysis with only 1 feature
    elif len(features) == 1:
        for i, feature in enumerate(features):
            # LEFT COLUMN (feature vs. 'n')
            axis[0].scatter(visualization_df[feature].values,
                            visualization_df['n'].values,
                            color='blue', s=500)
            axis[0].set_xlabel(feature)
            axis[0].set_ylabel('n')
            # MIDDLE COLUMN (feature vs. 'tau')
            axis[1].scatter(visualization_df[feature],
                            visualization_df['tau'],
                            color='red', s=500)
            axis[1].set_xlabel(feature)
            axis[1].set_ylabel('tau')
            axis[1].semilogy()
            # RIGHT COLUMN (feature vs. 'Q')
            axis[2].scatter(visualization_df[feature],
                            visualization_df['Q'],
                            color='green', s=500)
            axis[2].set_xlabel(feature)
            axis[2].set_ylabel('Q')
    plt.tight_layout()
    return fig
