import tkinter as tk
from tkinter import filedialog, Text
import os

root= tk.Tk()

def change_bg():
    frame.config(background='red')

def res_co():
    frame.config(background='white')

canvas=tk.Canvas(root, height=700,width=700, bg="#263D42")

frame=tk.Frame(root, bg="white")

frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)
openFile = tk.Button(root,text="Change Color", padx=10, pady=5, fg="white", bg="#263D42", command=change_bg)

openFile.pack()

runApps = tk.Button(root,text="Reset", padx=10, pady=5, fg="white", bg="#263D42", command=res_co)
runApps.pack()
root.mainloop()