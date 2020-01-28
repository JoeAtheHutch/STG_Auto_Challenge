import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.headerSearch import headerSearch
from common.screenshot import screenshot
from common.searchResults import searchResults
from common.filters import filters

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")
        print("Dun gettin' setup yo'")

    def tearDown(self):
        # self.driver.close()
        print("All torn down 'n' stuff")


    def test_challenge6(self):
        hs = headerSearch(self.driver)
        hs.searchFor("Nissan")
        f = filters()
        f.clickFilter("")
        s = screenshot()
        s.takeScreenshot("Skyline")
        sr = searchResults()
        sr.changeDropDown("100")
        # create this challenge here.
        # search for a make
        # Select a list of models within that make
        # Attempt Select and invalid model and when it fails get a screen shot
        # Create a class that goes through each of the filter options
        # try:
        #     filterName = "Nissan"
        #     modelValue = "Altima SR"
        #     # runheadersearch
        #     elements = self.driver.findElements("//*[@id='filters-collapse-1']//li//a/text()")
        #     count = 3
        #     for e in elements:
        #         if(e.text == filterName):
        #             e.click
        #     txtelement = self.driver.find_element("//*[@id='collapseinside" + str(count) + "']/form/div/input")
        #     txtelement.send_keys(modelValue)
        #     checkElement = self.driver.find_element("//*[@id='collapseinside4" + str(count) + "']//abbr[@value='" + modelValue + "']")
        #     checkElement.click()
             
        # except:
        #     print("Error, Will Robinson, Error")
        #     print("An Error occured")
        #     print("You wanted " + modelValue)
        #     print("These are the available checkboxes: ")
        #     # something like:
        #     checkboxElements = self.driver.find_elements(By.XPATH, "//*[@id='collapseinside4']//input[@type='checkbox']")
        #     for e in checkboxElements:
        #         e.get_attribute('value')


if __name__ == '__main__':
    unittest.main()


