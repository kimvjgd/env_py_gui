import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class InfoScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        
        self.show_home = show_home
        self.controller = controller
        
        