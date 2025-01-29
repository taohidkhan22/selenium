import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()
driver.get("https://www.facebook.com/signup")
# elem= driver.find_element(By.NAME,"q")
# elem= driver.find_element(By.ID,"APjFqb")
# elem.send_keys("some text", Keys.ARROW_LEFT)
# elem.cle
elem =driver.find_element(By.XPATH, "//select[@name='birthday_year']" )
# elem.send_keys("Cricbuzz")
# elem.send_keys(Keys.RETURN)