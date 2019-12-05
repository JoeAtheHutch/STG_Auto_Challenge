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
        searchButton = self.driver.find_element_by_xpath("//*[@id='search-form']/div/div[2]/button")
        searchField = self.driver.find_element_by_id("input-search")

        self.assertIn("Copart", self.driver.title)
        searchField.send_keys("exotic")
        searchButton.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="collapseinside3"]')))
        makeField = self.driver.find_element_by_xpath('//*[@id="collapseinside3"]').text
        self.assertIn("Porsche", makeField)


if __name__ == '__main__':
    unittest.main()


