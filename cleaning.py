import numpy as np
import pandas as pd

def remove_nan(df):
    rows = np.where(pd.isnull(df))[0]
    idx = df.loc[rows,:]
    print(f"-{len(set(rows))} << # of rows with NaN values")
    df = df.dropna()
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def duplicates(df, col):
    dups = df.duplicated(col, keep="first")
    print(f"-{len(dups)} << # of rows with NaN values")
    df = df.drop(df.index[dups], axis=0)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def long_sents(df, col1, col2):
    cond = df[col1].str.len() | df[col2].str.len() > 108
    print(f"-{len(df.loc[cond,:].index)} << # of rows where str length > 108")
    df = df.drop(df.loc[cond, :].index)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def same_cols(df, col1, col2):
    cond = df[col1] == df[col2]
    print(
    f"-{len(df.loc[cond,:].index)} << # of rows where both columns have the same strings"
    )
    df = df.drop(df.loc[cond, :].index, axis=0)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df