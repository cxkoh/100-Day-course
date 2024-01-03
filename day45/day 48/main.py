from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
url ='https://www.python.org'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
events={}
event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n],
        "name": event_name[n],
    }
print(events)
driver.quit()