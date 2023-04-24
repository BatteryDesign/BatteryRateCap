import numpy as np
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt


def feature_vs_n_tau_Q(visualization_df, features):
    '''
    This function takes in a pandas dataframe, which contains the columns
    (in order from left to right) named "Paper #" and "Set" 
    followed by the "n", "tau", and "Q" and "DOI" features and as well as the
    n, tau, and Q parameters, to quickly investigate and relationship(s) between a feature and parameter
    '''
    matplotlib.rcParams.update({'font.size': 24})
    fig = plt.figure(figsize=(36,24))
    ax = fig.subplots(nrows=len(features),ncols=3)
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
    plt.tight_layout()