from selenium import webdriver
from collections import Counter


class countList:
    def __init__(self, itemsList):
        self.items = itemsList
        self.listStr = []
        for item in itemsList:
            self.listStr.append(str(item.text))
        
        

    def getCounts(self):
        return Counter(self.listStr)