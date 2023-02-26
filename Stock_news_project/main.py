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







    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
