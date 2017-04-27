import csv
import gspread
import json
import os
import requests
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

news_search_url = 'http://www.nydailynews.com/search-results/search-results-7.113?q=bronx%2C+gun&sortOrder=desc&selecturl=site&pdate=2016-01-01&edate=2016-12-31&tfq=articles'
tmp_article_links = []

def scrape(news_search_url):
	get_page = requests.get(news_search_url)
	page_results = BeautifulSoup(get_page.content, 'html.parser')
	soup_search = page_results.find('div', class_='rtww')
	# scrape for current page
	for link in soup_search.find_all('a'):
		tmp_news_links.append(link.get('href'))
		#print links
	
	#appends daily news url to links
	article_links = ['http://www.nydailynews.com{0}'.format(l) for l in tmp_article_links]

#add pagination to new array
news_search_pagination = [x for x in article_links if '&page=' in x]


#remove duplicates in 
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

pagination_result_sf = [r.replace('bronx, gun', 'bronx%2C+gun') for r in pagination_result]

new_page_links = []

### ADD RESULUST FROM MORE PAGES ####
for page in pagination_result_sf:
	get_result = requests.get(page)
	paged_results = BeautifulSoup(get_result.content, 'html.parser')
	paged_soup_search = paged_results.find('div', class_='rtww')
	for l in paged_soup_search.find_all('a'):
		new_page_links.append(l.get('href'))

### KEEP GETTING MORE PAGES ###
# matching = [s for s in new_page_links if '&page=' in s]

# for pages in new_page_links:
# 	while matching:
# 		get_result = requests.get(page)
# 		paged_results = BeautifulSoup(get_result.content, 'html.parser')
# 		paged_soup_search = paged_results.find('div', class_='rtww')
# 		for l in paged_soup_search.find_all('a'):
# 			new_page_links.append(l.get('href'))


new_page_links_appended = ['http://www.nydailynews.com{0}'.format(l) for l in new_page_links]
new_page_result_sf = [r.replace('bronx, gun', 'bronx%2C+gun') for r in new_page_links_appended]
merged_list = new_page_result_sf + appended_links
# Remove page 1 link from search results
news_links = [y for y in merged_list if not '&page=' in y]

#### WRITE TO EXCEL FILE ####
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
