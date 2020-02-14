# Scraper! Go wild 
# This will consist of the combined code (and documentation) of all parties.

import requests
import re
from bs4 import BeautifulSoup

url = "https://katu.com/resources/ftptransfer/katu/traffic/traffic.html"
page  = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
results = soup.find_all("div", attrs={"class":"cwcReport Oregon"})
ResultStr = str(results)


#records = []
#for result in results:
  #alert = result.find('n">').text[0:-7]
  # lie = result.contents[1][1:-2]
  # explanation = result.find('a').text[1:-1]
  # url = result.find('a')['href']
  #records.append((alert))
 


print(len(results))
print(results)
#print(records)
