"""
Lambdata is a class object for basic data manipulation.
It has 3 manipulationmethods for manipulating Pandas DataFrames:
    - tt_split: returns a training and testing set
    - null_count: returns the sum of all null values
    - list_to_column: transforms a list to a column
    and joins it with a given dataframe

The object has the attribute data, of type pandas dataframe

Author: Jacob Torres
Version: 0.0.1
Published on 07 May 2021
https://test.pypi.org/project/lambdata-jr/0.0.1/
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class Lambdata:

    def __init__(self, data):
        """
        Lambdata instantiates with a dataframe argument.
        Its methods are tt_split, null_count, and list_to_column.
        """

        try:
            e = "The data must be in a list or other collection."
            self.data = pd.DataFrame(data)

        except ValueError:
            print(e)
            return

    def tt_split(self, frac):
        """
        Returns the training and testing dataframes,
        where frac = fraction that is training data.
        """

        if type(frac) == 'int':
            frac = float(frac)

        try:
            e = """
            The fraction of the data that is split for training
            must be a decimal between 0.0 and 1.0.
            """

            if type(frac) != 'float':
                raise TypeError

            elif frac not in range(0.0, 1.0):
                raise ValueError

        except (TypeError, ValueError):
            print(e)
            return

        df = self.data.copy()
        train, test = train_test_split(df, train_size=frac)

        return train, test

    def null_count(self):
        """
        Returns the sum of nulls in the dataframe.
        """

        df = self.data.copy()
        sum = 0

        for col in df.columns:
            sum += df[col].isnull().sum()

        return sum

    def list_to_column(self, list, column_name):
        """
        Transforms a python list/array into a pandas series,
        then returns the dataframe with the new series as a column.
        """

        try:
            e = f"""
            The list must be of length {len(self.data)}.
            """

            if len(list) != len(self.data):
                raise ValueError

        except ValueError:
            print(e)
            return

        df = self.data.copy()
        series = pd.Series(list)
        series.name = column_name
        new_df = df.join(series)

        return new_df
