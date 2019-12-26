import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# TODO: Pull up a list of image URLS with alt_text for the blue/orange/orange and blue offering form Sling landing page.
    
class bonusSlingImage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()
    
    def test_bonusSlingImage(self):
        self.driver.get("https://sling.com")
        planList = self.driver.find_elements(By.XPATH, '//*[@id="hp_pcgrid"]/div//*[contains(@id,"plan")]')        
        for plan in planList:
            plan.click()
            time.sleep(0.5)
            channelList = self.driver.find_elements(By.XPATH, '//*[@id="channelList"]//img')
            print("\n" + str(plan.get_attribute("id")) + ":")
            for i in channelList:
                print(str(i.get_attribute("title")) + " - " + str(i.get_attribute("alt")))


if __name__ == '__main__':
    unittest.main()
