#!/usr/bin/python
import os, sys

path = "img/"
dirs = os.listdir(path)
i = 0
for file in dirs:
    i = i+1
    if(i > 500):
        os.remove("img/" + file)