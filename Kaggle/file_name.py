#!/usr/bin/python

import os, sys
import json

path = "img/"
dirs = os.listdir( path )

content = []

for file in dirs:
    img = {
    'title': file,
    'link': "img/" + file
    }
    content.append(img)

with open('data.json', 'w') as js:
    json.dump(content, js, indent =4)
