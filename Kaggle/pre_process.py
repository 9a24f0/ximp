#!/usr/bin/python

import os, sys
import json

path = "img/"
dirs = os.listdir( path )

content = []
i = 0

for file in dirs:
    i = i + 1
    if (i <= 500):
        img = {
        'title': file,
        'link': "img/" + file
        }
        content.append(img)
    else:
        os.remove("img/" + file)

with open('data.json', 'w') as js:
    json.dump(content, js, indent =4)
