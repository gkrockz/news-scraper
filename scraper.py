import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get("https://news.ycombinator.com/news")
parser_obj = BeautifulSoup(response.text, "html.parser")
links = parser_obj.select(".titlelink")
subtext = parser_obj.select(".subtext")

def sort_by_votes(news):
	return sorted(news, key = lambda k:k['votes'], reverse=True)

def custom_news(links, subtext):
	news = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get("href", None)
		vote = subtext[idx].select(".score")
		if len(vote):
			points = int(vote[0].getText().replace(" points",""))
			if points > 100:
				news.append({'title':title,'link':href,'votes':points})
	return sort_by_votes(news)

pprint(custom_news(links, subtext))