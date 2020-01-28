from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class headerSearch:
    def __init__(self, driver):
        self.driver = driver
        print("initializing Header Search")

    def searchFor(self, query):
        print("Search for: " + query)
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.send_keys(query)
        searchButton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        searchButton.click()
        dataElement = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideTable"]//tbody')) )
        tableData = self.driver.find_element(By.XPATH, '//*[@id="serverSideTable"]//tbody')
        visible = tableData.text
        print("Visible")