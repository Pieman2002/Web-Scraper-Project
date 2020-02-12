import tkinter as tk

def input_entry_fields():
    One = e1.get()
    Two = e2.get()
    Three = e3.get()
    if (One != '') and (Two != '') and (Three != ''):
        print(One, Two, Three)
    

master = tk.Tk()
tk.Label(master, 
         text="Test").grid(row=0)
tk.Label(master, 
         text="Text").grid(row=1)
tk.Label(master, 
         text="URL").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Scrape', command=input_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
