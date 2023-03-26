# this is to make a window appear to start scanning using the hash collector python script
# cant use print inside tkinter window frame, and other functions


from tkinter import *
import tkinter as tk
from os import listdir, getcwd
from os.path import isfile, join, normpath, basename
import hashlib


root=Tk()

class VirusTotal_Window:

    def task_option(self):

        root = Tk() 

        root.title('HashCollector-Window.py')

        root.minsize(300,300)
        root.geometry("800x800")

        button1 = Button(root, text="Scan suspicious file specified", command=self.button1 )
        button1.place(x = 368, y = 714.5 )

    def button1(self):
        if self.string.get():
            def get_files():
                path_specified = input("Enter path of file or directory specified: ")
                return [join(path_specified, f) for f in listdir(path_specified) if isfile(join(path_specified, f))]
            # END of inner def function 
            
            def get_hashes():
                files = get_files()
                list_of_hashes = []
                for each_file in files:
                    hash_md5 = hashlib.md5()
                    with open(each_file, "rb") as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            hash_md5.update(chunk)
                    list_of_hashes.append('{}\n'.format(hash_md5.hexdigest()))
                print("file has been hashed")
                
                return list_of_hashes 
            
            def write_hashes():
                hashes = get_hashes()  
                file_save_path = input("Enter path of the file to save file hashes with filenames: ")
                with open(file_save_path, 'w') as f:
                    for md5_hash in hashes:
                        f.write(md5_hash)
            
                print("Hash Saved")

if __name__ == '__main__':
    VirusTotal_Window().mainloop()