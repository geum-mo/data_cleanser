import numpy as np
import pandas as pd

def empty_brckts(df, col1, col2) 
    cond = df[col1].str.contains("\[]") | df[col2].str.contains("\[]")
    print(f"-{len(df.loc[cond,:].index)} << # of rows containing empty brackets")
    df = df.drop(df[col1].index[cond])
    df.index = range(len(df))
    print(f"={len(df)}")
    return df