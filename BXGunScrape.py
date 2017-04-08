import csv
import gspread
import json
import os
import requests
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

news_search_url = 'http://www.nydailynews.com/search-results/search-results-7.113?q=bronx%2C+gun&sortOrder=desc&selecturl=site&pdate=2016-01-01&edate=2016-12-31&tfq=articles'
get_page = requests.get(news_search_url)

page_results = BeautifulSoup(get_page.content, 'html.parser')

soup_search = page_results.find('div', class_='rtww')
tmp_news_links = []

for link in soup_search.find_all('a'):
	tmp_news_links.append(link.get('href'))
	#print links

news_links = ['http://www.nydailynews.com{0}'.format(s) for s in tmp_news_links]


result_file = open(os.path.abspath('BXVR.csv'), 'wb')

with result_file as f:
	write_to_file = csv.writer(f, dialect="excel", lineterminator='\n');
	for val in news_links:
		write_to_file.writerow([val])

### FOR WRITING TO GSPREADSHEET - WORK IN PROGRESS ###
# json_key = json.load(open(os.path.abspath('Documents/BXVR.json')) 
# scope = [
#     'https://spreadsheets.google.com/feeds',
#     'https://www.googleapis.com/auth/drive'
# ]

# credentials = ServiceAccountCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) 

# file = gspread.authorize(credentials) # authenticate with Google
# sheet = file.open("BXVR").sheet1 # open sheet
