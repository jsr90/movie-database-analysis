#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

from exercises.ejercicio_3 import Ejercicio3
from tests.base_test import BaseTest


class Test3(BaseTest):
    """
    A tests case class for testing utility functions in utils_3 module.
    """
    test_order = 3
    ej3 = Ejercicio3()

    def setUp(self):
        """
        Set up a sample DataFrame for testing.
        """
        self.df = pd.DataFrame({
            'name': ['name_0', 'name_1', 'name_2', 'name_3', 'name_4'],
            'original_name': ['name_0_o', 'name_1_o', 'name_2_o', 'name_3_o', 'name_4_o'],
            'original_language': ['en', 'es', 'en', 'ja', 'en'],
            'overview': ['a mystery crime', 'banana', 'my crime', 'apple', 'nothing'],
            'status': ['Canceled', 'ok', 'Canceled', 'ok', 'Canceled'],
            'first_air_date': ['2023-01-01', '2020-01-01', '2020', '2023-012-01', '2023-01-05'],
            'languages': ['en', 'es', 'ja', 'en', 'en, ja'],
            'networks': ['n0', 'n1', 'n2', 'n3', 'n4'],
            'production_companies': ['p0', 'p1', 'p2', 'p3', 'p4']
        })
        self.ej3.set_df(self.df)

    def test_filter_by_value(self):
        """
        Test the get_filtered_df function with value-based filtering.
        """
        self.ej3.ejercicio_3_1()
        filtered_df = self.ej3.filtered_df
        expected_filtered_df = self.df.drop(index=[1, 3, 4])
        pd.testing.assert_frame_equal(filtered_df, expected_filtered_df)

    def test_filter_by_regex(self):
        """
        Test the get_filtered_df function with regex-based filtering.
        """
        self.ej3.ejercicio_3_2()
        filtered_df2 = self.ej3.filtered_df2
        expected_filtered_df2 = self.df.drop(index=[1, 2, 3])
        pd.testing.assert_frame_equal(filtered_df2, expected_filtered_df2)

    def test_combined_filters(self):
        """
        Test the get_filtered_df function with combined filters.
        """
        self.ej3.ejercicio_3_3()
        filtered_df3 = self.ej3.filtered_df3
        expected_filtered_df3 = self.df.drop(index=[0, 1, 3])
        pd.testing.assert_frame_equal(filtered_df3, expected_filtered_df3)
