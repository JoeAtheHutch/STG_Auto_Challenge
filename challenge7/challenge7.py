import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.navigateTo import navigateTo

class challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        elements = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]//a')
        ng = navigateTo(self.driver)
        for count in elements:
            if ng.goTo(count.get_attribute("href"),count.text):
                pass
            else:
                # take screenShot
            print(make.text + " - " + make.get_attribute("href"))

        

if __name__ == '__main__':
    unittest.main()


