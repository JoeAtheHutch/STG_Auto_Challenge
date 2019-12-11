class Fibonacci:
    
    #I don't think there is any value to this method, but I feel better having a constructor. Old Java habits
    def fibonacci(self):
        n1=0
        n2=1
    
    def getFibOrder(self, order):
        if order <= 1:
            return order
        else:
            return(self.getFibOrder(order - 1) + self.getFibOrder(order - 2))
    