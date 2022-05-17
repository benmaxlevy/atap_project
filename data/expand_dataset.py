if __name__ == "__main__":
    import pandas as pd
    import requests
    dataset = pd.read_csv("data/dataset.csv", names = ["date", "closures"], skiprows = [0])
    for r in df.iterrows():
        # fetch weather data for the day
        # first, get /points/{points}/stations


