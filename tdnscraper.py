import csv
import os
import requests
from bs4 import BeautifulSoup
from newspaper import Article


# Placeholder for links
tmp_article_links = []

# Sets the year we are searching for in the url
def set_search_url(year):
	tdnews_url = 'http://www.nydailynews.com/search-results/search-results-7.113?q=bronx,%20gun&selecturl=site&sortOrder=desc&pdate=' + year + '-01-01&edate=' + year + '-12-31&tfq=articles&afq=&page='
	return tdnews_url

def 

def main():
	search_year = input("Please enter the year to search for: ")
	url = set_search_url(search_year)

main()



for page_num in range(1, 46):
	url = 'http://www.nydailynews.com/search-results/search-results-7.113?q=bronx,%20gun&selecturl=site&sortOrder=desc&pdate=2013-01-01&edate=2013-12-31&tfq=articles&afq=&page=' + str(page_num)

	get_page = requests.get(url)
	page_results = BeautifulSoup(get_page.content, 'html.parser')
	soup_search = page_results.find('div', class_='rtww')
	if soup_search:
		# Scrape for current page and add to temporary links array
		for link in soup_search.find_all('a'):
			tmp_article_links.append(link.get('href'))
			#print tmp_article_links
	else:
		# Return alert to user
		print ('Cannot proceed, please check HTML DOM')


# Prepends daily news url to links
article_links = ['http://www.nydailynews.com{0}'.format(l) for l in tmp_article_links]
#print article_links

# Remove paginated links
news_links = [y for y in article_links if not '&page=' in y]
#print news_links

# Create Dictionary
napi_links = []
tmp_article_details = {}


for art_link in news_links:
	article = Article(art_link)
	try:
		article.download()
		article.parse()
		article.nlp()
		tmp_article_details = {
			'title': article.title,
			'keywords': article.keywords,
			'link': article.url,
		}
		napi_links.append(tmp_article_details)
	except Exception:
		print ('we will continue after this short error')
		continue

#print napi_links

#### WRITE TO EXCEL FILE ####

result_file = open(os.path.abspath('BXVR.csv'), 'w')

csv_columns = ['title', 'keywords', 'link']

with result_file as f:
	write_to_file = csv.DictWriter(f, dialect="excel", lineterminator='\n', fieldnames=csv_columns);
	write_to_file.writeheader()
	for value in napi_links:
			write_to_file.writerow(value)
