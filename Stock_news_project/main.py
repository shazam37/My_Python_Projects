import requests
import datetime as dt
from datetime import timedelta
import smtplib
import random

MY_MAIL = 'shazajmal37@gmail.com'
MY_API = '21a371da32d543ff95a5db145c85b826'
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'TSLA',
    'apikey': '3BNP95HZ8IPCHGL3'
}

today = dt.datetime.now().date()
yesterday = today - timedelta(days=1)
day_before = today - timedelta(days=2)
day_before1 = today - timedelta(days=3)

paramed = {
    'q': 'tesla',
    'from': str(yesterday),
    'sortBy':'publishedAt',
    'apiKey':MY_API,
}

data = requests.get(url=STOCK_ENDPOINT, params = parameters)
dictionary1 = data.json()['Time Series (Daily)'][str(day_before)]
dictionary2 = data.json()['Time Series (Daily)'][str(day_before1)]
my_list1 = [value for (key, value) in dictionary1.items()]
my_list2 = [value for (key, value) in dictionary2.items()]

difference = float(my_list1[3]) - float(my_list2[3])
percent_diff = difference/float(my_list2[3])*100

if percent_diff > 5:
    data = requests.get(url=NEWS_ENDPOINT,params=paramed)
    articles = data.json()['articles'][:3]
    my_list = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    for article in my_list:
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password='jouabiojgvmavpzs')
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL,
                                msg=f'Subject: TSLA: {float(percent_diff)}\n\n'
                                    f'{article}')
