from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/signup")
# elem= driver.find_element(By.ID,"day")
# -- Day selct ---
elem =driver.find_element(By.XPATH, "//select[@id='day']")
alloption= elem.find_elements(By.TAG_NAME,"option")
for option in alloption:
    print("value is: ",option.get_attribute("value"))
    option.click()

