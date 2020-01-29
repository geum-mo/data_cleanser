import numpy as np
import pandas as pd

def drop_rows(df, cond, fn_name):
    print(f"-{len(df.loc[cond,:].index)} << # of rows to be removed: {fn_name}")
    df = df.drop(df.loc[cond, :].index)
    df.index = range(len(df))
    print(f"={len(df)}")
    return df

def check_rows(df, cond, fn_name):
    pd.set_option('display.max_rows', None)
    print(f"-{len(df.loc[cond,:].index)} << # of rows to be checked: {fn_name}")
    # print(df.loc[cond,:])
    pd.set_option('display.max_rows', 10)

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
    for w in list: # Need to optimize this block 
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

def unusuals(df):
    df2 = pd.read_csv("./dataset/unusual.csv", header=None)
    list = []
    list2 = []
    for e in (e for e in df2[1] if len(e) > 10):        
        list.append(e) 
        cond = df[1].str.contains(e)
        if cond.any():
            idx = df.loc[cond].index
            for e in idx:
                list2.append(e)
        else:
            pass
    # print(set(list2))   
    print(f"-{len(set(list2))} << # of rows containing unusual words")
    
    # print(df.loc[set(list2),:])
    df = df.drop(df.iloc[list2,:].index)
    df.index = range(len(df))
    print(f"={len(df)}")
    # print(df)
    return df

def outliers(df):
    df.columns = ["ko", "en"]
    df["ko_len"] = df["ko"].str.len()
    df["en_len"] = df["en"].str.len()
    df["ratio"] = (df["en_len"] / df["ko_len"])
    df["std"] = df["ratio"].std()
    df["var"] = df["ratio"] - df["std"] 
    # print(df.loc[df["var"] > 3,["ko","en"]])
    cond = df.loc[df["var"].abs() > 3, ["ko","en"]].index # you can change variance
    # print(cond)
    drop_rows(df,cond,outliers)
    return df