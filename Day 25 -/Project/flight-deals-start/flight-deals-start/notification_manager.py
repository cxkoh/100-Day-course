from smtplib import SMTP
class NotificationManager:
    def __init__(self):
        self.email = "kohcheexuan@gmail.com"
        self.password = "ltjqanxevewvbsxt"
    def send(self,msg):
        with SMTP("smtp@gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email,password=self.password)
            connection.sendmail(to_addrs=self.email, from_addr=self.email, msg=msg)
