import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from wifi import Cell, Scheme
import wifi
import subprocess

class WifiConnectionScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi):
        super().__init__(parent)
        self.controller = controller
        self.show_wifi = show_wifi
        
        