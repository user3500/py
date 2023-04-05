from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1}")
        #return results
    return wrapper

@performance
def hello():
    print("Hello!")
hello()
