#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


""" Reading an in-progress csv file """

path_inProg_main = "./dataset/inProg_main.csv"

df = pd.read_csv(path_inProg_main, header=None)
print(f"{len(df)} << Total length of in-progress(main) data")


""" Naming columns """

df.columns = ["ko", "en"]

""" Spliting rows using - (dash) as a seperater. """

df["ko"] = df["ko"].str.split(pat="\s-|-\s|\s-\s")
df["en"] = df["en"].str.split(pat="\s-|-\s|\s-\s")

print(df)

""" Checking value length in 2 columns is identical """

list = df["ko"].str.len() != df["en"].str.len()
print(df.loc[list])

df = df.drop(df["ko"].index[list], axis=0)


def explode(df, lst_cols, fill_value=""):
    # all columns except `lst_cols`
    idx_cols = df.columns.difference(lst_cols)

    # calculate lengths of lists
    lens = df[lst_cols[0]].str.len()

    if (lens > 0).all():
        # ALL lists in cells aren't empty
        return (
            pd.DataFrame(
                {
                    col: np.repeat(df[col].values, df[lst_cols[0]].str.len())
                    for col in idx_cols
                }
            )
            .assign(**{col: np.concatenate(df[col].values) for col in lst_cols})
            .loc[:, df.columns]
        )
    else:
        # at least one list in cells is empty
        return (
            pd.DataFrame(
                {
                    col: np.repeat(df[col].values, df[lst_cols[0]].str.len())
                    for col in idx_cols
                }
            )
            .assign(**{col: np.concatenate(df[col].values) for col in lst_cols})
            .append(df.loc[lens == 0, idx_cols])
            .fillna(fill_value)
            .loc[:, df.columns]
        )


df = explode(df, lst_cols=["ko", "en"])

savePath = "./dataset/inProg_main2.csv"
df.to_csv(savePath, index=False, header=None)


"""
if listA[0] | listB[0] > 0:
    print(
        df[
            (df["ko"].str.count("-") != df["ko"].str.count("- "))
            | (df["en"].str.count("-") != df["en"].str.count("- "))
        ]
    )
else:
    pass
"""

