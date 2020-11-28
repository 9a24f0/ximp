# Web scraper for wikimedia

import re
import json
import requests
from bs4 import BeautifulSoup


URLS = 'https://radiopaedia.org/search?fbclid=IwAR1w46Ai6R5Yqiwucw6L_gM9o3dwVN_YC5pazixzs0oYf94r-lzODd1nKEI&lang=us&page={}&q=pneumonia&scope=cases'

def getImgUrls(html):
	urls = []

	url = html.find_all('img', {'src':re.compile('.jpg|.png|.svg|.jpeg|.JPEG|.JPG')}, class_="media-object centered-image")

	for pic in url:
		link = pic['src']
		fullsize = link.replace('thumb', 'jumbo')
		urls.append(fullsize)

	return urls

def getLabels(html):
	labels = []
	label = html.find_all('h4', class_ = 'search-result-title-text')
	#label = html.find('h4', {'class': 'search-result-title-text'}).string
	for la in label:
		labels.append(la.text)
	return labels

if __name__ == '__main__':
	content = []
	for i in range(27):
		page_number = str(i+1)
		URL = URLS.format(page_number)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		result = soup.find(id='content')
		urls = getImgUrls(result)
		labels = getLabels(result)
		
		for i in range(len(urls)):
			img = {
			'title': labels[i],
			'link': urls[i]
			}
			content.append(img)
	
	with open('radio_urls.json', 'w') as js:
		json.dump(content, js, indent =4)
	
