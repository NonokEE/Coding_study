import time
n = 50000

#2.6359684467315674
s1 = time.time()
a = [[0 for _ in range(n)] for _ in range(n)]
e1 = time.time()
print(e1-s1)

# 0.9696991443634033
s2 = time.time()
a = [[0]*n for _ in range(n)]
e2 = time.time()
print(e2-s2)

print((e1-s1)/(e2-s2))