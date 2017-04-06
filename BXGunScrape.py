import csv
import gspread
import json
import os
import requests
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

url = "http://www.nydailynews.com/search-results/search-results-7.113?q=shot%2C+bronx%2C+gun&sortOrder=desc&selecturl=site&pdate=2017-03-01&edate=2017-12-31&tfq=articles"
page = requests.get(url)

page_results = BeautifulSoup(page.content, 'html.parser')

soup_search = page_results.find('div', class_='rtww')
links = []
append_url = " http://www.nydailynews.com"

for link in soup_search.find_all('a'):
	links.append(link.get('href'))
	#print links

result_file = open(os.path.abspath('BXVR.csv'), 'wb')

with result_file as f:
	write_to_file = csv.writer(f, dialect="excel", lineterminator='\n');
	for val in links:
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
