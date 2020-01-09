import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.send_keys("porsche")
        searchButton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        searchButton.click()
        
        
        

if __name__ == '__main__':
    unittest.main()


