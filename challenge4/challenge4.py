import unittest
from fibonacci import Fibonacci
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class challenge2(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()

    def test_challenge4(self):
        print(self.fib.getFibOrder(6))

        

if __name__ == '__main__':
    unittest.main()


