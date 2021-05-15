# Lambdata
### Jacob A. Torres
Version 0.0.4
https://github.com/jacob-torres/Lambdata-Jacob-Torres/

This is a test Python package. It contains a module called Lambdata
which holds some basic Pandas DataFrame manipulation functionality.

---

## Lambdata

This module, Lambdata.py, holds a class of the same name.
The Lambdata object is instantiated with a required parameter, "data."
This argument must be of type pandas DataFrame for the Lambdata object to work properly.

The following methods can be used by calling Lambdata.method_name:

### tt_split

This method takes a float between 0.0 and 1.0 as its argument.
The argument, "frac," represents the fraction of the
original dataset which should be used as training data,
as opposed to the fraction which should be used as testing data (1 - frac.) 

Within the method, the
[SKLearn module train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
is used to randomly split the data into training and testing sets,
whose sizes are determined by the frac argument.

### null_count

The method null_count simply returns an integer representing
the number of null values in the dataframe.

### list_to_column

Finally, the list_to_column method takes a list --
which could be any collection of values --
and a string called "column_name" for naming the new column.

If the length of the list is not the same as that of the dataframe,
the method throws an error. Similarly, the method does not accept a single value,
such as a string, number, or other single object.

---

## Download Using Pip

Download and use the package from TestPypi:

`pip install --index-url https://test.pypi.org/simple/ Lambdata-Jacob-Torres`

