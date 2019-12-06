import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        popularMakes = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]/*')
        self.assertIn("Copart", self.driver.title)
        print(popularMakes)
        for make in popularMakes:
            print(make.text)
        print("This totally works")
        

if __name__ == '__main__':
    unittest.main()


