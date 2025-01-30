import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()
driver.get("https://www.facebook.com/signup")
# elem =driver.find_element(By.XPATH, "//select[@name='birthday_year']" )
elem= driver.find_element(By.ID,"year")
allOptions = elem.find_elements(By.TAG_NAME, "option")
for option in allOptions:
    print("Value is:" , option.get_attribute("value"))
    option.click()
    if option.get_attribute("value") == "2020":
        break 
