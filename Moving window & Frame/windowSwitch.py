from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Firefox()
driver.get("https://www.facebook.com/signup")
print("Opened Goggle")

main_window= driver.current_window_handle

# driver.execute_script("window.open('https://www.bing.com','_blank');")

driver.execute_script("window.open('https://www.bing.com','_blank');")

windows= driver.window_handles
time.sleep(5)


# print("Switched to Bing: ", driver.title)
# time.sleep(5)
driver.switch_to.window(main_window)
print("Switched to goggle : ",driver.title)

for window in windows:
        time.sleep(5)
        driver.switch_to.window(window)
        