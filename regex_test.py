""" #1. Filter rows where # of sentences in each column is not matched """

f1 = df.loc["ko"].str.count(r"(\B-\B)") != df.loc["en"].str.count(r"(\B-\B)")

""" #2. Filter rows quotes ('' or "") are not properly used """

f2_1 = df.loc["ko"].str.count('"') > 0 | df.loc["en"].str.count((r"\B'\B)")) > 0
f2_2 = df.loc["ko"].str.count("'")%2 != 0 | df.loc["en"].str.count('"')%2 != 0
f2_3 = df.loc["ko"].str.contains(r'\"\"\"') | df.loc["ko"].str.contains(r"\'\'\'")
f2_4 = df.loc["en"].str.contains(r'\"\"\"') | df.loc["en"].str.contains(r"\'\'\'")

""" #3. Filter rows brackets ([]) are not properly used """

f3_1 = df.loc["ko"].str.contains(r'\[') != df.loc["en"].str.contains(r'\[')
f3_2 = df.loc["ko"].str.count(r'\[') != df.loc["ko"].str.contains(r'\]')
f3_3 = df.loc["en"].str.count(r'\[') != df.loc["en"].str.contains(r'\]')