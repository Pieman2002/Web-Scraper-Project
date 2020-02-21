import tkinter as tk

def input_entry_fields():
    One = e1.get()
    Two = e2.get()
    Three = e3.get()
    Four = e4.get()
    if (One != '') and (Two != '') and (Three != '') and (Four != ''):
        print(One, Two, Three, Four)
    

master = tk.Tk()
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)
master.minsize(200,120)
master.maxsize(400,300)
tk.Label(master, 
         text="Test One").grid(row=0)
tk.Label(master, 
         text="Test Two").grid(row=2)
tk.Label(master, 
         text="URL").grid(row=4)
tk.Label(master, 
         text="Test Four").grid(row=6)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1, sticky='NSEW')
e2.grid(row=2, column=1, sticky='NSEW')
e3.grid(row=4, column=1, sticky='NSEW')
e4.grid(row=6, column=1, sticky='NSEW')
# For resizable elements within window
master.grid_columnconfigure(0,weight=5)
master.grid_columnconfigure(1,weight=5)
master.grid_columnconfigure(2,weight=1)
master.grid_rowconfigure(0,weight=1)
master.grid_rowconfigure(1,weight=6)
master.grid_rowconfigure(2,weight=1)
master.grid_rowconfigure(3,weight=6)
master.grid_rowconfigure(4,weight=1)
master.grid_rowconfigure(5,weight=6)
master.grid_rowconfigure(6,weight=1)

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

tk.mainloop()
