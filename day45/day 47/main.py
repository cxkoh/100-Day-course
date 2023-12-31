import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.com/Nintendo-SwitchTM-Neon-Blue-Joy%E2%80%91ConTM-Switch/dp/B0BFJWCYTL/ref=sr_1_1?crid=3OFYV3XI12VOQ&keywords=nintendo%2Bswitch&qid=1703744471&sprefix=nintendo%2Bswitch%2Caps%2C334&sr=8-1&th=1'
r=requests.get("https://www.amazon.com/Nintendo-SwitchTM-Neon-Blue-Joy%E2%80%91ConTM-Switch/dp/B0BFJWCYTL/ref=sr_1_1?crid=3OFYV3XI12VOQ&keywords=nintendo%2Bswitch&qid=1703744471&sprefix=nintendo%2Bswitch%2Caps%2C334&sr=8-1&th=1", headers={ 'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
soup= BeautifulSoup(r.text, "html.parser")
price = soup.select_one(".a-offscreen").getText()

from smtplib import *
my_email = "kohcheexuan@gmail.com"
password = "ltjqanxevewvbsxt"
prices = float(price[1:])
if prices < 300:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"nintendo switch is at a low price")