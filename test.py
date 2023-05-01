from collections import deque
import sys
ip = sys.stdin.readline

a = deque([1,2,3,4])
print(",".join(list(map(str,a))))