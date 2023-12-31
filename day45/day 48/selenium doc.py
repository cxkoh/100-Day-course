'''from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
url ='https://www.python.org'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

'''price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"{price_dollar}.{price_cents}")'''

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(link.text)

#xpath, right click html and copy Xpath
bug_link = driver.find_element(By.XPATH, value='//......')
print(bug_link.text)

driver.find_element(By.)


#driver.close()
driver.quit()'''