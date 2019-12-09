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


""" Divide rows for [] """

# Check if the number of [] is identical b/w 2 columns

noMatch_br1 = pd.DataFrame(df[0].str.count("\[]") != df[1].str.count("\[]"))
nmIndex_br1 = noMatch_br1[0].index[noMatch_br1[0] == True]
print(f"-{len(nmIndex_br1)} << rows containing inconsistent brackets ([])")
# print(df.iloc[df.index[nmIndex_br1], :])
df = df.drop(df.index[nmIndex_br1], axis=0)
df.index = range(len(df))

noMatch_br2 = pd.DataFrame(df[0].str.count("\[") != df[1].str.count("\["))
nmIndex_br2 = noMatch_br2[0].index[noMatch_br2[0] == True]
print(f"-{len(nmIndex_br2)} << rows containing inconsistent brackets ([)")
# print(df.iloc[df.index[nmIndex_br2], :])
df = df.drop(df.index[nmIndex_br2], axis=0)
df.index = range(len(df))

noMatch_br3 = pd.DataFrame(df[0].str.count("\]") != df[1].str.count("\]"))
nmIndex_br3 = noMatch_br3[0].index[noMatch_br3[0] == True]
print(f"-{len(nmIndex_br3)} << rows containing inconsistent brackets (])")
# print(df.iloc[df.index[nmIndex_br3], :])
df = df.drop(df.index[nmIndex_br3], axis=0)
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


""" Check if any - (dash) without a single whitespace on the right and Print """

listA = df[0].str.count("-")
listB = df[1].str.count("-")


if listA[0] | listB[0] > 0:
    print(
        df[
            (df[0].str.count("-") != df[0].str.count("- "))
            | (df[1].str.count("-") != df[1].str.count("- "))
        ]
    )
else:
    pass


""" Look up and remove duplicated rows """

"""
# Look up duplicates, it returns a Boolean Series
duplicates = df.duplicated([0], keep="first")
print(len(duplicates))

# Returns Dataframe of True value
print(df[df.duplicated([0], keep="first")])

# Remove duplicates
duplicates_removed = df.drop(df.index[duplicates], axis=0)
print(len(duplicates_removed))
"""

""" Print a specific or a range of rows """

# 1. A specific row:
#   print(df.loc[22562])
# 2. A range of row:
#   print(df.loc[22562:22566])

""" Print a specific value or a range of value """

# 1. A specific value:
#   print(df[0].loc[22562])
# 2. A range of value:
#   print(df[0].loc[22562:22566])

""" Look up for a row containing specific strings in its value """

# condition0 = df[0].str.contains('"""|\n|\r|&#39;') # They don't exist
# condition1 = df[1].str.contains('"""|\n|\r|&#39;') # They don't exist
# print(df.loc[condition0 == True])
# print(df.loc[condition1 == True])

'''

print(df[0].str.contains('""').value_counts())  # You need to index a column.
print(df[0].str.contains('"""').value_counts())  # You need to index a column.
print(df[1].str.contains('""').value_counts())  # You need to index a column.
print(df[1].str.contains('"""').value_counts())  # You need to index a column.

'''

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
