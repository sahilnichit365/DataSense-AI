import pandas as pd

def get_missing_values(df):
    return df.isnull().sum()

def get_duplicate_count(df):
    return df.duplicated().sum()

def remove_duplicates(df):
    return df.drop_duplicates()

def fill_missing_values(df):
    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    return df