#Error Handling
def doub(num):
    for i in num:
        yield(i*i)

nu = doub([1,2,3,4,5])
while True:
    try:
        print(next(nu))
    except:
        continue
    finally:
        break
