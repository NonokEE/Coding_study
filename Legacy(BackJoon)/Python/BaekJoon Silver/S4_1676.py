import sys
ip = sys.stdin.readline

N = int(ip())
num = 1
for i in range(2, N+1): num *= i

num = str(num)
zero = 0
for i in range(len(num)-1,0,-1):
    if num[i] == '0': zero +=1
    else: break

print(zero)

'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때 까지 0의 개수를 구해라고?
'''