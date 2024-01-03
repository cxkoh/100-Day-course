from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
url ='https://en.wikipedia.org/wiki/Main_Page'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#click on item
number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(number.text)
number.click()

#find element by link text
all_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portal.click()

#find search
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)


driver.quit()