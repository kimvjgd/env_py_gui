import tkinter as tk

window = tk.Tk()

window.title("Label Tutorial")
window.geometry("800x480")

label = tk.Label(window, text="Insert your text")
label.grid(row=0, column=0, pady=5, padx=5)

entry = tk.Entry(window)
entry.grid(row=0, column=1, pady=5, padx=5)

label1 = tk.Label(window, text="Your text")
label1.grid(row=1, pady=5, padx=5)

def label_reload():
    upText = entry.get()
    label1.configure(text=upText)
    label1.after(100, label_reload)

label_reload()

window.mainloop()