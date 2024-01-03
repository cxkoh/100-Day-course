from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
insta_user = "luminar_lighter"
insta_pass = "wss2017A!"
search= "crocflameco"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
class Instagram_login:
    def __init__(self, insta_user, insta_pass, driver):
        self.url= "https://www.instagram.com/"
        self.driver = driver
        self.driver.get(self.url)
        self.usern = insta_user
        self.passw = insta_pass

    def login(self):
        user = self.driver.find_element(by=By.NAME, value='username')
        user.send_keys(self.usern, Keys.ENTER)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(self.passw, Keys.ENTER)

    def no_notification(self):
        notification = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notification.click()

    def search(self,searchs):
        search_enter = self.driver.find_element(by=By.NAME,
                                                value="search")
        search_enter.click()
        search = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="mount_0_0_OG"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search.send_keys(searchs, Keys.ENTER)

    def find_followers(self, search):
        time.sleep(5)
        # Show followers of the selected account.
        self.driver.get(f"https://www.instagram.com/{search}/followers")

        time.sleep(5.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def Follow(self):
        time.sleep(2)
        for i in range(1,10):
            Xpath = f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button/div/div'
            print(Xpath)
            modal = self.driver.find_element(by=By.XPATH, value=Xpath)
            modal.click()




insta_login = Instagram_login(insta_user, insta_pass, driver)
time.sleep(3)
insta_login.login()
time.sleep(5)
insta_login.no_notification()
time.sleep(1)
insta_login.find_followers(search)
time.sleep(5)
insta_login.Follow()

#/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div
#/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[3]/div/button
#/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[3]/div/div/div/div[3]/div/button/div/div