#!/usr/bin/ python
# -*- coding: utf-8 -*-

import csv
import os
import tarfile
import time
import zipfile

from pandas import read_csv


def unzip(file_path):
    """
    Unzips files in zip or tar.gz format.

    Parameters:
    - file_path (str): The path to the file that needs to be uncompressed.

    Returns:
    - List[str] or None: If the file is successfully uncompressed, returns a list of paths
        to the extracted .csv files. Returns None if the file format is not supported.

    """
    dir = os.path.dirname(file_path)

    # Unzip if it's a zip file
    if file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dir)
            return [os.path.join(dir, f)
                    for f in os.listdir(dir) if f.endswith('.csv')]
    # Unzip if it's a tar.gz file
    elif file_path.endswith('.tar.gz'):
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(dir)
            return [os.path.join(dir, f)
                    for f in os.listdir(dir) if f.endswith('.csv')]
    # Print error if the file format is not supported
    else:
        print(f'Error: {file_path} is not a zip or tar.gz file.')
        return None


def get_execution_time(func, *args):
    """
    Measure the execution time of a given function with specified arguments.

    Parameters:
    - func (function): The function to be executed and timed.
    - *args: Variable number of arguments to pass to the function.

    Returns:
    tuple: 
        - The result of the function.
        - The execution time in seconds.
    """
    # Record the start time
    start_time = time.time()

    # Execute the function with specified arguments
    result = func(*args)

    # Record the end time
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    # Return the result and execution time as a tuple
    return result, execution_time


def merge_csv_with_pandas(csv_files, on='id'):
    """
    Read CSV files and merge them into a DataFrame using the Pandas library.

    Parameters:
    - csv_files (list): List of paths to the CSV files to be merged.

    Returns:
    - pd.DataFrame: The resulting DataFrame.
    """
    # Read CSV files and create a list of DataFrames
    df_list = [read_csv(file) for file in csv_files]

    # Drop duplicates (done before new dataset)
    for df in df_list:
        df.drop_duplicates(subset=on, keep='first', inplace=True)

    # Initialize the DataFrame with the first CSV file
    df = df_list[0]

    # Merge subsequent DataFrames on the 'id' column
    for df_ in df_list[1:]:
        df = df.merge(df_, on=on)

    return df


def merge_csv_with_csv_module(csv_files, key='id'):
    """
    Read CSV files and merge them into a dictionary using the csv library.

    Parameters:
    - csv_files (list): List of paths to the CSV files to be merged.

    Returns:
    dict: The resulting dictionary.
    """
    # Initialize an empty dictionary to store the merged data
    merged_dict = {}

    # Iterate through each CSV file
    for file in csv_files:
        # Open the CSV file and create a CSV reader
        with open(file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Extract the 'id' field from the row
                id = row.pop(key)
                # Add the row data to the dictionary with 'id' as the key
                try:
                    merged_dict[id].update(row)
                except KeyError:
                    merged_dict[id] = row

    return merged_dict
