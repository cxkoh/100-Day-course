

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
url= "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Chee Xuan", Keys.ENTER)
first_name = driver.find_element(By.NAME, value="lName")
first_name.send_keys("Koh", Keys.ENTER)
first_name = driver.find_element(By.NAME, value="email")
first_name.send_keys("random@jdkd.com", Keys.ENTER)
drivers = driver.find_element(By.CSS_SELECTOR, value="form button")
drivers.click()