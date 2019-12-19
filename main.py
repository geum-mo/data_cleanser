#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from cleaning import * 
from parsing import * 
from ioFile import * 

df = r_tsv("test") # change filename for upload
print(df)
print(f'={len(df)} << Starting #')

df = remove_nan(df)
df = duplicates(df)
df = same_cols(df)
df = long_sents(df)
df = third_lang(df)

df = empty_brckts(df)
df = incons_brckts(df)
df = many_brckts(df)

df = many_qts(df)
df = many_dshs(df)
df = incons_dshs(df)

df = unusuals(df)

df = outliers(df)

""" From here, column has been labeled """









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