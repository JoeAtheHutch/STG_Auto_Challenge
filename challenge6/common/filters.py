from selenium import webdriver
from selenium.webdriver.common.by import By

class filters:
    def __init__(self, driver):
        self.driver = driver
        print("Dun ben initialized yo'")

    def clickFilter(self, filterName):
        print("All about clickin them filters: " + filterName)

    def filtersSearchText(self, filterBy):
        print("searching filter section by text: " + filterBy)

    def clickFilterCheckbox(self, checkboxValue):
        print("click on " + checkboxValue)

    def getAllFilterCheckboxes(self, checkboxValue):
        listOfChecboxValues = self.driver.find_element(By.XPATH, '//*[@id="collapsinside' + checkboxValue + ']')
        return listOfChecboxValues
