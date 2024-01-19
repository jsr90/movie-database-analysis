#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import tarfile
import tempfile
import time
import zipfile

from exercises.ejercicio_1 import Ejercicio1
from tests.base_test import BaseTest
from utils.utils_1 import get_execution_time


class Test1(BaseTest):
    """
    A tests case class for testing utility functions in utils_1 module.
    """
    test_order = 1
    ej1 = Ejercicio1()

    def setUp(self):
        """
        Set up a temporary directory and create tests CSV files for testing.
        """
        self.temp_dir = tempfile.mkdtemp()
        self.csv_files = []
        self.zip_file_path = os.path.join(self.temp_dir, 'tests.zip')
        for i in range(3):
            csv_file_path = os.path.join(self.temp_dir, f'test_data_{i}.csv')
            self.csv_files.append(csv_file_path)
            with open(csv_file_path, 'w') as file:
                file.write(f'id,val{i}\n1,{i}0\n2,{i}0\n3,{i}0\n2,{i}0\n')
        with zipfile.ZipFile(self.zip_file_path, 'w') as zip_ref:
            for file in self.csv_files:
                zip_ref.write(file)
        self.ej1.set_path_to_zip(self.zip_file_path)

    def tearDown(self):
        """
        Remove the temporary directory and its contents after testing.
        """
        shutil.rmtree(self.temp_dir)

    def test_unzip(self):
        """
        Test the unzip function with various archive formats.
        """
        # zip file
        self.ej1.set_csv_files(None)
        self.ej1.set_path_to_zip(self.zip_file_path)
        result = self.ej1.get_csv_files()
        self.assertEqual(set(result), set(self.csv_files))

        # tar_gz file
        tar_gz_file_path = os.path.join(self.temp_dir, 'tests.tar.gz')
        with tarfile.open(tar_gz_file_path, 'w:gz') as tar_ref:
            for file in self.csv_files:
                tar_ref.add(file)

        self.ej1.set_csv_files(None)
        self.ej1.set_path_to_zip(tar_gz_file_path)
        result = self.ej1.get_csv_files()
        self.assertEqual(set(result), set(self.csv_files))

        # invalid file format
        invalid_file_path = os.path.join(self.temp_dir, 'tests.txt')
        self.ej1.set_csv_files(None)
        self.ej1.set_path_to_zip(invalid_file_path)
        result = self.ej1.get_csv_files()
        self.assertIsNone(result)

        self.ej1.set_path_to_zip(self.zip_file_path)

    def test_get_execution_time(self):
        """
        Test the get_execution_time function with a time-consuming lambda function.
        """
        result, execution_time = get_execution_time(
            lambda *args: time.sleep(0.1))

        # Check if the result is correct
        self.assertEqual(result, None)

        # Check if the execution time is greater than or equal to 0.1 seconds
        self.assertGreaterEqual(execution_time, 0.1)

    def test_merge_csv_with_pandas(self):
        """
        Test the merge_csv_with_pandas function for merging CSV files using pandas.
        """
        self.ej1.set_csv_files(None)
        self.ej1.set_df(None)
        self.ej1.ejercicio_1_2()
        result_df = self.ej1.get_df()

        # Check if the result DataFrame has the correct columns
        expected_columns = ['id', 'val0', 'val1', 'val2']
        self.assertSetEqual(set(result_df.columns), set(expected_columns))

        # Check if the result DataFrame has the correct values
        expected_values = {'id': [1, 2, 3], 'val0': [0, 0, 0],
                           'val1': [10, 10, 10], 'val2': [20, 20, 20]}
        for column, expected_value in expected_values.items():
            self.assertListEqual(list(result_df[column]), expected_value)

    def test_merge_csv_with_csv_module(self):
        """
        Test the merge_csv_with_csv_module function for merging CSV files using csv module.
        """
        self.ej1.set_csv_files(None)
        self.ej1.set_df(None)
        self.ej1.ejercicio_1_3()
        result_dic = self.ej1.dic

        # Check if the result dictionary has the correct keys
        expected_keys = ['1', '2', '3']
        self.assertListEqual(list(result_dic.keys()), expected_keys)

        # Check if the result dictionary has the correct values
        expected_values = {
            '1': {'val0': '00', 'val1': '10', 'val2': '20'},
            '2': {'val0': '00', 'val1': '10', 'val2': '20'},
            '3': {'val0': '00', 'val1': '10', 'val2': '20'}
        }
        for key, expected_value in expected_values.items():
            self.assertDictEqual(result_dic[key], expected_value)
