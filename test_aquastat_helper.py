import pandas as pd
import aquastat_helper as base
#import packages from helper functions
import folium
from matplotlib import pyplot as plt
import numpy as np
#from aquastat_helper import time_slice, time_series, variable_slice

def test_time_slice():
    #set up inputs, df, time_period
    input_df = pd.DataFrame({'country':['Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan'],
                            'region': ['World | Asia', 'World | Asia', 'World | Asia', 'World | Asia', 'World | Asia'],
                            'variable': ['total_area', 'total_area', 'total_area', 'total_area', 'total_area'],
                            'variable_full': ['Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)'],
                            'time_period': ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982'],
                            'year_measured': [1962.0, 1967.0, 1972.0, 1977.0, 1982.0],
                            'value': [65286.0, 65286.0, 65286.0, 65286.0, 65286.0]})
    input_time_period = '1963-1967'
    #set up true values for comparison
    country_true = 'Afghanistan'
    value_true = 65286.0
    #testing
    df_test = base.time_slice(input_df, input_time_period)
    country_test = df_test.index[0] #check row
    value_test = df_test.values[0][0] #df_test.values is an array
    #comparison
    assert country_test==country_true
    assert value_test==value_true;

def test_time_series():
    #set up inputs, df, country, variable
    input_df = pd.DataFrame({'country':['Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan'],
                            'region': ['World | Asia', 'World | Asia', 'World | Asia', 'World | Asia', 'World | Asia'],
                            'variable': ['total_area', 'total_area', 'total_area', 'total_area', 'total_area'],
                            'variable_full': ['Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)'],
                            'time_period': ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982'],
                            'year_measured': [1962.0, 1967.0, 1972.0, 1977.0, 1982.0],
                            'value': [65286.0, 65286.0, 65286.0, 65286.0, 65286.0]})
    input_country = 'Afghanistan'
    input_variable = 'total_area'
    #set up true values for comparison
    year_true = [1962, 1967, 1972, 1977, 1982]
    area_true = [65286.0, 65286.0, 65286.0, 65286.0, 65286.0]
    #testing
    df_test = base.time_series(input_df, input_country, input_variable)
    year_test = df_test.index #check row
    area_test = df_test.values #df_test.values is an array
    column_test = df_test.columns[0]
    #comparison column
    assert column_test == input_variable
    #compare years
    assert year_test[0]==year_true[0]
    assert year_test[1]==year_true[1]
    assert year_test[2]==year_true[2]
    assert year_test[3]==year_true[3]
    assert year_test[4]==year_true[4]
    #compare area
    assert area_test[0][0]==area_true[0]
    assert area_test[1][0]==area_true[1]
    assert area_test[2][0]==area_true[2]
    assert area_test[3][0]==area_true[3]
    assert area_test[4][0]==area_true[4];


def test_variable_slice():
    #set up inputs, df, variable
    input_df = pd.DataFrame({'country':['Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan'],
                            'region': ['World | Asia', 'World | Asia', 'World | Asia', 'World | Asia', 'World | Asia'],
                            'variable': ['total_area', 'total_area', 'total_area', 'total_area', 'total_area'],
                            'variable_full': ['Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)', 'Total area of the country (1000 ha)',
                                             'Total area of the country (1000 ha)'],
                            'time_period': ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982'],
                            'year_measured': [1962.0, 1967.0, 1972.0, 1977.0, 1982.0],
                            'value': [65286.0, 65286.0, 65286.0, 65286.0, 65286.0]})
    input_variable = 'total_area'
    #set up true values for comparison
    country_true = 'Afghanistan'
    time_true = ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982']
    value_true = [65286.0, 65286.0, 65286.0, 65286.0, 65286.0]
    #testing
    df_test = base.variable_slice(input_df, input_variable)
    country_test = df_test.index[0]
    time_test = df_test.columns.tolist()
    value_test = df_test.values.tolist()[0]
    #compare
    assert country_test==country_true
    assert time_test==time_true
    assert value_test == value_true;
