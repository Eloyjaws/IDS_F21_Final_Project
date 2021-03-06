import pandas as pd
from pathlib import Path, PurePath

DATA_DIR = (Path(__file__).parent.parent)
DATA_DIR = DATA_DIR.joinpath("Data")

def get_productivity_countries_list():
    return list(pd.read_csv(DATA_DIR.joinpath('productivity/productivity_transposed.csv'))['Entity'])

def get_productivity_data():
    return pd.read_csv(DATA_DIR.joinpath('productivity/productivity.csv'))

def get_ml_data():
    return pd.read_csv(DATA_DIR.joinpath('ml/prediction_dataset.csv'))

def get_inclusivity_data():
    df = pd.read_csv(DATA_DIR.joinpath('viz/scores_3i_2021.csv'))
    country_list = list(df['Country'])

    return country_list, df
