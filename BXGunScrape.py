import csv
import gspread
import json
import os
import requests
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


news_search_url = 'http://www.nydailynews.com/search-results/search-results-7.113?q=bronx%2C+gun&sortOrder=desc&selecturl=site&pdate=2016-01-01&edate=2016-12-31&tfq=articles'
get_page = requests.get(news_search_url)

page_results = BeautifulSoup(get_page.content, 'html.parser')

soup_search = page_results.find('div', class_='rtww')
tmp_news_links = []

for link in soup_search.find_all('a'):
	tmp_news_links.append(link.get('href'))
	#print links

appended_links = ['http://www.nydailynews.com{0}'.format(l) for l in tmp_news_links]
#add pagination to new array
news_search_pagination = [x for x in appended_links if '&page=' in x]
# Remove page 1 link from search results
news_links = [y for y in appended_links if not '&page=' in y]

def remove_duplicates(news_search_pagination):
    output = []
    seen = set()
    for value in news_search_pagination:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

pagination_result = remove_duplicates(news_search_pagination)

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
