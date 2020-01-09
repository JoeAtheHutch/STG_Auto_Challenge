# TODO: Access the sling help center and perform a search (ROKU in the example). Verify that non-zero items returned in the search

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# TODO: Pull up a list of image URLS with alt_text for the blue/orange/orange and blue offering form Sling landing page.
    
class bonusSlingSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
    
    def test_bonusSlingSearch(self):
        self.driver.get("https://www.sling.com")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@href="https://help.sling.com"]')))
        helpCenter = self.driver.find_element(By.XPATH, '//*[@href="https://help.sling.com"]')
        # This is definitely cheating, just looking for the href.
        # I justified this to myself saying, "This test will fail if the link doesn't exist anyway"
        # And, "this will also be more stable than any other XPATH I found"
        # and finally, "I'm testing results after the click, not the link itself"

        helpCenter.click()
        resultTitle = "How do I install Sling TV on my Roku"
        searchBar = self.driver.find_element(By.XPATH, '//*[@id="support-search-input"]')
        searchButton = self.driver.find_element(By.XPATH, '//*[@id="hc-search-form"]/div[2]/button')
        searchBar.send_keys("ROKU")
        searchButton.click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul')))
        searchResults = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul').text
        self.assertIn(resultTitle, searchResults)

        

if __name__ == '__main__':
    unittest.main()
