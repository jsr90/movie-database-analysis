#!/usr/bin/ python
# -*- coding: utf-8 -*-
import time
import unittest


class BaseTest(unittest.TestCase):
    test_order = None

    def run_(self):
        """
        Run the tests suite and display the results.
        """
        print('\n', '-' * 50)
        print(f"Test {self.test_order}")
        print("*" * 50)
        time.sleep(0.5)
        try:
            suite = unittest.TestLoader().loadTestsFromTestCase(self.__class__)
            unittest.TextTestRunner(verbosity=2).run(suite)
            time.sleep(0.5)
            print(f"\n...tests {self.test_order} finalizado.\n")
        except SystemExit:
            pass

    def run_all(self):
        self.run_()
