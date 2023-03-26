# this is to make a window appear to start scanning using the hash collector python script


import sys
import os
import tkinter as tk



window = tk.Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run():
    
    entry_label = tk.Label(window, text = "PythonVirusTotal.py Options", font_color='black')
    entry_label.grid(row=0, column=0)
    
    #btn = tkinter.Button(window, text="Start VirusTtotal Scan", bg="blue", fg="white", command=run)
    #btn.grid(column=0, row=1)




    
    

window.mainloop()
