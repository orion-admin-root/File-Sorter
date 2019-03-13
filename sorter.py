import os, configparser, re, time
from glob import glob
#Reading configfile and parsing folders
config = configparser.ConfigParser()
config.read('Config/config.ini')
loop = config['DEFAULT']['Loop']
loop = int(loop)
files = config['DEFAULT']['Folders']
ndir = len(files)
ndir = int(ndir)
files= re.split('[|]',files)
dircount = 0
#Reading configfile and parsing tags
extensions = config['DEFAULT']['Tags']
next = len(files)
next = int(next)
extensions= re.split('[|]',extensions)
extcount = 0
#Reading configfile for directory to organize
directory = config['DEFAULT']['Directory']
#Getting working path
path = os.getcwd()
#Creating folders if they do not exist
if not directory == "current":
    directory += "/"
    if not os.path.exists(os.getcwd() + "/" + directory):
        os.makedirs(os.getcwd() + "/" + directory)
for i in range(len(files)):
    if not os.path.exists(os.getcwd() + "/" + files[i]):
        os.makedirs(os.getcwd() + "/" + files[i])
#If loop has been enabled, the program awaits for new files, if not then it only runs once
if loop == 0:
    for x in range(len(extensions)):
        all_files = [f for f in os.listdir(path + "/" + directory) if f.endswith(extensions[x])]
        i = 0
        sizeofList = len(all_files)
        while i < sizeofList :
            file = all_files[i]
            os.rename(os.getcwd() + "/" + directory + file , os.getcwd() + "/" + files[x] + "/" + file)
            i += 1
        all_files = []
print("")
print("File Sorter")
print("By Tomás Nobre")
print("All rights reserved")
print("")
while loop == 1:

    print("Awaiting...")
    fileexists = 0
    pattern = directory + "*"
    while (fileexists < 1):
        time.sleep(5)
        if glob(pattern):
            fileexists = 1
            print("Files found")
        else:
            pass
    #Reoragnaizing directory depending on tags
    for x in range(len(extensions)):
        all_files = [f for f in os.listdir(path + "/" + directory) if f.endswith(extensions[x])]
        i = 0
        sizeofList = len(all_files)
        while i < sizeofList :
            file = all_files[i]
            os.rename(os.getcwd() + "/" + directory + file , os.getcwd() + "/" + files[x] + "/" + file)
            i += 1
        all_files = []
