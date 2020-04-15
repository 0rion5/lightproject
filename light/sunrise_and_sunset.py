# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime as dt

url = 'https://dateandtime.info/citysunrisesunset.php?id=6028050'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
response.close()
dfs = pd.read_html(str(soup))
sunrise_list = list(dfs[1].Sun.Sunrise)
sunset_list = list(dfs[1].Sun.Sunset)
todays_date = dt.datetime.today().strftime('%a, %B %d').lstrip('0')
for i, v in enumerate(list(dfs[1].Date.Date)):
    if v == todays_date:
        sunrise = sunrise_list[i]
        sunset = sunset_list[i]

# %%
