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
