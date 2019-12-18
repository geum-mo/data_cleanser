import pandas as pd

def read_tsv(filename):
    df = pd.read_csv(f"./dataset/{filename}.tsv", sep="\t", header=None)
    return df

def read_csv(filename):
    df = pd.read_csv(f"./dataset/{filename}.csv", header=None)
    return df

def save_tsv(df, filename):
    df.to_csv(f"./dataset/{filename}.tsv", sep="\t", header=None)

def save_csv(df, filename):
    df.to_csv(f"./dataset/{filename}.csv", header=None)
