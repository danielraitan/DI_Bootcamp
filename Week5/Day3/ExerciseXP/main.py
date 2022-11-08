# 1#
# number = 10

# abs_number = abs(number)
# print(abs_number)

# print( int("10"))

# print('Enter your name:')
# name = input()
# print('Hello, ' + name)

# def hello():
#     print("hello there")
# hello().__doc__

# 2#
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return str(self.currency)
        
    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return repr(self.currency)

    def __repr__(self):
        return repr(self.amount)

    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

