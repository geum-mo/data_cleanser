import numpy as np
import pandas as pd
from cleaning import drop_rows 

def empty_brckts(df): 
    cond = df[0].str.contains(r"\[]") | df[1].str.contains(r"\[]")
    drop_rows(df,cond,empty_brckts)
    return df

def incons_brckts(df):
    cond = df[0].str.count(r"\[") != df[1].str.contains(r"\[")
    drop_rows(df,cond,incons_brckts)
    return df

def many_brckts(df):
    cond = df[0].str.count(r"\[") | df[1].str.contains(r"\[") > 3
    drop_rows(df,cond,many_brckts)
    return df