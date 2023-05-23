from tkinter import *

from PIL import Image, ImageTk
import os
import sys
import datetime

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
root = Tk()
root.title("dongdong")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

# temp_img = Image.open(resource_path('img/1.png'))
temp_img = Image.open(resource_path('img/1.png'))
resized_temp_img = temp_img.resize((20, 20), Image.ANTIALIAS)

# photo1 = PhotoImage(file=resource_path('img/1.png'))
photo1 = ImageTk.PhotoImage(resized_temp_img)
# photo1.config(width=20, height=20)
photo2 = PhotoImage(file=resource_path('img/2.png'))      
# 그냥 path를 적어줘야하는데... 후..



label2 = Label(root, image=photo1)
label2.pack()

def change():
    label1.config(text='또 만나요')

    global photo2
    label2.config(image=photo2)

btn = Button(root, text='클릭', command= change)
btn.pack()

OWNER = 'envsensorapp'
REPO = 'test_app'

API_SERVER_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"
# access_token = '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'
MY_API_KEY = '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'


import os, sys

def execute_cmd(cmd):
    os.system(cmd)

# execute_cmd('rm terminal_cmd.py')
import subprocess
def firmware_update():
    execute_cmd('rm -r /home/orangepi/python/core/521pyinstaller')
    print('rm 완료')
    
    repo_url = "https://github.com/kimvjgd/521pyinstaller.git"
    destination_folder = '/home/orangepi/python/core/521pyinstaller'
    
    try:
        subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
        print('Process well done')
    except subprocess.CalledProcessError as e:
        print(e)

update_btn = Button(root, text='업데이트', command= firmware_update)
update_btn.pack()

ver_label = Label(root, text='ver5 maybe final')
ver_label.pack()



root.mainloop()

