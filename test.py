import sys
ip = sys.stdin.readline

def quicksort(l):
    if len(l) <= 1: return l
    pivot = l[len(l)//2]
    lt, gt = [], []
    for item in l:
        if   item < pivot: lt.append(item)
        elif item > pivot: gt.append(item)
    return quicksort(lt) + [pivot] + quicksort(gt)

a = ['ac', 'dc', 'fb', 'a']
quicksort(a)
print(a)