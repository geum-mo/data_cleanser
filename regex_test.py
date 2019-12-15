""" #1. Filter rows where # of sentences in each column is not matched """

f1 = df.loc["ko"].str.count(r"(\B-\B)") != df.loc["en"].str.count(r"(\B-\B)")

""" #2. Filter rows quotes are not properly used """

f2_1 = df.loc["ko"].str.count('"') > 0 | df.loc["en"].str.count((r"\B'\B)") > 0
f2_2 = (df.loc["ko"].str.count("'"))%2 != 0 | (df.loc["en"].str.count('"'))%2 != 0
