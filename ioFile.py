import pandas as pd

def r_tsv(filename):
    df = pd.read_csv(f"./dataset/{filename}.tsv", sep="\t", header=None)
    return df

def r_csv(filename):
    df = pd.read_csv(f"./dataset/{filename}.csv", header=None)
    return df

def s_tsv(df, filename):
    df.to_csv(f"./dataset/{filename}.tsv", sep="\t", header=None)

def s_csv(df, filename):
    df.to_csv(f"./dataset/{filename}.csv", header=None)

def sampling(df):
    condA = (df["ko"].str.len() > 50) | (df["en"].str.len() > 50) 
    condB = (df["ko"].str.len() > 50) | (df["en"].str.len() < 80)
    condA1 = (df["ko"].str.len() <= 50) | (df["en"].str.len() <= 50) 
    condB1 = (df["ko"].str.len() <= 50) | (df["en"].str.len() >= 80)

    s = df.loc[condA & condB]
    ns = df.loc[condA1 | condB1]

    samples = s.sample(n=19998)
    VAL = samples.sample(n=9999)
    TEST = samples.drop(VAL.index, axis=0)
    TRAIN = df.drop(samples.index, axis=0)

    s_tsv(VAL, "validation")
    s_tsv(TEST, "test")
    s_tsv(TRAIN, "train")