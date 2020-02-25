import requests 
import re
from bs4 import BeautifulSoup
page = requests.get("https://weather.com/weather/today/l/97202:4:US")
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='today_nowcard-temp')
RawTemp = str(results.find('span'))

if len(RawTemp) == 35:
  temp = RawTemp[15:16]

if len(RawTemp) == 36:
  temp = RawTemp[15:17]

if len(RawTemp) == 37:
  temp = RawTemp[15:18]
