#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_filtered_df(df, regex_search=None, **kwargs):
    """
    Filter a DataFrame based on specified conditions for each column.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be filtered.
    - regex_search (tuple): A tuple containing the column name and regex pattern
                           for filtering based on regular expression (default: None).
    - **kwargs: Keyword arguments where each key is a column name and the
                corresponding value is a list of values to filter for that column.

    Returns:
    - pd.DataFrame: A filtered DataFrame based on the specified conditions.
    """
    filtered_df = df.copy()  # Copy the DataFrame to avoid modifying the original

    # Apply filters for each column and its specified values
    for column, values in kwargs.items():
        values = [values] if not isinstance(
            values, list) else values  # ensure list
        filtered_df = filtered_df[filtered_df[column].isin(values)]

    # Apply regex search if provided
    if regex_search:
        column = regex_search[0]
        regex_pattern = regex_search[1]
        # Create a boolean mask based on the regex search
        mask = filtered_df[column].str.contains(
            regex_pattern, regex=True).fillna(False)
        filtered_df = filtered_df[mask]

    return filtered_df
