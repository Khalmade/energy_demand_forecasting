import pandas as pd
import matplotlib.pyplot as plt

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
    return plt.show()


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
    return plt.show()


!git add .
!git commit -m "Add visualization functions for daily and monthly energy demand"
!git push origin main