import time
from collections import deque
n = 10000
print("n = %d"%n)
# +
s = time.time()
a = []
for i in range(n):
    temp = []
    for j in range(n):
        temp += [0]
    a.append(temp)
e = time.time()
print("temp += [0]: %f"%(e-s))

# append
s = time.time()
a = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    a.append(temp)
e = time.time()
print("append(list): %f"%(e-s))

# deque append
s = time.time()
a = deque([])
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    a.append(temp)
e = time.time()
print("append(deque): %f"%(e-s))

# for for
s = time.time()
a = [[0 for _ in range(n)] for _ in range(n)]
e = time.time()
print("for for: %f"%(e-s))

# * for
s = time.time()
a = [[0]*n for _ in range(n)]
e = time.time()
print(" *  for: %f"%(e-s))
