import plot_geo as geo
import pandas as pd

file = '3D_Battery_Parameter_Log.xls'
sheet = 'GeometryParameters'
df = geo.load_data(file, sheet)

# The function `test_load_data()` tests the function `geo.load_data()`
def test_load_data():
    """
    Tests if the object returned from geo.load_data() is a Pandas dataframe.
    """
    file = '3D_Battery_Parameter_Log.xls'
    sheet = 'GeometryParameters'
    merged_df = geo.load_data(file, sheet)
    str_type = str(type(merged_df))
    if str_type != "<class 'pandas.core.frame.DataFrame'>":
        raise ValueError(f'The object returned is not a DataFrame.')
        
    print('Test passed')
    return

# The function `test_get_archs()` tests the function `get_archs(merged_df)`
def test_get_archs():
    """
    Tests if the two objected returned from geo.get_archs() are lists of the same length.
    """
    archs, arch_strings = geo.get_archs(df)
    if type(archs) != list:
        raise ValueError(f'The first object returned is not a list.')
    if type(arch_strings) != list:
        raise ValueError(f'The second object returned is not a list.')
    if len(archs) != len(arch_strings):
        raise ValueError(f'The two objects returned have different length.')
        
    print('Test passed')
    return

# The function `test_get_params()` tests the function `get_params(arch_type)`
def test_get_params():
    """
    Tests if the two objected returned from geo.get_params() are lists of the same length.
    Tests the function for arch_type = 'Overall Architecture', 'Cathode Architecture', and 'Anode Architecture'.
    """
    overall_params, overall_errors = geo.get_params(df, 'Overall Architecture')
    if type(overall_params) != list:
        raise ValueError(f'The first object returned is not a list.')
    if type(overall_errors) != list:
        raise ValueError(f'The second object returned is not a list.')
    if len(overall_params) != len(overall_errors):
        raise ValueError(f'The two objects returned have different length.')
        
    cathode_params, cathode_errors = geo.get_params(df, 'Cathode Architecture')
    if type(cathode_params) != list:
        raise ValueError(f'The first object returned is not a list.')
    if type(cathode_errors) != list:
        raise ValueError(f'The second object returned is not a list.')
    if len(cathode_params) != len(cathode_errors):
        raise ValueError(f'The two objects returned have different length.')
        
    anode_params, anode_errors = geo.get_params(df, 'Anode Architecture')
    if type(anode_params) != list:
        raise ValueError(f'The first object returned is not a list.')
    if type(anode_errors) != list:
        raise ValueError(f'The second object returned is not a list.')
    if len(anode_params) != len(anode_errors):
        raise ValueError(f'The two objects returned have different length.')
        
    print('Test passed')
    return

