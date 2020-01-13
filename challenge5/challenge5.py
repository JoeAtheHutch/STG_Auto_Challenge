import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from common.TopNavSearch import topNavSearch

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        searchBar = topNavSearch(self.driver)
        searchBar.runSearch("ford")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')))
        resultNumber = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')
        Select(resultNumber).select_by_visible_text('100')
        time.sleep(5)

        
        
        
        

if __name__ == '__main__':
    unittest.main()