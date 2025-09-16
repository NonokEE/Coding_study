## G3 2473 세 용액
import sys
ip = sys.stdin.readline

## 입력
N = int(ip())
solutions = list(map(int, ip().split()))

## 퀵 소트
sys.setrecursionlimit(10000)
def quick_sort(l: list):
    if not l: return []

    left = []
    right = []
    pivot = l[0]

    for i in range(1, len(l)):
        if l[i] < pivot: left.append(l[i])
        else              : right.append(l[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

solutions = quick_sort(solutions)

## 투포인터 시작
def mix(i, j, k): return solutions[i] + solutions[j] + solutions[k]

minimum = sys.maxsize
combination = []

for fix in range(N):
    left = 0
    right = N-1

    while(left < right):
        if left == fix: 
            left += 1
            continue
        if right == fix: 
            right -= 1
            continue

        mixed = mix(fix, left, right)
        if abs(mixed) < abs(minimum):
            minimum = mixed
            combination = [solutions[fix], solutions[left], solutions[right]]

        if   mixed > 0 : right -= 1
        elif mixed < 0 : left += 1
        elif mixed == 0: break
        
    if minimum == 0: break

## 출력
combination = quick_sort(combination)
print(*combination)
