from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.google.co.uk/")
cookie ={'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)

# Optional
i= driver.get_cookies()
print("the cookies are: ",i)
