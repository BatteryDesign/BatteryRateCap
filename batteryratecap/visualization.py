import numpy as np
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

def feature_vs_n_tau_Q(visualization_df, features):
    '''
    This function takes in a pandas dataframe, which contains the columns "n", "tau", and "Q" as extracted from the
    curve fit components as well as any geometric or material features the user wish to investigate. A paneled plot
    will be created to analyze the relationship(s) between a feature and any fitting parameter (n, tau, and Q).
    Input:
     - visualization_df: a dataframe that contains column names specified by *features*
     - features: columns in *visualization_df* to be plotted
    Output:
     - A panel plot with three columns (n, tau, and Q) and x rows, where x is the number of features.
    '''
    # Test that the input dataframe has the requried columns named correctly
    assert 'n' in visualization_df, 'The dataframe is missing the "n" column'
    assert 'tau' in visualization_df, 'The dataframe is missing the "tau" column'
    assert 'Q' in visualization_df, 'The dataframe is missing the "Q" column'
    matplotlib.rcParams.update({'font.size': 24})
    fig = plt.figure(figsize=(36,10*len(features)))
    ax = fig.subplots(nrows=len(features),ncols=3)
    # For analysis with more than 1 features
    if len(features) > 1:
        for i, feature in enumerate(features):
            ## LEFT COLUMN (feature vs. 'n')
            ax[i,0].scatter(visualization_df[feature].values, visualization_df['n'].values, color='blue', s = 500)
            ax[i,0].set_xlabel(feature)
            ax[i,0].set_ylabel('n')
            ## MIDDLE COLUMN (feature vs. 'tau')
            ax[i,1].scatter(visualization_df[feature], visualization_df['tau'], color='red', s = 500)
            ax[i,1].set_xlabel(feature)
            ax[i,1].set_ylabel('tau')
            ax[i,1].semilogy()
            ## RIGHT COLUMN (feature vs. 'Q')      
            ax[i,2].scatter(visualization_df[feature], visualization_df['Q'], color='green', s = 500)
            ax[i,2].set_xlabel(feature)
            ax[i,2].set_ylabel('Q')
    # For analysis with only 1 feature
    elif len(features) == 1:
        for i, feature in enumerate(features):
            ## LEFT COLUMN (feature vs. 'n')
            ax[0].scatter(visualization_df[feature].values, visualization_df['n'].values, color='blue', s = 500)
            ax[0].set_xlabel(feature)
            ax[0].set_ylabel('n')
            ## MIDDLE COLUMN (feature vs. 'tau')
            ax[1].scatter(visualization_df[feature], visualization_df['tau'], color='red', s = 500)
            ax[1].set_xlabel(feature)
            ax[1].set_ylabel('tau')
            ax[1].semilogy()
            ## RIGHT COLUMN (feature vs. 'Q')      
            ax[2].scatter(visualization_df[feature], visualization_df['Q'], color='green', s = 500)
            ax[2].set_xlabel(feature)
            ax[2].set_ylabel('Q')        
    plt.tight_layout()
    return fig