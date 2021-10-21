def logger(func):
    def inner(*a,**b):
        return func(*a,**b)
    return inner

def logger2(func):
    def inner(*a,**b):
        print('a1')
        return func(*a,**b)
    return inner
@logger2
@logger
def diz():
    print("ola 2")
    print("123")
    print("abcaas")



diz()
