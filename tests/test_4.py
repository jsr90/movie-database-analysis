#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

from exercises.ejercicio_4 import Ejercicio4
from tests.base_test import BaseTest


class Test4(BaseTest):
    """
    A tests case class for testing utility functions in utils_4 module.
    """
    test_order = 4
    ej4 = Ejercicio4()

    def setUp(self):
        """
        Set up a sample DataFrame for testing.
        """
        data = {'first_air_date': ['1950-01-15', '1961-02-25', '1972-03-10', '1983-04-22', '1994-05-08',
                                   '2005-06-12', '2016-07-17', '2017-08-29', '2020-09-05', '2023-10-18'],
                'type': ['Action', 'Drama', 'Comedy', 'Sci-Fi', 'Thriller',
                         'Action', 'Drama', 'Comedy', 'Sci-Fi', 'Thriller'],
                'genres': ['Action', 'Drama, Romance', 'Comedy, Romance',
                           'Sci-Fi, Action', 'Thriller, Mystery', 'Action, Adventure',
                           'Drama, Romance', 'Comedy, Romance', 'Sci-Fi, Action',
                           'Thriller, Mystery']}
        self.ej4.df = pd.DataFrame(data)
        self.expected_data = pd.DataFrame({'decade': ["1950's", "1960's", "1970's", "1980's", "1990's",
                                                      "2000's", "2010's", "2010's", "2020's", "2020's"],
                                           'debut_year': ['1950', '1961', '1972', '1983', '1994',
                                                          '2005', '2016', '2017', '2020', '2023']})

    def test_prepared_df(self):
        """
        Tests the right calculation of decade and debut_year
        """
        self.ej4.ejercicio_4_1()
        prepared_data = self.ej4.prepared_df[['decade', 'debut_year']]
        pd.testing.assert_frame_equal(prepared_data, self.expected_data)
