#!/usr/bin/python
import os

host = "95.31.3.231"
print("Enter username: ")
user = input()
print("Enter filename: ")
filename = input()
print("Enter path: ")
path = input()

os.system("scp " + filename + " " + user + "@" + host + ":" + path)