from collections import deque

def int_to_deque(e):
    e = deque(str(e))
    while len(e) < 4:
        e.appendleft('0')
    return e

def funcL(e):
    e = int_to_deque(e)
    e.append(e.popleft())
    return int("".join(e))

def funcR(e):
    e = int_to_deque(e)
    e.appendleft(e.pop())
    return int("".join(e))

print(funcL(1000))
print(funcR(234))