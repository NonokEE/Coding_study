import sys
ip = sys.stdin.readline

###
def push(stack: list, e):
    stack.append(e)

def pop(stack: list):
    if stack:
        return stack.pop()
    else:
        return False

def top(stack: list):
    if stack:
        return stack[len(stack)-1]
    else:
        return False
###
line = ip()
while line != ".\n":
    stack = []
    flag = True
    for c in line:
        
        if   c == "(": push(stack, "(")
        elif c == "[": push(stack, "[")

        elif c == ")":
            if    top(stack) == "(": pop(stack)
            else: flag = False
        elif c == "]":
            if    top(stack) == "[": pop(stack)
            else: flag = False

    if stack: print("no")
    elif not flag: print("no")
    else: print("yes")

    line = ip()

''' 균형잡힌 세상

문자열이 주어졌을 때, 괄호의 균형이 맞는지 판단해야한다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

그래야 세상의 균형이 맞을거아냐

! 각줄은 무조건 .으로 끝난다.
!! 온점 단 하나만 들어오면 프로그램 종료.

--1트-- : 성공
이거 컴파일러 할 떄 배웠던 거 같은데
일단 여는게 무조건 먼저인거지?

스택으로 해결했던 거같음
'''