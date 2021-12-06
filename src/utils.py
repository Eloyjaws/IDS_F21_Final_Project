import pandas as pd

DATA_DIR = "Data/productivity/"

def get_productivity_countries_list():
    return list(pd.read_csv(f'{DATA_DIR}productivity_transposed.csv')['Entity'])

def get_productivity_data():
    return pd.read_csv(f'{DATA_DIR}productivity.csv')
