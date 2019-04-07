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

import time
import _thread

def gen_decorator(f):
    def wrapper(*args,**kwargs):
        gen_f = f()
        r = next(gen_f)
        def fun(g):
            ret = next(g)
            try:
                gen_f.send(ret)
            except StopIteration
                pass
        _thread.start_new_thread(fun,(r,))
    return wrapper

def long_io():
    print('开始执行io操作了')
    time.sleep(5)
    print('io操作执行完成')

def select_sort(lst):
    for i in range(len(lst)-1):
        index = i
        for j in range(i+1,len(lst)):
            if lst[index] > lst[j]:
                index = j
        lst[i],lst[index] = lst[index],lst[j]
    return lst

# insert sort:
def insert_sort(lst):
    for j in range(1,len(lst)-1):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key
    return lst

def req_a():
    print('请求a开始执行')
    import time
    time.sleep(2)
    print('请求a执行完成')

