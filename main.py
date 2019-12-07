import numpy as np
import pandas as pd

path = "/Users/geummokang/Documents/GitHub/data_cleanser/dataset/test.tsv"

f = pd.read_csv(path, sep="\t")

print(f)
