from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from time import sleep
import unittest



class moveToRelease(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    def test_draganddropcheck(self):
        # driver = self.driver
        driver=webdriver.Firefox()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
        source= driver.find_element(By.ID, "draggable")
        target= driver.find_element(By.ID, "droppable")
        action_chains = ActionChains(driver)
        time.sleep(5)
        action_chains.click_and_hold(source).move_by_offset(50,60).release().perform()


if __name__ == "__main__":
    unittest.main()


