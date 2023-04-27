import tkinter as tk

my_w = tk.Tk()
my_w.geometry("800x480")

from time import strftime

def my_time():
    time_string = strftime('%H:%M:%S %p')
    l1.config(text=time_string)
    l1.after(1000, my_time)


my_font = ('times', 52, 'bold')
l1 = tk.Label(my_w, font=my_font, bg="yellow")
l1.grid(row=1, column=1, padx=5, pady=25)
my_time()
my_w.mainloop()


