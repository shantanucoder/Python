#this program is used for renaming a file to a new name with the ability to change the extension of the said file ...


import os
oldname = input("Enter the name of the file to rename")
newname = input("Enter the new name of the file:")

with open(oldname, "r") as f:
    text = f.read()

with open(newname, "w") as f:
    f.write(text)

os.remove(oldname)