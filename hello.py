def func():
    print("hello world")

def fib(count):
    a = 0
    b = 1
    n = 0
    while n < count:
        yield a
        a ,b = b ,a+b
        n += 1


