from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Firefox()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))

elem= driver.find_element(By.XPATH,'//button[text()="Try it"]')
elem.click()

alert= driver.switch_to.alert
time.sleep(5)
print(alert.text)

alert.accept()

# alert.dismiss()


