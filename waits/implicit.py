from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# driver.find_element(By.XPATH,'//button[text()="Start"]').click()
# start_button = driver.find_element(By.TAG_NAME, "button")
start_button = driver.find_element(By.CSS_SELECTOR, "button")
start_button.click()