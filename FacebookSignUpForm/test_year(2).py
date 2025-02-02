from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver= webdriver.Firefox()
driver.get("https://www.facebook.com/signup")

alloptions= elem.find_elements(By.TAG_NAME,"option")

for option in alloptions:
    option.click()


