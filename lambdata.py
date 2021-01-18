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
Published on 18 Jan 2021
https://test.pypi.org/project/lambdata-jacob-torres/
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

        if type(data) != 'pandas.core.frame.DataFrame':
            raise TypeError(
                "Lambdata cannot accept data with a type other than Pandas DataFrame."
            )

        self.data = data


    def tt_split(frac):

        """
        Returns the training and testing dataframes,
        where frac = fraction that is training data.
        """

        df = self.data.copy()
        train, test = train_test_split(df, train_size=frac)

        return train, test


    def null_count():

        """
        Returns the sum of nulls in the dataframe.
        """

        df = self.data.copy()
        sum = 0

        for col in df.columns:
            sum += df[col].isnull().sum()

        return sum


    def list_to_column(list, column_name):

            """
            Transforms a python list/array into a pandas series,
            then returns the dataframe with the new series as a column.
            """

        df = self.data.copy()
        series = pd.Series(list)
        series.name = column_name
        new_df = df.join(series)

        return new_df
