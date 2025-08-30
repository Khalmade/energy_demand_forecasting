import pandas as pd


def load_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def load_excel(filepath: str) -> pd.DataFrame:
    return pd.read_excel(filepath)