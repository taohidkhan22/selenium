import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class PythonOrgNavigationDownloadPage(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox()

    def test_download_navigation(self):
        driver=self.driver
        driver.get("http://www.python.org")
        elem=driver.find_element(By.LINK_TEXT,"Downloads")
        elem.click()

sleep(10)

# Combining the search and download navigation test class into one 

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox()
    def test_search_org(self):
        driver=self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        elem= driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("$")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("NO RESULT FOUND FOR KEYS.", driver.page_source)
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        
        
if __name__ == "__main__":
    unittest.main()
