import os
#
# print("Python Program to print list the files in a directory.")
#
# Direc = input(r"Enter the path of the folder: ")
# print(f"Files in the directory: {Direc}")
#
# files = os.listdir(Direc)
# files = [f for f in files if os.path.isfile(Direc + '/' + f)]  # Filtering only the files.
# print(*files, sep="\n")


root='D:/AutomationFramework/TestScripts/CRM'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
for x in dirlist:
    print(x)


