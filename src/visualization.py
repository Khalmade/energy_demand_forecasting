import pandas as pd
import matplotlib.pyplot as plt

def hourly_demand_summary(df: pd.DataFrame) -> pd.Series:
    return df.groupby(df["Date Time"].dt.hour)['National Unsuppressed Demand'].mean()

def plot_hourly_demand(df):
    df["Date Time"] = pd.to_datetime(df["Date Time"])
    hourly_demand = df.groupby(df["Date Time"].dt.hour)['National Unsuppressed Demand'].mean()
    plt.plot(hourly_demand.index, hourly_demand.values)
    plt.title("Average Hourly National Unsuppressed Demand")
    plt.xlabel("Hour of Day")
    plt.ylabel("Demand (MW)")
    plt.xticks(hourly_demand.index)
    plt.grid()
    plt.show()


#Daily Demand Visualization
def daily_demand_summary (df: pd.DataFrame) -> pd.Series:
    return df.groupby(df['Date Time'].dt.dayofweek)['National Unsuppressed Demand'].mean()


def plot_daily_demand(df: pd.DataFrame):
    unsuppressed_daily_demand = df.groupby(df['Date Time'].dt.dayofweek)['National Unsuppressed Demand'].mean()
    plt.title("Average Daily Energy Demand")
    plt.xlabel("Day")
    plt.ylabel("Average Demand (MW)")
    plt.plot(unsuppressed_daily_demand.index, unsuppressed_daily_demand.values)
    plt.xticks(unsuppressed_daily_demand.index, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.grid()
    plt.show()


#Monthly Demand Visualization
def monthly_demand_summary(df: pd.DataFrame) -> pd.Series:
    return df.groupby(df['Date Time'].dt.month)['National Unsuppressed Demand'].mean()

def plot_monthly_demand(df: pd.DataFrame):
    unsuppressed_monthly_demand = df.groupby(df['Date Time'].dt.month)['National Unsuppressed Demand'].mean()
    plt.title("Average Monthly Energy Demand")
    plt.xlabel("Month")
    plt.ylabel("Average Demand (MW)")
    plt.plot(unsuppressed_monthly_demand.index, unsuppressed_monthly_demand.values)
    plt.xticks(unsuppressed_monthly_demand.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid()
    plt.show()