#!/usr/bin/python
import zipfile
import os

path = os.getcwd()

archive = zipfile.ZipFile(path+"/archive.zip", 'w')

for folder, subfoldes, files in os.walk(path):
    for file in files:
        archive.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), path), compress_type = zipfile.ZIP_DEFLATED)
 
archive.close()


host = "95.31.3.231"
print("Enter username: ")
user = input()
print("Enter path(where to save):")
savepath = input()
os.system("scp " + user + "@" + host + ":archive.rar " + savepath)