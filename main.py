#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from cleaning import * 
from parsing import * 
from ioFile import * 

df = r_csv("rawDataset_combined") # change filename for upload
print(df)
print(f'={len(df)} << Starting #')

df1 = remove_nan(df)
df2 = duplicates(df1)
df3 = same_cols(df2)
df4 = long_sents(df3)
df5 = third_lang(df4)

df6 = empty_brckts(df5)
df7 = incons_brckts(df6)
df8 = many_brckts(df7)

df9 = many_qts(df8)
df10 = many_dshs(df9)
df11 = incons_dshs(df10)

df12 = unusuals(df11)

df13 = outliers(df12)

""" From here, column has been labeled """
sampling(df13)







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