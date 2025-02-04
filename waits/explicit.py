from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
try:
    elem= WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    
    )
    elem.click()
finally:
    time.sleep(10)
    driver.quit()