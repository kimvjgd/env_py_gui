import tkinter as tk
from tkinter import ttk

class CH2O(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)