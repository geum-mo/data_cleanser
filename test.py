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

text = "강금모"



ratio = df["A"].str.len / df["B"].str.len