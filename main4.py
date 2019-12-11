#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import pandas as pd
# from polyglot.detect import Detector


pd.set_option('display.max_rows', 500)

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

condA = df["ko"].str.len() | df["en"].str.len() > 50 
condB = df["ko"].str.len() | df["en"].str.len() < 80
condA1 = df["ko"].str.len() | df["en"].str.len() <= 50 
condB1 = df["ko"].str.len() | df["en"].str.len() >= 80


s = df.loc[condA & condB]
ns = df.loc[condA1 | condB1]
print(ns)

print(s)
TRAIN1 = ns
TRAIN2 = s.sample(n=1330748, random_state=1)
VALIDATION = s.sample(n=10000, random_state=2)
TEST = s.sample(n=10000, random_state=3)

savePath1 = "./dataset/validation.tsv"
savePath2 = "./dataset/test.tsv"
savePath3 = "./dataset/train1.tsv"
savePath4 = "./dataset/train2.tsv"

VALIDATION.to_csv(savePath1, sep="\t", index=False, header={"ko","en"})
TEST.to_csv(savePath2, sep="\t", index=False, header={"ko","en"})
TRAIN1.to_csv(savePath3, sep="\t", index=False, header={"ko","en"})
TRAIN2.to_csv(savePath4, sep="\t", index=False, header={"ko","en"})

