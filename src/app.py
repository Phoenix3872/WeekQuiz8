def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def multiply(self, a, b):
    return a * b

def divide(self, a, b):
   if b == 0:
        raise ValueError("Division by zero")
    return a / b

def log(self, x):
    if x <= 0:
        raise ValueError("Log undefined for zero or negative values")
    return math.log(x)

def square(self, x):
    return x * x

def sin(self, x):
    return math.sin(x)

def cos(self, x):
    return math.cos(x)

def sqrt(self, x):
    if x < 0:
        raise ValueError("Square root undefined for negative values")
    return math.sqrt(x)

def percentage(self, a, b):
    return (a / 100) * b
