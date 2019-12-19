import numpy as np
import pandas as pd
from cleaning import drop_rows, check_rows 


""" Handles improperly used square brackets ([]) """

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


""" Handles improperly used single or double quotes ('' or "") """

def many_qts(df):
    cond = df[0].str.count(r"\'|\"") | df[1].str.contains(r"\'|\"") > 6
    drop_rows(df,cond,many_qts)
    return df


""" Handles improperly used dashes (-) """

def many_dshs(df):
    cond = df[0].str.count(r"\B-\B") | df[1].str.contains(r"\B-\B") > 4
    drop_rows(df,cond,many_dshs)
    return df

def incons_dshs(df):
    cond = df[0].str.count(r"\B-\B") != df[1].str.contains(r"\B-\B")
    check_rows(df,cond,incons_dshs)
    return df