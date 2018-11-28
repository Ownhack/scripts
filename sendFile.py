#!/usr/bin/python
import os

# host = "192.168.20.1"
user = input("Enter username: ")
host = input("Enter host: ")
filename = input("Enter filename: ")
path = input("Enter remote path: ")

os.system("scp " + filename + " " + user + "@" + host + ":" + path)
