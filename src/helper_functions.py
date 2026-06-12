import pandas as pd

def calculate_win_rate(df):
    return (df['Profit_Flag'].mean() * 100)

def average_profit_by_sentiment(df):
    return df.groupby('classification')['Closed PnL'].mean()

def total_profit_by_sentiment(df):
    return df.groupby('classification')['Closed PnL'].sum()

def trade_volume_by_sentiment(df):
    return df.groupby('classification')['Size USD'].mean()