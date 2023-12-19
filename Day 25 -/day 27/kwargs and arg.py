def sum(*args):
    n = 0
    for arg in args:
        n += arg
    return n
print(sum(9,8,7,6,5,4))
#kwargs type is a dict
def calculate(**kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
    # or print(kwargs['add'])

class Car:
    def __init__(self, **kwargs):
        self.make = kw["make"]
        self.model = kwargs.get("model")
        # if no model was given to class and it is called,
        # it would say none

my_car = Car()