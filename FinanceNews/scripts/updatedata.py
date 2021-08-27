from stocks.models import Stocknews
from django.contrib.auth.models import User
from datetime import datetime
import requests


def run():
	date = datetime.today().strftime('%Y-%m-%d')
	api_key = "EJrNICI1cx7espOUKtsRSErMbwlKLpQp"
	news = {}
	tickers = []
	stockenews_set = Stocknews.objects.all()
	for values in stockenews_set.iterator():
		tickers.append(values.stock_ticker)
	
	for i in tickers:
		try:
			api_url = f"https://api.polygon.io/v2/reference/news?limit=10&order=descending&sort=published_utc&ticker={i}&published_utc.gte={date}&apiKey={api_key}"
			data = requests.get(api_url).json()
			all_news = data['results'][0]['description']
			news[i] = all_news
		except :
			news[i] = "Sorry there is No news on this stock today"
		
	for key in news:
		Stocknews.objects.filter(stock_ticker=key).update(stock_news=news[key])