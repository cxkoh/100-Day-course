'''import pandas
import random
from smtplib import *

my_email = "kohcheexuan@gmail.com"
password = "ltjqanxevewvbsxt"

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="shanekoh@ymail.com",
        msg="Subject:Hello\n\nThis is the body of my mail")
connection.close()'''


my_email = "kohcheexuan@gmail.com"
password = "ltjqanxevewvbsxt"
from smtplib import *
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()
if day == 4:
    with open(file="quotes.txt",mode= "r") as data:
        quote = data.readlines()
        selected_quote = random.choice(quote)
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"subject:Monday motivation \n\n{selected_quote}")







