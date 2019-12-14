#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

""" Read the following article to grasp the basic of pandas """
""" https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/ """


""" Combining multiple files (csv format) into one """

"""
path_official = "./dataset/rawDataset.csv"

path_open = "./dataset/rawDataset_open.csv"

path_combined = "./dataset/rawDataset_combined.csv"

df_official = pd.read_csv(path_official, header=None)
df_open = pd.read_csv(path_open, header=None)

with open(path_combined, mode="a") as f:
    df_official.to_csv(f, header=None, index=None)
    df_open.to_csv(f, header=None, index=None)

df = pd.read_csv(path_combined, header=None)

# print(len(df_official))
# print(len(df_open))
print(len(df_official) + len(df_open) == len(df)) # If True, it's been properly combined
"""

""" Reading a combined csv file """

path_combined = "./dataset/rawDataset_combined.csv"
df = pd.read_csv(path_combined, header=None)
print(f"{len(df)} << Total length of row data")

""" Indexing columns """
# print(df.columns)
# print(df[0])
# print(df[1])

""" Searching indexes with empty values (NaN) & Remove rows """

blank_rows = np.where(pd.isnull(df))[0]  # Returns an array of rows

'''
def checkIfDuplicates_1(listOfElems):
    """ Check if given list contains any duplicates """
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


result = checkIfDuplicates_1(blank_rows)

if result:
    print("Yes, list contains duplicates")
else:
    print("No duplicates found in list")
'''

# print(df.blank_rows)
print(f"-{len(set(blank_rows))} << blank rows")
# print(len(blank_rows))
# print(np.where(pd.isnull(df))[1]) # Return an array of columns
# print(len(df.drop(df.iloc[blank_rows, :], axis=0)))
# print(df.iloc[blank_rows, :])
# df = df.drop(df.index[blank_rows], axis=0)  # Removes the blank rows
df = df.dropna()
df.index = range(len(df))
# print(df)
print(f"={len(df)}")




""" Divide rows for - """

# Check if the number of - is identical b/w 2 columns

noMatch_ds = pd.DataFrame(df[0].str.count("-") != df[1].str.count("-"))
nmIndex_ds = noMatch_ds[0].index[noMatch_ds[0] == True]
print(f"-{len(nmIndex_ds)} << rows containing inconsistent dashes")
df = df.drop(df.index[nmIndex_ds], axis=0)
df.index = range(len(df))
# print(df)
print(f"={len(df)}")


""" Handle -s (dashes) """

""" Remove rows containing more than 2 -s (dashes) """

listA = df[0].str.count("-")
listB = df[1].str.count("-")
print(
    f"-{len(df.iloc[np.where(listA | listB > 2)])} << rows containing more than 2 -s (dashes)"
)
df = df.drop(df.index[np.where(listA | listB > 2)], axis=0)
df.index = range(len(df))
print(f"={len(df)}")

""" Remove first -s including the whitespace(s) on the right """
# print(len(df[0|1].str.contains("^-|^\s-")))
print(df)
df = df.replace(to_replace="^-|^\s-|^-\s", value="", regex=True)
print(df)
# print(df[0].str.contains("\S-\S"))
# print(df[1].str.contains("\S-\S"))

savePath = "./dataset/inProg_main.csv"
df.to_csv(savePath, index=False, header=None)
"""

df[0] = df[0].str.split(pat="\s-|-\s|\s-\s")
df[1] = df[1].str.split(pat="\s-|-\s|\s-\s")
print(df)


savePath_type = "./dataset/types_main.csv"


df.dtypes.to_frame("types").to_csv(savePath_type)


"""

