###helpful functions module
### Jacob A. Torres

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


def split_dates(date_series):
  """Split datetimes into a dataframe with columns month, day, and year"""

  date_series = pd.to_datetime(date_series, infer_datetime_format=True)
  month = [date.dt.month for date in date_series]
  day = [date.dt.day for date in date_series]
  year = [date.dt.year for date in date_series]

  df = pd.DataFrame(
    {'month': month, 'day': day, 'year': year}
  )

  return df
