def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devision(x,y):
    if y==0:
        raise ValueError('can not divide by zero')
    return x/y
print(add(3,7))