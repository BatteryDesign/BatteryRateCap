import numpy as np
import pandas as pd
import os
import matplotlib
from matplotlib import pyplot as plt
%matplotlib inline
import sklearn
import openpyxl
import xlwt


def potential_rate(xls_file, sheet_name, paper_num, set_num, c_rate):
    """ 
    This function converts potential vs. capacity data to capacity vs c-rate data
    The Highest x-value (capacity [mAh]) from the charge/discharge graph
    PARAMETERS
    ----------
    1) Excel file (file path) - string
    2) sheetnames - list
    3) Paper # - string
    4) Set # - integer: max number of sets
    5) c_rate - dataframe
    RETURNS
    -------
    Capacity vs c-rate dataframe
    """
    # Determining which set # and the number of set lists from the excel file
    set_list = ['set #' + str(i) for i in range (1, set_num + 1)]
    # Test that the input 'set_num' is an integer
    assert type(set_num) == int, 'set_num must be an integer'
    # Dataframing the interested potential vs capacity excel sheet
    df = pd.read_excel(xls_file, sheet_name, header = [0,1,2]) #
    # Merging multiple spreadsheets
    df_sheets = []
    for i in sheet_name:
        df_sheets.append(df[i])
    df_merged = pd.concat(df_sheets, axis = 1)
    # Selecting maximum capacity values for each dataset and concatnate with corresponding c-rates or current density
    caplist = []
    for i in set_list:
        set_i = (df_merged[paper_num, i])
        set_i_max = set_i["Capacity (mAh/g)"].max(axis=0).array
        caplist.append(c_rate)
        caplist.append(pd.DataFrame({"Capacity (mAh/g)": set_i_max}))
    df_cap_rate = pd.concat(caplist, axis = 1)
    # Test that the output is a dataframe
    assert type(c_rate) == type(df_cap_rate), 'The output must be a dataframe'
    return df_cap_rate


def excel_merge(dataframe, xls_file, sheetname):
    """
    This function adds the converted dataframe to an existing excel file
    PARAMETERS
    ----------
    1) converted dataframe - dataframe
    2) Excel file (file path) - string
    3) sheetname - string
    RETURNS
    -------
    A new sheet in the excel file
    """
    # Exporting the converted dataframe to an excel file
    dataframe.to_excel(xls_file, sheet_name = sheetname, index=False, header=True)
    # Test that the sheet name is a string
    assert type(sheetname) == str, 'sheetname must be a string'
    print('saved succesfully to' + xls_file)
    return