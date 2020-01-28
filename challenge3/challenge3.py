import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        popularList = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]//a')
        for make in popularList:
            print(make.text + " - " + make.get_attribute("href"))


    def test_challenge3whileLoop(self):
        self.driver.get("https://www.copart.com")
        categoryList = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[3]//a')
        self.assertIn("Copart", self.driver.title)
        loopIndex=0
        while(loopIndex < len(categoryList)):
            print(categoryList[loopIndex].text + " - " + categoryList[loopIndex].get_attribute("href"))
            loopIndex=loopIndex+1

        

if __name__ == '__main__':
    unittest.main()


