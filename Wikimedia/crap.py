# Web scraper for wikimedia

import re
import json
import requests
from bs4 import BeautifulSoup


#URL = 'https://commons.wikimedia.org/w/index.php?search=Pneumonia+x-ray&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'
URL = 'https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=500&offset=0&profile=default&search=Pneumonia+x-ray&advancedSearch-current={}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'
#URL = 'https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=50&offset=0&profile=default&search=Pneumonia+x-ray&advancedSearch-current={}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id='mw-content-text')
urls = result.find_all('img', {'src':re.compile('.jpg|.png')})
urlos = result.find_all('a', {'href':re.compile('.jpg|.png|.svg')}, class_="image")
labels = result.find_all('a', {'title':re.compile('.jpg|.png|.svg')})

image_url = []
label = []
img_dict = {}
url_last = []
links = []

for pic in urlos:
	if '.pdf' in pic['href'] or '.djvu' in pic['href']:
		continue
	else:
		link = pic['href'][11:]
		url_last.append(link)

for pic in urls:
	if '.pdf' in pic['src'] or '.djvu' in pic['src']:
		continue
	else:
		link = pic['src'][:46] + pic['src'][52:58]
		image_url.append(link)

for i in range(len(image_url)):
	link = image_url[i] + url_last[i]
	links.append(link)

for l in labels:
	label.append(l['title'])

for i in range(len(image_url)):
	img_dict[label[i]] = links[i]

with open('img_link.json', 'w') as js:
	json.dump(img_dict, js)
