from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class topNavSearch:
    def __init__(self, driver):
        self.driver = driver


    def runSearch(searchString):
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.send_keys(searchString)
        searchButton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        searchButton.click()
