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
from common.DamageSwitch import damageSwitch

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        searchBar = topNavSearch(self.driver)
        searchBar.runSearch("porsche")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')))
        resultNumber = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')
        Select(resultNumber).select_by_visible_text('100')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[50]//span')))
        models = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr/td[6]/span')
        modelCount = countList(models)
        countedList = modelCount.getCounts()
        for model in countedList:
            print(model + " - " + str(countedList[model]))
        print("****end model counts****")
        
    def test_damages(self):
        damageTypes = {"REAR END":0, "FRONT END":0, "MINOR DENT/SCRATCHES":0, "UNDERCARRIAGE":0, "MISC.":0}
        searchBar = topNavSearch(self.driver)
        searchBar.runSearch("porsche")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')))
        resultNumber = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_length"]/label/select')
        Select(resultNumber).select_by_visible_text('100')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[50]//span')))
        damages = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr/td[12]/span')
        whichType = damageSwitch()
        for d in damages:
            thisCar = whichType.switch(d.text)
            damageTypes[thisCar] += 1
        for i in damageTypes:
            print(i + " - " + str(damageTypes[i]))
        print("****end damage counts****")
        
            
            
        
        
        
        
        

if __name__ == '__main__':
    unittest.main()