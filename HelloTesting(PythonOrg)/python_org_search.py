from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.python.org/about")
assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem= driver.find_element(By.ID, "site-map")

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No Result Found" not in driver.page_source
time.sleep(5)
driver.forward()
time.sleep(5)
driver.back()