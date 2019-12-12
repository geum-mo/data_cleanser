#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pandas as pd
pd.set_option('display.max_rows', 100)

""" Reading a csv file """

path = "./dataset/inProg_main4.csv"
df = pd.read_csv(path, header=None)
# print(df)
print(f"{len(df)} << Starting length of data")

df.columns = ["ko", "en"]


""" Removing rows with NaN values """

df = df.dropna()
df.index = range(len(df))
print(f"={len(df)} << NaN removed")


""" Ensuring no double quotes contained in Korean column """

df["ko"] = df["ko"].str.replace('"',"'")
df["ko"] = df["ko"].str.replace("''","'")
df["ko"] = df["ko"].str.replace("''","'")
df["ko"] = df["ko"].str.replace("'\s'","''")

# print(df.loc[df["ko"].str.count("'")>2])
# print(df.loc[df["ko"].str.contains("''")])
# print(df.loc[df["ko"].str.contains('"')])

""" Eusuring no single quote contained in English column """

df["en"] = df["en"].str.replace("'",'"')

df["en"] = df["en"].str.replace('"m',"'m")
df["en"] = df["en"].str.replace('"ve',"'ve")
df["en"] = df["en"].str.replace('"re',"'re")
df["en"] = df["en"].str.replace('"s',"'s")
df["en"] = df["en"].str.replace('"ll',"'ll")
df["en"] = df["en"].str.replace('"d',"'d")
df["en"] = df["en"].str.replace('"t',"'t")

df["en"] = df["en"].str.replace('""','"')
df["en"] = df["en"].str.replace('""','"')
df["en"] = df["en"].str.replace('"\s"','""')
# df["en"] = df["en"].str.replace('?"','"?') >>> Raises an error

print(df.loc[(df["ko"].str.contains('"""|""."'))|(df["en"].str.contains('"""|""."'))])


'''
manyQuotes = df.loc[df["en"].str.count('"')>2]
doubleDouble = df.loc[df["en"].str.contains('""')]

manyQuotes.to_csv("./dataset/manyQuotes.csv", header=None, index=False)
doubleDouble.to_csv("./dataset/doubleDouble.csv", header=None, index=False)
# print(df.loc[df["en"].str.contains("'")])
'''

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

VAL.to_csv(savePath1, sep="\t", index=False, header={"ko","en"}, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
TEST.to_csv(savePath2, sep="\t", index=False, header={"ko","en"}, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
TRAIN.to_csv(savePath3, sep="\t", index=False, header={"ko","en"}, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
