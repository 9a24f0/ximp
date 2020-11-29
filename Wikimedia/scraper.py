# Web scraper for wikimedia

import re
import json
import requests
from bs4 import BeautifulSoup


#URL = 'https://commons.wikimedia.org/w/index.php?search=Pneumonia+x-ray&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'
URL = 'https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=500&offset=0&profile=default&search=Pneumonia+x-ray&advancedSearch-current={}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'
#URL = 'https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=50&offset=0&profile=default&search=Pneumonia+x-ray&advancedSearch-current={}&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1'

def getImgUrls(html):
	start = []
	end = []
	urls = []

	url_start = html.find_all('img', {'src':re.compile('.jpg|.png')})
	url_end = html.find_all('a', {'href':re.compile('.jpg|.png|.svg')}, class_="image")

	for pic in url_end:
		if '.pdf' in pic['href'] or '.djvu' in pic['href']:
			continue
		else:
			link = pic['href'][11:]
			end.append(link)

	for pic in url_start:
		if '.pdf' in pic['src'] or '.djvu' in pic['src']:
			continue
		else:
			link = pic['src'][:46] + pic['src'][52:58]
			start.append(link)
	for i in range(len(start)):
		link = start[i] + end[i]
		urls.append(link)
	return urls

def getLabels(html):
	labels = []
	label = html.find_all('a', {'title':re.compile('.jpg|.png|.svg')})
	for i in label:
		labels.append(i['title'])
	return labels

if __name__ == '__main__':
	content = []
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	result = soup.find(id='mw-content-text')
	urls = getImgUrls(result)
	labels = getLabels(result)
	for i in range(len(urls)):
		img = {
		'title': labels[i],
		'link': urls[i]
		}
		content.append(img)
	with open('data.json', 'w') as js:
		json.dump(content, js, indent=4)