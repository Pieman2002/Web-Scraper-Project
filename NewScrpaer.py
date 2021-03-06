import requests 
import re
import time
from bs4 import BeautifulSoup
from twilio.rest import Client

# GUI Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import unicodedata
 
# GUI class - This allows the program to take things outside of the GUI
class GetEntry():
 
    
 
    # Main window stats
    def __init__(self, master):
 
        self.master=master
        self.master.title('Scraper Inputs')
        self.entry_contents=None
        master.minsize(350,100)
        master.maxsize(400,150)
 
        # Set entries
        
        # First entry
        self.e1 = ttk.Entry(master)
        self.e1.grid(row=0, column=1)
        self.e1.focus_set()
 
        # Second entry
        self.e2 = ttk.Entry(master)
        self.e2.grid(row=2, column=1)
        self.e2.focus_set()
 
 
        # Labels
        ttk.Label(text="Your Phone Number (ONLY numbers)").grid(row=0)
        ttk.Label(text="Delay between checks (No less than 30)").grid(row=2)
 
        # Main window grid - the weight allows cleaner resizing
        self.e1.grid(row=0, column=1, sticky='NSEW')
        self.e2.grid(row=2, column=1, sticky='NSEW')
 
        # For resizable elements within window
        master.grid_columnconfigure(0,weight=5)
        master.grid_columnconfigure(1,weight=5)
        master.grid_columnconfigure(2,weight=1)
        master.grid_rowconfigure(0,weight=2)
        master.grid_rowconfigure(1,weight=1)
        master.grid_rowconfigure(2,weight=2)
 
        # Buttons
        ttk.Button(master, text='Quit', command=master.quit).grid(row=9, column=0, sticky=tk.NSEW, pady=4)
        ttk.Button(master, text='Scrape', command=self.callback).grid(row=9, column=1, sticky=tk.NSEW, pady=4)
 
    # The super special code that makes this whole thing work
    def callback(self):
        print(self.e1.get())
        try:
            if (len(self.e1.get()) == 10) and (int(self.e1.get()) > 1):
                    messagebox.showinfo(title="Success",message="Scraper set! Now running.")
                    # get the contents of the Entries and exit the prompt
                    self.entry_contents=[self.e1.get(),self.e2.get()]
                    self.master.destroy()
            else:
                print('Phone number is not valid')
                messagebox.showerror(title="Oh no!",message="Phone number not valid. Please enter a valid 10 digit number without dashes.")
        except:
            messagebox.showerror(title="Oh no!",message="Phone number not valid. Please enter a valid 10 digit number without letters.")
            pass
# End of GUI code

try:
  f = open("temperature.txt", "w")
  f.write("0")
  f.close()
except IOError:
  f = open("temperature.txt", "w")
finally:
  f.close()



def main():
  
  sender = #Please enter your trial number here.
  account_sid = #Please enter your Account SID here.
  auth_token = #Please enter your Authorization Token here.
  
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
    message = client.messages \
        .create(
             body='The temperature is now '+temp+' degrees',
             from_=sender,
             to=yournumber
        )

    print(message.sid)
  
  
  
  f = open("temperature.txt", "w")
  f.write(temp)
  f.close()
  
  f = open("temperature.txt", "w")
  f.write(temp)
  f.close()
  print(temp)
  
  time.sleep(60)
  main()
  
  
  # Other GUI code
    # Main window stats
    def __init__(self, master):
 
        self.master=master
        self.master.title('Scraper Inputs')
        self.entry_contents=None
        master.minsize(350,100)
        master.maxsize(400,150)
 
        # Set entries
        
        # First entry
        self.e1 = ttk.Entry(master)
        self.e1.grid(row=0, column=1)
        self.e1.focus_set()
 
        # Second entry
        self.e2 = ttk.Entry(master)
        self.e2.grid(row=2, column=1)
        self.e2.focus_set()
 
 
        # Labels
        ttk.Label(text="Your Phone Number (ONLY numbers)").grid(row=0)
        ttk.Label(text="Delay between checks (No less than 30)").grid(row=2)
 
        # Main window grid - the weight allows cleaner resizing
        self.e1.grid(row=0, column=1, sticky='NSEW')
        self.e2.grid(row=2, column=1, sticky='NSEW')
 
        # For resizable elements within window
        master.grid_columnconfigure(0,weight=5)
        master.grid_columnconfigure(1,weight=5)
        master.grid_columnconfigure(2,weight=1)
        master.grid_rowconfigure(0,weight=2)
        master.grid_rowconfigure(1,weight=1)
        master.grid_rowconfigure(2,weight=2)
 
        # Buttons
        ttk.Button(master, text='Quit', command=master.quit).grid(row=9, column=0, sticky=tk.NSEW, pady=4)
        ttk.Button(master, text='Scrape', command=self.callback).grid(row=9, column=1, sticky=tk.NSEW, pady=4)
 
    # The super special code that makes this whole thing work
    def callback(self):
        print(self.e1.get())
        try:
            if (len(self.e1.get()) == 10) and (int(self.e1.get()) > 1):
                    messagebox.showinfo(title="Success",message="Scraper set! Now running.")
                    # get the contents of the Entries and exit the prompt
                    self.entry_contents=[self.e1.get(),self.e2.get()]
                    self.master.destroy()
            else:
                print('Phone number is not valid')
                messagebox.showerror(title="Oh no!",message="Phone number not valid. Please enter a valid 10 digit number without dashes.")
        except:
            messagebox.showerror(title="Oh no!",message="Phone number not valid. Please enter a valid 10 digit number without letters.")
            pass
 
master = tk.Tk()
GetPoints=GetEntry(master)
master.mainloop()
 
# Get inputs out of Tkinter
Points=GetPoints.entry_contents
def test_case(numb):
    try:
        number = int(numb)
        return(number)
    except (TypeError, ValueError):
        number = numb
        return(number)
 
# Make sure that inputs are, in fact, numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
# Dummy delay (just in case)
delay = 0
 
try:
    phonenumber = test_case(Points[0])
    delay = test_case(Points[1])
except:
    exit()
 
# Checking delay
if is_number(delay) == True:
    if delay <= 29:
        delay = 30
else:
    delay = 30
 
print(phonenumber)
print(delay)

if __name__ == "__main__":
  main()
