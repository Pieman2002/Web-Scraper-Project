import requests 
import re
import time
from bs4 import BeautifulSoup

try:
  f = open("temperature.txt", "w")
  f.write("0")
  f.close()
except IOError:
  f = open("temperature.txt", "w")
finally:
  f.close()



def main():
  page = requests.get("https://weather.com/weather/today/l/97202:4:US")
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find(class_='today_nowcard-temp')
  RawTemp = str(results.find('span'))
  PrevTempFile = open("temperature.txt", "r")
  PrevTemp = PrevTempFile.read()
  print(PrevTemp)
  
  PrevTempFile.close()
  
  if len(RawTemp) == 35:
    temp = RawTemp[15:16]

  if len(RawTemp) == 36:
    temp = RawTemp[15:17]

  if len(RawTemp) == 37:
    temp = RawTemp[15:18]
  
  print(temp)
  
  if (int(PrevTemp) == int(temp)) or (int(PrevTemp) == 0):
    print("Temperature is unchanged")
  else:
    print("The temperature is now "+temp+" degrees")
  
  
  
  f = open("temperature.txt", "w")
  f.write(temp)
  f.close()
  
  f = open("temperature.txt", "w")
  f.write(temp)
  f.close()
  print(temp)
  
  time.sleep(60)
  main()
  
if __name__ == "__main__":
  main()
