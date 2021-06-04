# Imports libraries for math operations, pandas dataframes, and data processing
import pandas as pd
import numpy as np

# Imports libraries for plotting
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Imports a library for the user interface
from ipywidgets import interact, interactive, Layout, Dropdown, IntSlider, Checkbox, fixed

# Imports library for saving plots
import os

# Sets plotting theme to seaborn
sns.set()

# Loading and merging dataframes
def load_data(file, sheet):
    """
    Takes as input an Excel file name and sheet name and loads datasets of geometry and architecture parameters into 
    dataframes and merges them. Returns the merged dataframe.
    
    Parameters:
    file: Excel file name
    sheet: sheet name within `file`
    
    Returns:
    merged_df: a dataframe containing geometry and architecture parameters
    """
    # Creates a dataframe of geometry parameters
    geo_df = pd.read_excel(io=file, sheet_name=sheet)
    geo_df.drop(columns=['DOI', 'Cathode 3D \nCharateristic Note', 'Anode 3D \nCharateristic Note', 'SA/V [1/µm]', 'SA gain'], 
                inplace=True)
    cols = list(geo_df.columns)
    new_cols = ['Paper', 'Set', 'Full Cell Thickness [µm]', 'Cathode Thickness [µm]', 'Anode Thickness [µm]', 
               'Separator Thickness [µm]', 'Cathode Length [µm]', 'Anode Length [µm]']
    rename_cols = dict(zip(cols, new_cols))
    geo_df.rename(columns=rename_cols, inplace=True)
    
    # Creates a dataframe of architecture parameters
    arch_df = pd.read_excel('3D_Battery_Parameter_Log.xls', sheet_name='GeneralInformation', nrows=100)
    arch_df.rename(columns={'Paper #': 'Paper'}, inplace=True)
    archs = list(arch_df.columns[[3,5,7]])
    gen_archs = list(arch_df.columns[[4,6,8]])
    remove_cols = list(arch_df.columns[-15:len(arch_df.columns)])
    remove_cols.append('DOI')
    remove_cols += archs
    arch_df.drop(columns=remove_cols, inplace=True)
    rename_cols = dict(zip(gen_archs, archs))
    arch_df.rename(columns=rename_cols, inplace=True)
    arch_df.drop(arch_df[arch_df['Overall Architecture'] == '3D Concentric'].index, inplace = True)
    
    # Merges the two dataframes
    merged_df = pd.merge(geo_df, arch_df, on=['Paper', 'Set'])
    for col in merged_df.columns[:8]:
        merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')
        
    return merged_df

# Getting architecture types and architecture strings
def get_archs(merged_df):
    """
    Takes as input a dataframe and returns a list of lists of architectures and a list of 
    strings for each architecture type.
    
    Parameter:
    merged_df: dataframe
    
    Returns:
    archs: a list of lists of architectures
    arch_strings: a list of strings for each architecture type
    """
    # Creates a list of architectures for each type: overall, cathode, and anode
    overall_arch = list(np.unique(list(merged_df['Overall Architecture'])))
    cathode_arch = list(np.unique(list(merged_df['Cathode Architecture'].values)))
    cathode_arch.remove('nan')
    anode_arch = list(np.unique(list(merged_df['Anode Architecture'].values)))
    anode_arch.remove('nan')
    
    # Creates a list of lists of architectures
    archs = [overall_arch, cathode_arch, anode_arch]
    # Creates a list of strings for each architecture type
    arch_strings = ['Overall Architecture', 'Cathode Architecture', 'Anode Architecture']
    
    return archs, arch_strings

# Getting parameters and errors for a given architecture type
def get_params(merged_df, arch_type):
    """
    Takes as input a dataframe and an architecture type and returns a list of values of each parameter and 
    the errors for each architecture type.
    
    Parameters:
    merged_df: dataframe
    arch_type: architecture type
            - Options: 'Overall Architecture', 'Cathode Architecture', 'Anode Architecture'
    
    Returns:
    params: a list of lists of values for each parameter
    errors: a list of lists of errors for each parameter
    """
    archs, arch_strings = get_archs(merged_df)
    param_strings = ['Average Full Cell Thickness', 'Average Cathode Thickness', 'Average Anode Thickness', 
                     'Average Separator Thickness', 'Average Cathode Length', 'Average Anode Length']
    
    i = arch_strings.index(arch_type)
    
    avg_full_cell_thicknesses = []
    full_cell_thickness_errors = []
    
    avg_cathode_thicknesses = []
    cathode_thickness_errors = []
    
    avg_anode_thicknesses = []
    anode_thickness_errors = []
    
    avg_sep_thicknesses = []
    sep_thickness_errors = []
    
    avg_cathode_lengths = []
    cathode_length_errors = []
    
    avg_anode_lengths = []
    anode_length_errors = []
    
    for arch in archs[i]:
        # Full cell thickness
        avg_full_cell_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Full Cell Thickness [µm]'].mean()
        avg_full_cell_thicknesses.append(avg_full_cell_thickness)
        
        min_full_cell_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Full Cell Thickness [µm]'].min()
        max_full_cell_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Full Cell Thickness [µm]'].max()
        full_cell_thickness_errors.append([avg_full_cell_thickness - min_full_cell_thickness, 
                                           max_full_cell_thickness - avg_full_cell_thickness])
        
        # Cathode thickness
        avg_cathode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Thickness [µm]'].mean()
        avg_cathode_thicknesses.append(avg_cathode_thickness)
        
        min_cathode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Thickness [µm]'].min()
        max_cathode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Thickness [µm]'].max()
        cathode_thickness_errors.append([avg_cathode_thickness - min_cathode_thickness, 
                                           max_cathode_thickness - avg_cathode_thickness])
        
        # Anode thickness
        avg_anode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Anode Thickness [µm]'].mean()
        avg_anode_thicknesses.append(avg_anode_thickness)
        
        min_anode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Anode Thickness [µm]'].min()
        max_anode_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Anode Thickness [µm]'].max()
        anode_thickness_errors.append([avg_anode_thickness - min_anode_thickness, 
                                           max_anode_thickness - avg_anode_thickness])
        
        # Separator thickness
        avg_sep_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Separator Thickness [µm]'].mean()
        avg_sep_thicknesses.append(avg_sep_thickness)
        
        min_sep_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Separator Thickness [µm]'].min()
        max_sep_thickness = merged_df[merged_df[arch_strings[i]] == arch]['Separator Thickness [µm]'].max()
        sep_thickness_errors.append([avg_sep_thickness - min_sep_thickness, 
                                           max_sep_thickness - avg_sep_thickness])
        
        # Cathode length
        avg_cathode_length = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Length [µm]'].mean()
        avg_cathode_lengths.append(avg_cathode_length)
        
        min_cathode_length = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Length [µm]'].min()
        max_cathode_length = merged_df[merged_df[arch_strings[i]] == arch]['Cathode Length [µm]'].max()
        cathode_length_errors.append([avg_cathode_length - min_cathode_length, 
                                           max_cathode_length - avg_cathode_length])
        
        # Anode length
        avg_anode_length = merged_df[merged_df[arch_strings[i]] == arch]['Anode Length [µm]'].mean()
        avg_anode_lengths.append(avg_anode_length)
        
        min_anode_length = merged_df[merged_df[arch_strings[i]] == arch]['Anode Length [µm]'].min()
        max_anode_length = merged_df[merged_df[arch_strings[i]] == arch]['Anode Length [µm]'].max()
        anode_length_errors.append([avg_anode_length - min_anode_length, 
                                           max_anode_length - avg_anode_length])
        
    full_cell_thickness_errors = np.transpose(full_cell_thickness_errors)
    cathode_thickness_errors = np.transpose(cathode_thickness_errors)
    anode_thickness_errors = np.transpose(anode_thickness_errors)
    sep_thickness_errors = np.transpose(sep_thickness_errors)
    cathode_length_errors = np.transpose(cathode_length_errors)
    anode_length_errors = np.transpose(anode_length_errors)
    
    params = [avg_full_cell_thicknesses, avg_cathode_thicknesses, avg_anode_thicknesses, avg_sep_thicknesses, 
              avg_cathode_lengths, avg_anode_lengths]
    
    errors = [full_cell_thickness_errors, cathode_thickness_errors, anode_thickness_errors, sep_thickness_errors, 
              cathode_length_errors, anode_length_errors]
    
    return params, errors

# Plotting average parameters
def plot_geo_params(merged_df, arch_type, param, save_plot):
    """
    Takes as input an architecture type and parameter and produces plots of the input parameter vs. 
    all other parameters.
    
    Parameters:
    merged_df: dataframe
    arch_type: architecture type
            - Options: 'Overall Architecture', 'Cathode Architecture', 'Anode Architecture'
    param: parameter to be plotted on the y-axis vs. all other parameters
            - Options: 'Average Full Cell Thickness', 'Average Cathode Thickness', 'Average Anode Thickness', 
                     'Average Separator Thickness', 'Average Cathode Length', 'Average Anode Length'
    save_plot: (boolean) whether or not to save the figure to a PDF file
    
    Returns:
    5 plots
    """
    params, errors = get_params(merged_df, arch_type)
    param_strings = ['Average Full Cell Thickness', 'Average Cathode Thickness', 'Average Anode Thickness', 
                     'Average Separator Thickness', 'Average Cathode Length', 'Average Anode Length']
    archs, arch_strings = get_archs(merged_df)
    
    i = arch_strings.index(arch_type)
    j = param_strings.index(param)
    
    y = params[j]
    del params[j]
    y_string = param_strings[j]
    del param_strings[j]
    y_error = errors[j]
    del errors[j]
    
    matplotlib.rcParams.update({'font.size': 20})
    
    fig, axes = plt.subplots(figsize=(8,30), nrows=len(params), ncols=1)
    fig.suptitle(f'{arch_strings[i]} - {y_string}', fontsize=20)
    
    # Plots data
    for k in range(len(params)):
        axes[k].errorbar(params[k], y, 
                     xerr=errors[k], yerr=y_error, 
                     marker='o', linestyle='', color='red', ecolor='black')
        axes[k].set_title(f'{arch_strings[i]}: {y_string} vs. {param_strings[k]}')
        axes[k].set_xlabel(f'{param_strings[k]} [µm]')
        axes[k].set_ylabel(f'{y_string} [µm]')
        for index, text in enumerate(archs[i]):
            axes[k].annotate(text, (params[k][index], y[index]), fontsize=10)
            
    if save_plot:
        if not os.path.isdir(f'{arch_strings[i]}'):
            os.mkdir(f'{arch_strings[i]}')
        if not os.path.isfile(f'{arch_strings[i]}/{y_string}.pdf'):
            plt.savefig(f'{arch_strings[i]}/{y_string}.pdf')
            
# Interactive plotting of average parameters
def interactive_plot_geo_params(df, save_fig=False):
    """
    Displays plots of geometry parameters.
    
    Parameters:
    df: dataframe
    save_fig: (boolean) whether or not to save the figure to a PDF file
            - Default: False
    """
    arch_strings = ['Overall Architecture', 'Cathode Architecture', 'Anode Architecture']
    param_strings = ['Average Full Cell Thickness', 'Average Cathode Thickness', 'Average Anode Thickness', 
                     'Average Separator Thickness', 'Average Cathode Length', 'Average Anode Length']
    plot = interact(plot_geo_params, 
                    merged_df=fixed(df), 
                    arch_type=Dropdown(options=arch_strings, value='Overall Architecture', description='Architecture type'), 
                    param=Dropdown(options=param_strings, value='Average Full Cell Thickness', description='Parameter'), 
                    save_plot=Checkbox(save_fig, description='Save figure')
            )
    
    display(plot)

# Save plots of average parameters
def save_plots():
    """
    Saves plots of geometry parameters for each architecture type.
    """
    arch_strings = ['Overall Architecture', 'Cathode Architecture', 'Anode Architecture']
    param_strings = ['Average Full Cell Thickness', 'Average Cathode Thickness', 'Average Anode Thickness', 
                     'Average Separator Thickness', 'Average Cathode Length', 'Average Anode Length']
    for arch_type in arch_strings:
        for param in param_strings:
            plot_geo_params(arch_type, param, save_plot=True)
            
            