#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["-누구세요? - 나야", "누구?", "- 강금모 - 그게 누구지?", "문 열라고!", "짜잔!"],
        "B": [
            "- Who's it? - It's me.",
            "Who?",
            "- Geummo. - Not sure who you are?",
            "Open the door!",
            "Ta-da!",
        ],
    },
    dtype="category",
)

# counts = df["A"].str.count("-")

noMatch = pd.DataFrame(df["A"].str.count("-") != df["B"].str.count("-"))
# print(noMatch)
# print(len(noMatch[0].index[noMatch[0] == True]))
# df = df.drop(df.index[noMatch[0].index[noMatch[0] == True]], axis=0)
# print(df)
df.index = range(len(df))
# (df["A"].str.contains("- ")
# (df["B"].str.contains("- ")

# print(df)
listA = df["A"].str.count("-")
listB = df["B"].str.count("-")

# print(df.iloc[np.where(listA | listB > 2)])
# print(len(df.iloc[np.where(listA | listB > 2)]))

# df = df.drop(df.index[np.where(listA | listB > 2)], axis=0)


df = df.replace(to_replace="^-|^\s", value="", regex=True)
# print(df)

# print(df.explode(df["A"].str.split(pat="-")))

df["A"] = df["A"].str.split(pat="\s-|-\s|\s-\s")
df["B"] = df["B"].str.split(pat="\s-|-\s|\s-\s")

print(df)

col_list = df.columns
"""
for col in col_list:
    lens = df[col].str.len()
    print(lens > 1)
"""

list = [1, 2, 3, 4]
for i in list:
    print(i > 2)

print(pd.DataFrame(data=list) > 1)

"""
def explode(df, lst_cols, fill_value=""):
    # make sure `lst_cols` is a list
    if lst_cols and not isinstance(lst_cols, list):
        lst_cols = [lst_cols]
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


print(explode(df, lst_cols=[0, 1]))
"""

# df = df.drop(df.index[["A"].str.count("-") > 2], axis=0)

"""
if listA[0] | listB[0] > 0:
    print(
        df[
            (df["A"].str.count("-") != df["A"].str.count("- "))
            | (df["B"].str.count("-") != df["B"].str.count("- "))
        ]
    )
"""

# def noWhiteSpaceRight(column)


# def noWhiteSpaceLeft(column)

# df = df.drop(df.index[blank_rows], axis=0)  # Removes the blank rows

