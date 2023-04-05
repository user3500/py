#Decorator

def my_decorator(func):
    def my_wrapper():
        print("Before")
        func()
        print("After")
    return my_wrapper

@my_decorator
def hello():
    print("Hellllo")

hello()
