if __name__ == "__main__":
    import pandas as pd
    import requests
    import os
    import time
    import datetime
    from dotenv import load_dotenv
    load_dotenv("../.env")
    df = pd.read_csv("dataset.csv", names=["date", "closures"], skiprows=[0])
    for r in df.iterrows():
        # fetch weather data for the day from https://api.stormglass.io/v2/weather/point
        # convert the date to UNIX timestamp
        # create python timestamp from r[1]["date"]
        date = datetime.datetime.strptime(r[1]["date"], "%m/%d/%Y")
        unix_timestamp = int(time.mktime(date.timetuple()))
        # get lat and lon from env
        lat = os.getenv("LAT")
        lon = os.getenv("LON")
        # create the request
        url = "https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lon}&start={unix_timestamp}&end={unix_timestamp}"


