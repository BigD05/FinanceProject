import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from django.contrib.auth.models import User
from stocks.models import Stocknews

def run():
	Stocknews.objects.all().delete()
	names = []
	ticker = []

	url = 'https://www.advfn.com/nasdaq/nasdaq.asp'

	page = requests.get(url)
	soup = BeautifulSoup(page.text,'html.parser')
	odd_rows = soup.find_all('tr',attrs={'class':'ts0'})
	even_rows = soup.find_all('tr',attrs={'class':'ts1'})

	for k in  odd_rows:
		row  = k.find_all('td')
		names.append(row[0].text.strip())
		ticker.append(row[1].text.strip())

	for k in  even_rows:
		row  = k.find_all('td')
		names.append(row[0].text.strip())
		ticker.append(row[1].text.strip())





	date = datetime.today().strftime('%Y-%m-%d')
	api_key = "EJrNICI1cx7espOUKtsRSErMbwlKLpQp"
	news = {}
	for i in ticker:
		try:
			api_url = f"https://api.polygon.io/v2/reference/news?limit=10&order=descending&sort=published_utc&ticker={i}&published_utc.gte={date}&apiKey={api_key}"
			data = requests.get(api_url).json()
			all_news = data['results'][0]['description']
			news[i] = all_news
		except :
			news[i] = "Sorry there is No news on this stock today"
	for key,k in zip(news,names):
		Stocknews.objects.create(stock_name=k, stock_ticker=key, stock_news=news[key])
		


	



