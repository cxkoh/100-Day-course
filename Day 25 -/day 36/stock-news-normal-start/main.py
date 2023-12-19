import requests
from datetime import datetime
from smtplib import *
my_email = "kohcheexuan@gmail.com"
password = "ltjqanxevewvbsxt"
STOCK_NAME = "SOFI"
COMPANY_NAME = "SoFi Technologies"
api_key = "SG6YU45ZYC1WUD2I"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
p={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}
STOCK_ENDPOINT = requests.get(url="https://www.alphavantage.co/query",params= p)
news_api_key = "d51d57757a9e40ef8577ad64f724476d"
q={
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key
}
response_news = requests.get(url=NEWS_ENDPOINT, params=q)
articles = response_news.json()["articles"]
three_articles = articles[:3]
formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
body = []
for article in formatted_article:
    message = article
    body.append(message)
    print(message)


if datetime.now().weekday() in [1,2,3,4,5,6]:
    data = STOCK_ENDPOINT.json()['Time Series (Daily)']
    first_date = next(iter(data))
    print(data[first_date])
    open_price = data[first_date]["1. open"]
    close_price = data[first_date]["4. close"]
    high_price = data[first_date]["2. high"]
    change = ((float(close_price)-float(open_price))/float(open_price))*100
    if change<-5 or change>5:
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"subject:{STOCK_NAME} news \n\nstock: {STOCK_NAME}\nopen price: {open_price}\nclose price: {close_price}\npeak price: {high_price}\n% change: {change}.\nnews: {body}")
            




