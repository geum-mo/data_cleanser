#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd
from polyglot.detect import Detector


""" Reading an in-progress csv file """

path = "./dataset/inProg_main3.csv"
df = pd.read_csv(path, header=None)
# print(df)
print(f"{len(df)} << Total length of in-progress(main) data")

df.columns = ["ko", "en"]

df = df.dropna()
df.index = range(len(df))
print(f"={len(df)} << NaN removed")

# print(df["en"].str.len().sort_values(ascending=False))
# print(df["ko"].str.len().sort_values(ascending=False))

cond = df["ko"].str.len() | df["en"].str.len() > 108
print(f"-{len(df.loc[cond,:].index)} << Removing rows where str length > 108")
df = df.drop(df.loc[cond, :].index)
df.index = range(len(df))
print(f"= {len(df)}")

# df = df.drop(df.index[df["en"].str.len().sort_values(ascending=False) > 108], axis=0)
# df = df.drop(df.index[df["ko"].str.len().sort_values(ascending=False) > 108], axis=0)

cond = df["ko"] == df["en"]
print(
    f"-{len(df.loc[cond,:].index)} << Removing rows where both columns have the same strings"
)
df = df.drop(df.loc[cond, :].index, axis=0)
df.index = range(len(df))
print(f"= {len(df)}")

"""
for language in Detector(df).languages:
    print(language)
"""

