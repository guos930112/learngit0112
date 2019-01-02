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

def quick_sort(lst):
    if len(lst)<2:
        return lst
    else:
        baseval=lst[0]
        less=[l for l in lst[1:] if l<baseval]
        equal=[e for e in lst if e==baseval]
        greater=[g for g in lst[1:] if g>baseval]
    return quick_sort(less)+equal+quick_sort(greater)

