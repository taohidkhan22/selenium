from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class element_has_css_class(object):
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class= css_class
    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False
        

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

try:
    driver.find_element(By.XPATH, "//div[@id='start']/button").click()

    # Wait until the element becomes visible
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

    print("Element has the desired CSS class!")

finally:
    driver.quit()

