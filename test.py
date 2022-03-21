import sys
ip = sys.stdin.readline

a = [[1,2,3], [4,5,6], [7,8,9]]
b = [a[i][:2] for i in range(2)]
print(b)