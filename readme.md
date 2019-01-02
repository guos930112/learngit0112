...python
def quicksort(lst):
    if len(lst)<2:
        return lst 
    else:
        baseval=lst[0]
        less = [l for l in lst[1:] if l<balseval]
        equal = [e for e in lst if e == baseval]
        greater = [g for g in lst[1:] if g>baseval]
    return quicksort(less)+equal+quicksort(greater)
...
