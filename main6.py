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
