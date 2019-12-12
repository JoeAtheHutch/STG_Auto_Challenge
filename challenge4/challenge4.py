import unittest
from fibonacci import Fibonacci
from convertNumberToString import ConvertNumberToString

class challenge2(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()
        self.numToString = ConvertNumberToString()

    def test_challenge4(self):
        self.fib.getFibOrder(1)
        self.fib.getFibOrder(10)

    def test_numToString(self):
        self.numToString.getNumberString(12034200)
        self.numToString.getNumberString(0)

    def test_fibString(self):
        fibValues = [0, 1, 10, 12, 30]
        for value in fibValues:
            print(self.get_fibString(value))

    def get_fibString(self, fibValue):
        theNum = self.fib.getFibOrder(fibValue)  
        return str(theNum) + ' - ' + self.numToString.getNumberString(theNum)

        

if __name__ == '__main__':
    unittest.main()


