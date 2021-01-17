"""
    Helpful Functions Module
    Provides basic data science functionality
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def tt_split(df, frac):


    """
        Returns the training and testing dataframes,
        where frac = fraction of df set aside for testing
    """


    df = df.copy()
    train, test = train_test_split(df, train_size=frac)

    return train, test


def null_count(df):


    """
        Returns the sum of nulls in a dataframe
    """


    df = df.copy()
    sum = 0

    for col in df.columns:
        sum += df[col].isnull().sum()

    return sum


def list_to_column(list, df, column_name):


    """
        Transforms a python list/array into a pandas series,
        then returns the dataframe with the new series as a column.
    """


    df = df.copy()
    series = pd.Series(list)
    series.name = column_name
    new_df = df.join(series)

    return new_df
    