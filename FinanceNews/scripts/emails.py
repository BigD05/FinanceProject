from  django.core.mail import send_mail
from stocks.models import Stocknews,Subtype
from django.contrib.auth.models import User


def run():
	daily_subscription = []
	daily_news = {}
	subtype = Subtype.objects.all()
	users = User.objects.all()
	stocks_email = 'finanacialnews24@gmail.com'
	
	if subtype.get(daily_sub=True):
		daily_subscription = list(subtype)
	
	
	for obj in daily_subscription:
		user_email = obj.user.email
		username = obj.user.username
		stocks = obj.stock_ticker.all()
		for i in stocks.iterator():
			stock_obj = Stocknews.objects.get(stock_name=i)
			daily_news[i] = stock_obj.stock_news
	
	for key in daily_news:
		if len(daily_news) == 0:
			pass
		else:
			message = f"{key} : {daily_news[key]}\n"
			subject = "Your stocks news"
			send_mail(subject,f"All the news we could find on the stocks\n{message}",stocks_email,[user_email],fail_silently=True)
		