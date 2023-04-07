import tkinter as tk
from tkinter import ttk
from tkinter import *


class Sample(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)
        
        btn_0 = Button(self, text="0")
        btn_0.grid(column=0, row=0)
        btn_0 = Button(self, text="1")
        btn_0.grid(column=1, row=1)
        btn_0 = Button(self, text="2")
        btn_0.grid(column=2, row=2)
        
        # self.title("Sample Page")
        
        