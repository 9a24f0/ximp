import re
import json
import requests
from bs4 import BeautifulSoup

URLS = 'https://radiopaedia.org/search?fbclid=IwAR1w46Ai6R5Yqiwucw6L_gM9o3dwVN_YC5pazixzs0oYf94r-lzODd1nKEI&lang=us&page={}&q=pneumonia&scope=cases'

def getImgUrls(html):
	urls = []
	url = html.find_all('img', class_ = 'media-object centered-image')

	for pic in url:
		link = pic['src']
		fullsize = link.replace('thumb', 'jumbo')
		urls.append(fullsize)

	return urls

def getLabels(html):
	labels = []
	label = html.find_all('h4', class_ = 'search-result-title-text')
	for la in label:
		labels.append(la.text)
	return labels

if __name__ == '__main__':
	content = []
	num_of_page = 27
	for i in range(num_of_page):
		page_number = str(i+1)
		URL = URLS.format(page_number)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		result = soup.find(id='content')
		urls = getImgUrls(result)
		labels = getLabels(result)
		print(urls)
		print(labels)
		print(len(urls))
		print(len(labels))
		
		for i in range(len(urls)):
			img = {
			'title': labels[i],
			'link': urls[i]
			}
			content.append(img)
	
	with open('radio_urls.json', 'w') as js:
		json.dump(content, js, indent =4)
	