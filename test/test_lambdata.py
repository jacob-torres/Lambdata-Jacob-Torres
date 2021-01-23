"""
This is a unit test module for the functionality of the Lambdata class methods.
"""

import unittest
import numpy as np
import pandas as pd
from lambdata_jacob_torres.Lambdata import Lambdata


class test_lambdata(unittest.TestCase):

    # A testing DataFrame
    df = pd.DataFrame(
        {'a': [1, 2, 3, 4],
        'b': [5, 6, 7, np.NaN],
        'c': [np.NaN, 10, 11, np.NaN]}
    )


    def test_constructor(self):
        """Tests that Lambdata constructor accepts collections."""

        good_arg = ['a', 'b', 'c']
        ld = Lambdata(good_arg)
        self.assertIsInstance(ld, Lambdata)

        bad_arg = "A string. Big nono!"
        ld = Lambdata(bad_arg)
        self.assertRaises(ValueError)


    def test_tt_split(self):
        """Test the tt_split method."""

        bad_arg1 = 5
        bad_arg2 = "It's a string!"
        ld = Lambdata(self.df)

        ld.tt_split(bad_arg1)
        ld.tt_split(bad_arg2)
        self.assertRaises(ValueError)


    def test_null_count(self):
        """Test the null_count method."""

        ld = Lambdata(self.df)
        num_nulls = ld.null_count()
        self.assertEqual(num_nulls, 3)


    def test_list_to_column(self):
        """Test the list_to_column method."""

        good_arg = [13, 14, 15, 16]
        bad_arg = [13, 14, 15, 16, 17]
        ld = Lambdata(self.df)

        good_df = ld.list_to_column(good_arg, 'good_column')
        self.assertEqual(good_df.shape, (4, 4))

        bad_df = ld.list_to_column(bad_arg, 'bad_column')
        self.assertRaises(ValueError)
