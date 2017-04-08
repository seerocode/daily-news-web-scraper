# daily-news-web-scraper
My first web scraper. Very basic version. WIP as of 4/6/2017

## Built for

Research project to compile data on gun violence in the Bronx and surrounding areas + contributing factors

## Notes

This web scraper is built in Python and being used to scrape article links from The Daily News search website. The scraper is needed so my research advisor and I do not have to manually go through articles in the TDN and figure out which one we should use. Too much work. Automated.

## To-Dos (in no certain order)

Whatever has a :construction: emoji is what I am currently working on as of last commit. Also, some of these to-dos are extensions built on top of this scraper.

- [ ] :construction: Fix up style of code as it's all over the place (flesh out methods, remove redundant code, etc.)
- [ ] Extend search to multiple pages (this is half working as pagination goes deeper than 13 pages but it only captures the first 13)
- [ ] Build web interface to type in any search URL from Daily News and return a list of articles from that search
- [ ] Iterate on interface to allow for custom search terms to be applied to the Daily News search from the interface and return full list of articles for that search
- [ ] Allow export of articles links as json
- [ ] :construction: Connect newspaper API to interface with web and display the articles in a readable format
- [ ] Connect list to database to allow user removal of a document from web interface if it does not fit the specified criteria (e.g. article is vague, doesn't relate to gun violence, dupe, etc.)
- [ ] Allow user to add article to 
- [ ] Highlight key words in extracted article text
- [ ] :construction: Extract titles of articles, dates, and author (from HTML tags)
- [ ] :construction: Connect Google Sheets to scraper
- [ ] :construction: Display the article content on web
