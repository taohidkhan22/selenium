from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Firefox()
driver.get("https://www.google.com/")

continue_link= driver.find_element(By.LINK_TEXT, 'সম্পর্কে')
continue_link.click()