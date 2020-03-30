from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class filters:
    def __init__(self, driver):
        self.driver = driver
        collapseList = '//*[@id="filters-collapse-1"]'
        print("Filters Dun ben initialized yo'")

    def clickFilter(self, filterName):
        if(filterName == "Model"):
            
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="filters-collapse-1"]/div[1]/ul/li[3]/h4/a[1]')))
            modelField = self.driver.find_element(By.XPATH, '//*[@id="filters-collapse-1"]/div[1]/ul/li[3]/h4/a[1]')
            # //*[@id="filters-collapse-1"]/div[1]/ul/li[3]/h4/a[1]
            modelField.click()
        print("All about clickin them filters: " + filterName)

    def filtersSearchText(self, filterBy):
        print("searching filter section by text: " + filterBy)

    def clickFilterCheckbox(self, checkboxValue):
        print("click on " + checkboxValue)

    def getAllFilterCheckboxes(self, checkboxValue):
        listOfChecboxValues = self.driver.find_element(By.XPATH, '//*[@id="collapsinside' + checkboxValue + ']')
        return listOfChecboxValues
