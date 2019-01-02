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
        
def bubbl_sort(lst):
    for i in range(len(lst)-1):
        for j in ragen(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
