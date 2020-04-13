import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class filters:
    def __init__(self, driver):
        self.driver = driver
        collapseList = '//*[@id="filters-collapse-1"]'
        print("Initializing filters object")

    def clickFilter(self, filterName):
        print("Looking for filter: " + filterName.lower() + ".")
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="filters-collapse-1"]/div[1]')))
        filterList = self.driver.find_elements(By.XPATH, '//*[@id="filters-collapse-1"]//li//a')
        # //*[@id="filters-collapse-1"]/div[1]/ul/li[3]/h4/a[1]/i
        self.index = 1
        for f in filterList:
            if(filterName.lower() == str(f.text).lower()):
                print(self.index)
                print("Filter \"" + filterName + "\" located")
                self.filter = f
                self.filter.click()
                return
            if(str(f.text).strip().lower() != "clear" and str(f.text).strip() != ""):
                self.index = self.index+1
        print("Filter not located")
        return    
        

    def filtersSearchText(self, filterBy):
        print("searching filter section by text: " + filterBy)
        xpathString = '//*[@id="collapseinside' + str(self.index) + '"]/form/div/input'
        self.filterInput = self.driver.find_element(By.XPATH, xpathString)
        self.filterInput.send_keys(filterBy)
        self.filterInput.send_keys(Keys.RETURN)
        time.sleep(5)
        # //*[@id="lot_model_descSKYLINE"]

    def clickFilterCheckbox(self, checkboxValue):
        print("click on " + checkboxValue)

    def getAllFilterCheckboxes(self, checkboxValue):
        listOfChecboxValues = self.driver.find_element(By.XPATH, '//*[@id="collapsinside' + checkboxValue + ']')
        return listOfChecboxValues
