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

print(df)

s = df.sample(n=3)
s1 = s.sample (n=1)
s2 = s.drop(s1.index, axis=0)
print(s1)
print(s2)

r = df.drop(s.index, axis=0)

print(r)


for e in s1.index:
    if e in (s2.index) | (r.index):
        print(f'{e} is duplicated')
    else:
        for e2 in s2.index:
            if e2 in (s1.index) | (r.index):
                print(f'{e2} is duplicated')
            else: 
                for e3 in r.index:
                    if e3 in (s1.index) | (s2.index):
                        print(f'{e3} is duplicated')
                    else:
                        pass
