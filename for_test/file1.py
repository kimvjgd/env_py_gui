from tkinter import ttk
from tkinter import *


from file2 import AAA

class BBB(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.daemon = True
    
    def get_data(self, value):
        print('value : ', value)
        self.after(1000, value)
    

a = AAA()
b = BBB()
b.get_data(a.get_numnber)