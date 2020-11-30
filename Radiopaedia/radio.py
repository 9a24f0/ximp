import re
import json
import requests
from bs4 import BeautifulSoup

URLS = 'https://radiopaedia.org/search?fbclid=IwAR1w46Ai6R5Yqiwucw6L_gM9o3dwVN_YC5pazixzs0oYf94r-lzODd1nKEI&lang=us&page={}&q=pneumonia&scope=cases'
def getModularity(html):
	modules = []
	types = html.find_all('div', class_ = 'search-result-modalities')
	for box in types:
		temp = []
		typez = box.find_all('span', class_ ='label label--grey')
		for i in range(len(typez)):
			temp.append(typez[i].text)
		modules.append(temp)
	return modules
def getImgUrls(html, modules):
	urls = []
	
	url = html.find_all('img', class_ = 'media-object centered-image')
	
	for i in range(len(url)):
		if 'CT' in modules[i] or 'Annotated image' in modules[i] or 'Barium' in modules[i] or 'DSA (angiography)' in modules[i] or 'Diagram' in modules[i] or 'Fluoroscopy' in modules[i] or 'MRI' in modules[i] or 'Mammography' in modules[i] or 'Nuclear medicine' in modules[i] or 'Pathology' in modules[i] or 'Photo' in modules[i] or 'Ultrasound' in modules[i]:
			continue
		else:
			link = url[i]['src']
			fullsize = link.replace('thumb', 'jumbo')
			urls.append(fullsize)

	return urls

def getLabels(html, modules):
	labels = []

	label = html.find_all('h4', class_ = 'search-result-title-text')

	for i in range(len(label)):
		if 'CT' in modules[i] or 'Annotated image' in modules[i] or 'Barium' in modules[i] or 'DSA (angiography)' in modules[i] or 'Diagram' in modules[i] or 'Fluoroscopy' in modules[i] or 'MRI' in modules[i] or 'Mammography' in modules[i] or 'Nuclear medicine' in modules[i] or 'Pathology' in modules[i] or 'Photo' in modules[i] or 'Ultrasound' in modules[i]:
			continue
		else:
			labels.append(label[i].text)
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
		modules = getModularity(result)
		urls = getImgUrls(result, modules)
		labels = getLabels(result, modules)
		#print(urls)
		#print(labels)
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
	