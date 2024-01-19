#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

import pandas as pd

from exercises.ejercicio_2 import Ejercicio2
from tests.base_test import BaseTest


class Test2(BaseTest):
    """
    A tests case class for testing utility functions in utils_2 module.
    """
    test_order = 2
    ej2 = Ejercicio2()

    def test_airtime_duration(self):
        """
        Test the airtime_duration function with various scenarios.
        """
        # Create a list of cases
        cases = [('2022-01-01', '2022-01-01', 0), ('2022-01-01', '2022-01-02', 1), ('2022-02-29', '2023-02-28', -1),
                 ('2022-01-01', '2022-02-29', -1), ('2022-01-01', '2022-12-31', 364), ('2024-01-01', '2024-12-31', 365),
                 ('2022-01-05', '2022-01-01', -1)]

        # Create a dataframe with cases
        df = pd.DataFrame()
        for i, c in enumerate(cases):
            start_date = c[0]
            end_date = c[1]
            expected_result = c[2]
            sample_row = pd.Series(
                {'id': f'id_{i}', 'name': f'name_{i}',
                 'first_air_date': start_date, 'last_air_date': end_date,
                 'expected_result': expected_result})
            df = pd.concat([df, sample_row], axis=1, ignore_index=True)

        # Testing the 'airtime_duration' function for each scenario.
        self.ej2.set_df(df.T)
        self.ej2.ejercicio_2_1()
        df = self.ej2.get_df()
        result = df['air_days']
        expected_result = df['expected_result'].astype(int)
        self.assertTrue(result.equals(expected_result))

    def test_get_ordered_dict(self):
        """
        Test the get_ordered_dict function with different DataFrame scenarios.
        """
        # Test 4 cases
        data = {'name': ['Movie1', 'Movie2', 'Movie3', 'Movie4'],
                'homepage': ['http://example.com', 'http://example2.com', None, None],
                'poster_path': ['/poster1.jpg', None, '/poster2.jpg', None]}
        df = pd.DataFrame(data)
        self.ej2.set_df(df)
        self.ej2.ejercicio_2_2()
        result = self.ej2.ordered_dict
        expected_result = OrderedDict({'Movie1': 'http://example.com//poster1.jpg',
                                                 'Movie2': 'NOT AVAILABLE',
                                                 'Movie3': 'NOT AVAILABLE',
                                                 'Movie4': 'NOT AVAILABLE'})
        self.assertEqual(result, expected_result)
