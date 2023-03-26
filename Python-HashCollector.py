____author____ = "Jose Arturo Sraiz-Muniz"

____description____= "Python script reads the contents of a directory and collects their hashes, and saves them to a text document for later scanning."

____Date_____ = "03/25/2023"



#-------------IMPORTS---------------------------------------
# this 'import' statement will import from 'os' to be able to read down the list directory 
from os import listdir, getcwd
from os.path import isfile, join, normpath, basename


# this import statement will import the library to hash
import hashlib
#-------------END-OF-IMPORTS---------------------------------




# the first part of the code will be to hash the files and save them in a monitoring file that can be used to monitor those hashes

# this function will call on the user to acquire the path of the directory and read every file within the specfified directory
def get_files():

    path_specified = input("Enter path of file or directory specified: ")
    return [join(path_specified, f) for f in listdir(path_specified) if isfile(join(path_specified, f))]
# END of get_files function

# this function will hash every file in the directory and their filename
def get_hashes():
    # this will call on the failes
    files = get_files()

    # creates an array that will contain the number and names of files
    list_of_hashes = []

    #the for loop will call on every file in the array and repeat the process of hashing the file until theres no more in the array
    for each_file in files:
        hash_md5 = hashlib.md5()  # will hash to md5, weak but first try
        with open(each_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        #this will add the name of the file in the array with their hash
        list_of_hashes.append('{}\n'.format(basename(each_file), hash_md5.hexdigest()))
        # this will write append only their hashes to the array 
        
    return list_of_hashes
# END of get_hashes_filename function

# this function will ask user where to save the filename and hashes
def write_hashes():
    hashes = get_hashes()

    # this will ask the user to enter the file to save filenames/hashes
    # provide complete path to file
    file_save_path = input("Enter path of the file to save file hashes with filenames: ")
    with open(file_save_path, 'w') as f:
        for md5_hash in hashes:
            f.write(md5_hash)
    
# END of write_hashes_filenames function

# this line of code is used as to run the code as a script
#if __name__ == '__main__':
    write_hashes()
    





#--------------------------END-OF-SECTION-01---------------------------