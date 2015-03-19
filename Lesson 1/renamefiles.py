import os
def renamefiles():
    # (1) get file names from a folder
    file_list = os.listdir(r"D:\Udacity\Part 3\Lesson 1\prank")
    #print (file_list)
    saved_path = os.getcwd()
    #print("Current working directory is "+saved_path)
    os.chdir(r"D:\Udacity\Part 3\Lesson 1\prank")
    # (2) for each file, rename the file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))

renamefiles()
