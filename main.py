#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

path = "/Users/geummokang/Documents/GitHub/data_cleanser/dataset/rawDataset.csv"

df = pd.read_csv(path, header=None)

''' Read the following article to grasp the basic of pandas '''
''' https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/ '''


''' Indexing columns '''
# print(df.columns)
# print(df[0])
# print(df[1])

''' Search indexes with empty values (NaN) & Remove rows '''


print(len(df[0]))
blank_rows = np.where(pd.isnull(df))[0]  # Return an array of rows
# print(len(blank_rows))
# print(np.where(pd.isnull(df))[1]) # Return an array of columns
# print(len(df.drop(df.iloc[blank_rows, :], axis=0)))
# print(df.iloc[blank_rows, :])
blank_rows_removed = df.drop(df.index[blank_rows], axis=0)  # Remove rows
print(len(blank_rows_removed))
# print(df.drop([:5, :], axis=0))

''' Print a specific or a range of rows '''

# 1. A specific row:
#   print(df.loc[22562])
# 2. A range of row:
#   print(df.loc[22562:22566])

''' Print a specific value or a range of value '''

# 1. A specific value:
#   print(df[0].loc[22562])
# 2. A range of value:
#   print(df[0].loc[22562:22566])

''' Look up for a row containing specific strings in its value '''

print(df[0].str.contains('누구세요').value_counts())  # You need to index a column.
# It returns Series of Boolean.
# print(df[1].str.contains('"""').value_counts())

# print(df[0].str.contains('"""').value_counts().loc[False])

# print(df[1].str.contains('"""').value_counts().loc[False])

# df[0].replace('누구세요', "누구야")
# df[1].replace('Who is it', "Who's it")

# print(df[0])
# print(df[1])

# print(df[0].str.contains('누구세요'))  # You need to index a column.
# print(df[1].str.contains('Who is it'))  # It returns Series of Boolean.
