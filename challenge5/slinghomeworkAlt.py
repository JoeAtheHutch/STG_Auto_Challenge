import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from common.TopNavSearch import topNavSearch
from collections import Counter
from common.CountList import countList

class challenge2(unittest.TestCase):

    def setUp(self):
        print("Running SetUp Method")
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.sling.com")

    def tearDown(self):
        print("Tearing Down")
        self.driver.close()

    def test_slingForAltTags(self):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, '//body/*')
        ))
        elements = self.driver.find_elements(By.XPATH, "//*")
        print(len(elements))
        tags = []
        for e in elements:
            print(e.tag_name)
            tags.append(e.tag_name)
        # if("img" || "svg")
        #     is there an alt tag?
        #         imgAltCount =+ 1
        #         print(e.get_attribute("alt"))
        
        
        

if __name__ == '__main__':
    unittest.main()