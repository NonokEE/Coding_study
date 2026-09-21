## G2 1918 후위 표기식
import sys
ip = sys.stdin.readline

infix = ip().rstrip()
stack = [None]

operator = set(["+","-","*","/"])
priority = {"*": 1, "/": 1, "+": 0, "-":0, "(": -1, None: -2}


def get_top():
    return stack[len(stack)-1]

for letter in infix:
    if letter in operator:
        while(priority[get_top()] >= priority[letter]):
            top = stack.pop()
            if top != "(":
                print(top, end="")
        stack.append(letter)

    elif letter == "(":
        stack.append(letter)

    elif letter == ")":
        while(get_top() != "("):
            print(stack.pop(), end="")
        stack.pop()

    else:
        print(letter, end="")

while (get_top() != None):
    print(stack.pop(), end="")