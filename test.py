#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["-누구세요? - 나야", "누구?", "- 강금모 - 그게 누구지? - 아 진짜", "문 열라고!", "짜잔!"],
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

print(df)
listA = df["A"].str.count("-")
listB = df["B"].str.count("-")

print(df.iloc[np.where(listA | listB > 2)])
print(len(df.iloc[np.where(listA | listB > 2)]))

print(df.drop(df.index[np.where(listA | listB > 2)], axis=0))

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

