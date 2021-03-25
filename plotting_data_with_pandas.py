"""
Contains functions for reading in data and plotting data.
"""

from typing import List, Tuple
import pandas as pd

from pandas import DataFrame


def get_name(filename: str) -> str:
    """Returns a descriptive name of the file, removes the suffix describing the file format
    and replaces all instances of '_' with ' '
    >>> get_name('Mean_Global_Temperatures_in_Farenheit.csv')
    temperature data
    >>> get_name('Mean_Cumulative_Mass_Balance_of_Glaciers.csv')
    glaciers csv
    """
    period_index = filename.index('.')
    new_filename = filename[0:period_index]

    return new_filename.replace('_', ' ')


def check_file_format(filename: str) -> pd.DataFrame:
    """Check whether the file with filename is a csv doc or excel doc

    Preconditions
        - '.csv' or '.xlsx' in filename
    """
    if '.csv' in filename:
        return read_csv_file(filename)  # checking whether the files are in csv format or excel

    return read_excel_file(filename)


def read_excel_file(filename: str) -> pd.DataFrame:
    """Return the DataFrame created by reading in an Excel
    file with pandas.
    """
    df_excel = pd.read_excel(filename)
    return df_excel


def read_csv_file(filename: str) -> pd.DataFrame:
    """Return the DataFrame created by reading in a csv file
    with pandas.
    """
    df_csv = pd.read_csv(filename)
    return df_csv


def co2_processing_data(df: pd.DataFrame) -> List:
    """Process co2 data by taking averages for each year.
    This function is only called for CO2 data processing.
    """
    averages = []
    for i in range(len(df)):
        row = [df.loc[i][x] for x in range(1, len(df.loc[i]))]
        average = sum(row) / len(row)
        averages.append(average)

    averages.reverse()

    return averages


def sea_level_data_processing(data_df: pd.DataFrame) -> List[float]:
    """Convert the data from a dataframe object to a list, and return
    the list.
    """
    annual_values = []
    for i in range(len(data_df)):
        annual_values.append(data_df.loc[i][4])

    return annual_values


def filenames_to_lists(ind_filename: str, dep_filename: str) -> Tuple[List, List]:
    """Convert the files in the filenames to lists, and return these lists.

    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    df_independent = check_file_format(ind_filename)  # check file format of both variables
    df_dependent = check_file_format(dep_filename)

    if 'CO2' in ind_filename:
        # process CO2 data by computing averages
        independent_list = co2_processing_data(df_independent)
    else:
        independent_list = convert_data_to_list(df_independent)

    # process sea level data by taking data in the column at index 4
    dependent_list = sea_level_data_processing(df_dependent)

    return (independent_list, dependent_list)


def convert_data_to_list(data_df: pd.DataFrame) -> List[float]:
    """Convert the data from a dataframe object to a list, and
    return the list.
    """
    annual_values = []
    for i in range(len(data_df)):
        annual_values.append(data_df.loc[i][1])

    return annual_values


def create_data_frame(ind_filename: str, dep_filename: str) -> DataFrame:
    """Return a dataframe containing the data needed to graph a dependent variable
    against and an independent variable using pandas.
    """
    independent_name = get_name(ind_filename)  # titles for the axes are descriptions of the variables

    df_independent = check_file_format(ind_filename)  # check which format each file is in and read it
    df_dependent = check_file_format(dep_filename)

    if 'CO2' in ind_filename:
        independent_list = co2_processing_data(df_independent)  # process CO2 data by computing averages
    else:
        independent_list = convert_data_to_list(df_independent)

    dependent_list = sea_level_data_processing(df_dependent)

    new_df = pd.DataFrame({independent_name: independent_list, 'Global Mean Sea Levels': dependent_list})

    return new_df
