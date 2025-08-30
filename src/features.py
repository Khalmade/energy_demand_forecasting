import pandas as pd

def create_features(df):
    # Cyclical
    df['Hour'] = df['Date Time'].dt.hour #0-23
    df['Day'] = df['Date Time'].dt.dayofweek #Mon=0, Sun=6
    df['Month'] = df['Date Time'].dt.month #Jan=1, Dec=12

    # Lag_Features
    df['Lag_hour'] = df['National Unsuppressed Demand'].shift(1)
    df['Lag_day'] = df['National Unsuppressed Demand'].shift(24)
    df['Lag_week'] = df['National Unsuppressed Demand'].shift(168)

    # Rolling Window Features
    df['Demand_Rolling_mean_24'] = df['National Unsuppressed Demand'].shift(1).rolling(window=24).mean()
    df['Demand_Rolling_std_24'] = df['National Unsuppressed Demand'].shift(1).rolling(window=24).std()
    df['Demand_Rolling_median_24'] = df['National Unsuppressed Demand'].shift(1).rolling(window=24).median()

    
    return df


def is_weekend(date_time):
    return date_time.dayofweek >= 5