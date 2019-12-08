#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

path = "/Users/geummokang/Documents/GitHub/data_cleanser/dataset/rawDataset.csv"

df = pd.read_csv(path, header=None)

''' Indexing columns '''
# print(df.columns)
# print(df[0])
# print(df[1])

''' Look up for a row containing specific strings in its value '''
# print(df[0].str.contains('"""')) # You need to index a column.
# print(df[1].str.contains('"""')) # It returns Series of Boolean.

'''

''' Replacing multiple 's to a single '.'''

df.replace("'''", "'")
df.replace("''", "'")

print(df[0].str.contains('"""'))
