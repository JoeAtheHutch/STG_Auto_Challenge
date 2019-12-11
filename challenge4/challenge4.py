import unittest
from fibonacci import Fibonacci
from selenium import webdriver
from convertNumberToString import ConvertNumberToString
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge2(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()
        self.numToString = ConvertNumberToString()

    def test_challenge4(self):
         print(self.fib.getFibOrder(1))

    def test_numToString(self):
        print(self.numToString.getNumberString(12034200))
        print(self.numToString.getNumberString(0))

        

if __name__ == '__main__':
    unittest.main()


