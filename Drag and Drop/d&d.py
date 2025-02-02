from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from time import sleep
driver = webdriver.Firefox()
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

source= driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

action_chain = ActionChains(driver)
time.sleep(10)
action_chain.drag_and_drop(source, target).perform()
