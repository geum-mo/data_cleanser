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

samples = s.sample(n=19998, random_state=1)

samples = s.sample(n=19998)
VAL = samples.sample(n=9999)
TEST = samples.drop(VAL.index, axis=0)
TRAIN = df.drop(samples.index, axis=0)

print(VAL)
print(TEST)
print(TRAIN)


""" 
for e in VAL.index:
    if e in (TEST.index) | (TRAIN.index):
        print(f'{e} is duplicated')
    else:
        print(f'{e} in validation file is not duplicated')
        pass
for e2 in TEST.index:
    if e2 in (VAL.index) | (TRAIN.index):
        print(f'{e2} is duplicated')
    else: 
        print(f'{e2} in test file is not duplicated')
        pass
for e3 in TRAIN.index:
    if e3 in (VAL.index) | (TEST.index):
        print(f'{e3} is duplicated')
    else:
        print(f'{e3} in train file is not duplicated')
        pass
""" 

savePath1 = "./dataset/validation.tsv"
savePath2 = "./dataset/test.tsv"
savePath3 = "./dataset/train.tsv"

VAL.to_csv(savePath1, sep="\t", index=False, header={"ko","en"})
TEST.to_csv(savePath2, sep="\t", index=False, header={"ko","en"})
TRAIN.to_csv(savePath3, sep="\t", index=False, header={"ko","en"})
