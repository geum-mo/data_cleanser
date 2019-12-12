#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ['""""-누구세요? - 나야""""', '누구?', '- 강금모 - 그게 누구지?', '문 열라고!', '짜잔!'],
        "B": [
            "Who's it? - It's me.",
            "Who?",
            '""Geummo". Not sure who you are"?',
            "Open the door!",
            "Ta-da!",
        ],
    },
    dtype="category",
)


df["A"] = df["A"].str.replace('"',"'")
df["A"] = df["A"].str.replace("''","'")
df["A"] = df["A"].str.replace("''","'")

# print(df.loc[df["A"].str.count("'")>2])
# print(df.loc[df["A"].str.contains("''")])
# print(df.loc[df["A"].str.contains('"')])


print(df)


df["B"] = df["B"].str.replace("'",'"')


# print(df.loc[df["B"].str.contains('^("")|("")$')])

df["B"] = df["B"].str.replace(r'\\w"m', r"\\w'm")
df["B"] = df["B"].str.replace(r'\\w"re',r"\\w're")
df["B"] = df["B"].str.replace(r'\\w"s',r"\\w's")
df["B"] = df["B"].str.replace(r'\\w"ll',r"\\w'll")
df["B"] = df["B"].str.replace(r'\\w"d',r"\\w'd")
df["B"] = df["B"].str.replace(r'\\w"t',r"\\w't")

print(df)

'''
df["B"] = df["B"].str.replace('..."','"...')
df["B"] = df["B"].str.replace('."','".')
df["B"] = df["B"].str.replace(',"','",')
df["B"] = df["B"].str.replace('!"','"!')
df["B"] = df["B"].str.replace('....','...')
df["B"] = df["B"].str.replace('.....','...')
'''

'''

s = df.sample(n=3)
s1 = s.sample (n=1)
s2 = s.drop(s1.index, axis=0)
# print(s1)
# print(s2)

r = df.drop(s.index, axis=0)

print(r)

'''


# S1. i said, "sdfsf".
# S2. "what do you mean"?
# S3. "Did she say "What""?