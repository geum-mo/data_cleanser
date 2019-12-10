#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


""" Reading an in-progress csv file """

path = "./dataset/inProg_main2.csv"
df = pd.read_csv(path, header=None)
# print(df)
print(f"{len(df)} << Total length of in-progress(main) data")

""" Naming columns """

df.columns = ["ko", "en"]
# print(df)

""" Looking up rows containing -s """

lst_bool = df["ko"].str.contains("-") | df["ko"].str.contains("-")
index = df["ko"].index[lst_bool]
df.loc[index, :].to_csv("./dataset/noMatch.csv", index=False, header=None)


""" Removing leading & trailing whitespaces """

df["ko"] = df["ko"].str.strip
df["en"] = df["en"].str.strip


""" Removing empty square brackets, if any """

cond = df["ko"].str.contains("\[]") | df["en"].str.contains("\[]")
print(df.loc[cond, :])
df = df.drop(df["ko"].index[cond])
print(len(df))


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
