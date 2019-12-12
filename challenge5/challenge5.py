import unittest
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
        searchField.send_keys("exotic")
        changeCount = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select').click()
        self.driver.implicitly_wait(5000)

        
        

if __name__ == '__main__':
    unittest.main()


