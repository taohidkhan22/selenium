from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
elem=driver.find_element(By.XPATH,'//button[text()="Click for JS Alert"]')
elem.click()