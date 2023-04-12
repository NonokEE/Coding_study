import sys
ip = sys.stdin.readline

K = int(ip())
stack = []

for _ in range(K):
    num = int(ip())
    if num == 0: stack.pop()
    else       : stack.append(num)

print(sum(stack))

''' 제로
그냥 숫자 다 저장하다가 0 나오면 pop 하는 스택문제

--1트-- : 이걸 틀릴리가 있나
그냥 스택이요
'''