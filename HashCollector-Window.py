# this is to make a window appear to start scanning using the hash collector python script
# cant use print inside tkinter window frame, and other functions


from tkinter import *



class VirusTotal_Window:
    
    def __init__(self): 
        root=Tk()
    
        root.Title("HashCollector-Window.py") 
        
        frame_big = Frame(root, bg="white", hieght=700, width=700)
        frame_big.grid()
        
        label1 = Label(root, text="Malware Analysis ")
        label1.pack()
        
        button1 = Button(root, text="Scan suspicious hash", command=self.button1)
        button1.pack() 
        
        button2 = Button(root, text="Upload hash file to VirusTotal")
        button2.pack()



        root.mainloop()

