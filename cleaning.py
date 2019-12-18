import numpy as np
import pandas as pd

def drop_rows(df, cond, fn_name):
    print(f"-{len(df.loc[cond,:].index)} << # of rows to be removed: {fn_name}")
    df = df.drop(df.loc[cond, :].index)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def remove_nan(df):
    # print(f'={len(df)}')
    rows = np.where(pd.isnull(df))[0]
    idx = df.loc[rows,:]
    print(f"-{len(set(rows))} << # of rows with NaN values")
    df = df.dropna()
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def duplicates(df):
    dups = df.duplicated(subset=0, keep="first")
    length = len(dups) - dups.value_counts().loc[False]
    print(f"-{length} << # of duplicated rows")
    df = df.drop(df.index[dups], axis=0)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def long_sents(df):
    cond = df[0].str.len() | df[1].str.len() > 108
    drop_rows(df,cond,long_sents)
    return df

def same_cols(df):
    cond = df[0] == df[1]
    drop_rows(df,cond,same_cols)
    return df

def third_lang(df):
    # print(f'={len(df)}')
    df2 = pd.read_csv("./dataset/unusual.csv", header=None)
    # print(df2.loc[57511:,1])
    list = []
    list2 =[]
    for row in df2.loc[57511:,1]:
        list.append(row)
    # print(list)
    for w in list: 
        cond = df[1].str.contains(w)
        if cond.any():
            idx = df.loc[cond].index
            for e in idx:
                list2.append(e)
        else:
            pass
    # print(set(list2))   
    print(f"-{len(set(list2))} << # of rows containing 3rd foreign languages")
    
    # print(df.loc[set(list2),:])
    df = df.drop(df.iloc[list2,:].index)
    df.index = range(len(df))
    print(f"={len(df)}")
    # print(df)
    return df