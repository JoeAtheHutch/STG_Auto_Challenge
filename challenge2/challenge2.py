import unittest
from selenium import webdriver

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        searchButton = self.driver.find_element_by_xpath("//*[@id='search-form']/div/div[2]/button")
        searchField = self.driver.find_element_by_id("input-search")

        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.search.send_keys("exotic")
        self.searchButton.click()


if __name__ == '__main__':
    unittest.main()


