#!/usr/bin/ python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from datetime import datetime

import pandas as pd


def get_days(start_date_str, end_date_str):
    """
    Calculate the difference in days between two dates.

    Parameters:
    - start_date_str (str): The start date in string format (e.g., '2022-01-01').
    - end_date_str (str): The end date in string format (e.g., '2022-12-31').

    Returns:
    int: The difference in days between the two dates.
    """
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # If still in production, set today's date
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # Calculate the difference between the two dates
    date_difference = end_date - start_date

    # Extract the number of days from the difference
    number_of_days = date_difference.days

    return number_of_days


def airtime_duration(row):
    """
    Calculate the duration in days between two given dates.

    Parameters:
    - row (pandas.Series): DataFrame row containing 'first_air_date' and 'last_air_date'.

    Returns:
        int: The number of days between the two dates, or -1 if an error occurs during the calculation.
    """
    # Extract dates from dataframe row
    date_str1 = str(row['first_air_date'])
    date_str2 = str(row['last_air_date'])

    try:
        # Calculate the duration using the get_days function
        res = get_days(date_str1, date_str2)
        return -1 if res < 0 else res

    except ValueError:
        # Handle exception (if any) and return -1
        return -1


def get_ordered_dict(df):
    """
    Creates an ordered dictionary with movie names as keys and a formatted string
    containing homepage and poster path as values. If homepage or poster path is
    not available, it sets the value to "NOT AVAILABLE".

    Parameters:
    df (DataFrame): A pandas DataFrame containing movie data with 'name', 'homepage',
                    and 'poster_path' columns.

    Returns:
    OrderedDict: An ordered dictionary with movie names as keys and formatted strings
                 as values.
    """
    ordered_dic = OrderedDict()
    for _, row in df.iterrows():
        # Concatenate homepage and poster_path, or set to "NOT AVAILABLE" if either is missing
        ordered_dic[row['name']] = f"{row['homepage']}/{row['poster_path']}" if pd.notna(
            row['homepage']) and pd.notna(row['poster_path']) else "NOT AVAILABLE"
    return ordered_dic
