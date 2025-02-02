from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver = webdriver.Firefox()
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
