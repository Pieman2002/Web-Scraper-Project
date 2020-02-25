import tkinter as tk
from tkinter import messagebox


# The main window
def input_entry_fields():
    sender = e1.get()
    yournumber = e2.get()
    account_sid = e3.get()
    auth_token = e4.get()
    if (sender != '') and (yournumber != '') and (account_sid != '') and (auth_token != ''):
        messagebox.showinfo(title="Success",message="Scraper set!")
        return(sender, yournumber, account_sid, auth_token)
    else:
        messagebox.showerror(title='Error', message='Please fill all fields!')
    
# Within main window
master = tk.Tk()
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)
master.minsize(300,120)
master.maxsize(450,230)
tk.Label(master, 
         text="Trial Number").grid(row=0)
tk.Label(master, 
         text="Your Phone Number").grid(row=2)
tk.Label(master, 
         text="Twilio Account SID").grid(row=4)
tk.Label(master, 
         text="Twilio Authorization Token").grid(row=6)

# Input fields
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

# Main window grid - the weight allows cleaner resizing
e1.grid(row=0, column=1, sticky='NSEW')
e2.grid(row=2, column=1, sticky='NSEW')
e3.grid(row=4, column=1, sticky='NSEW')
e4.grid(row=6, column=1, sticky='NSEW')
# For resizable elements within window
master.grid_columnconfigure(0,weight=5)
master.grid_columnconfigure(1,weight=5)
master.grid_columnconfigure(2,weight=1)
master.grid_rowconfigure(0,weight=1)
master.grid_rowconfigure(1,weight=7)
master.grid_rowconfigure(2,weight=1)
master.grid_rowconfigure(3,weight=7)
master.grid_rowconfigure(4,weight=1)
master.grid_rowconfigure(5,weight=7)
master.grid_rowconfigure(6,weight=1)

# Quit and continue buttons
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=7, 
                                    column=0, 
                                    sticky=tk.NSEW, 
                                    pady=4)
tk.Button(master, 
          text='Scrape', command=input_entry_fields).grid(row=7, 
                                                       column=1, 
                                                       sticky=tk.NSEW, 
                                                       pady=4)


# Running the main window
tk.mainloop()
