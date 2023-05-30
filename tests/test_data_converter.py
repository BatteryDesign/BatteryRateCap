"""
Unit test for data_converter
"""
import os
import git
import pandas as pd
import numpy as np
from batteryratecap.data_converter import potential_rate_paper_set
from batteryratecap.data_converter import potential_rate_all
from batteryratecap.data_converter import excel_merge
from batteryratecap.data_converter import capacity_cycle

REPO = git.Repo('.', search_parent_directories=True)
GIT_PATH = REPO.git.rev_parse("--show-toplevel")
DATA_PATH = os.path.join(GIT_PATH, 'doc/data')
IN_PATH = os.path.join(DATA_PATH, 'input_performancelog.xls')
OUT_PATH = os.path.join(DATA_PATH, 'data_for_tests/\
test_export_potential_rate.xlsx')
WRONGH_IN_PATH = os.path.join(DATA_PATH, 'data_for_tests/\
wrong_header_performancelog.xls')
WRONGS_IN_PATH = os.path.join(DATA_PATH, 'data_for_tests/\
wrong_sheetname_performancelog.xls')


def test_potential_rate_paper_set():
    '''
    This functions tests that the input excel file has the required format,
    with sheet names containing with "C_".
    '''
    # Test paper number type
    try:
        potential_rate_paper_set(IN_PATH, ['2C_discharge'],
                                 OUT_PATH, 32, 2)
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input paper number is not a string."
    # Test paper number string content format
    try:
        potential_rate_paper_set(IN_PATH, ['2C_discharge'],
                                 OUT_PATH, 'Hung et al.', 2)
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input paper number is in wrong format."
    # Test input sheetname type
    try:
        potential_rate_paper_set(IN_PATH, '2C_discharge',
                                 OUT_PATH, 'Paper # 32', 2)
    except Exception as err:
        assert isinstance(err, TypeError), "Function outputs the wrong error \
        type when input sheetnames are not in a list."


def test_potential_rate_all():
    '''
    This function tests that the input dicharge data is stored in the requried
    format, with sheet name starting with "C_".
    '''
    try:
        potential_rate_all(WRONGH_IN_PATH, OUT_PATH)
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input file has wrong headers."
    try:
        potential_rate_all(WRONGS_IN_PATH, OUT_PATH)
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input file has wrong sheetnames."


def test_excel_merge():
    '''
    This function tests that the input excel file name has to correct
    extension in xls or xlsx.
    '''
    df = pd.DataFrame()
    try:
        excel_merge(df, '000', 'sheet1')
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when output file extension is wrong."
    try:
        excel_merge(df, '000.xls', 1)
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when output sheet name is not string."


def test_capacity_cycle():
    '''
    This function tests that the input capacity-cycle data is a nx2 array and
    that the list of current density is the same length as the number of
    stairs/rates.
    '''
    try:
        capacity_cycle(np.array([[1, 2, 3],
                                 [2, 3, 4],
                                 [6, 6, 6]]),
                       2, ['1', '2'], 'mA/cm^2', 'mAh')
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input array is the wrong shape."
    try:
        capacity_cycle(np.array([[1, 2],
                                 [2, 3],
                                 [6, 6]]),
                       2, ['1'], 'mA/cm^2', 'mAh')
    except Exception as err:
        assert isinstance(err, AssertionError), "Function outputs the wrong \
        error type when input array is the wrong shape."
