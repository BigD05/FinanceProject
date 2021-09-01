from  django.core.mail import send_mail
from stocks.models import Stocknews,Subtype
from django.contrib.auth.models import User


def run():
	weekly_news = {}
	weekly_subscription = []
	subtype = Subtype.objects.all()
	users = User.objects.all()
	stocks_email = 'finanacialnews24@gmail.com'

	if subtype.get(weekly_sub=True):
		weekly_subscription = list(subtype)

		
	for obj in weekly_subscription:
		user_email = obj.user.email
		username = obj.user.username
		stocks = obj.stock_ticker.all()
		for i in stocks.iterator():
			stock_obj = Stocknews.objects.get(stock_name=i)
			weekly_news[i] = stock_obj.stock_news
	
	for key in weekly_news:
		if len(weekly_news) == 0:
			pass
		else:
			message = f"{key} : {weekly_news[key]}\n"
			subject = "Your stocks news"
			send_mail(subject,f"All the news we could find on the stocks\n{message}",stocks_email,[user_email],fail_silently=True)
		
	