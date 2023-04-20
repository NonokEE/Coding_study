import sys
ip = sys.stdin.readline

n = int(ip())
len_s = int(ip())
s = list(" ".join((ip().strip())).split())

for i in range(len_s):
    if s[i] == 'I': s[i] = 1
    else          : s[i] = 0

def automata(listinput:list, n: int):
    chk = 1
    for i in range(2*n + 1):
        if listinput[i] != chk:
            break
        chk = 1 - chk
    else:
        return True
    return False

count = 0
for i in range(len_s - 2*n - 1):
    if s[i] == 1:
        if automata(s[i: i + (2*n) +1], n): count += 1

print(count)

''' IOIOI

P1 = IOI
P2 = IOIOI
P3 = IOIOIOI
입니다.

문자열 S와 정수 N을 줄거니까 S 안에 PN이 몇개 들어가는지 세세요.
P1인데 IOIOI면 2개 들어간거임.

- 입력 -
첫줄에 N, 둘째줄에 S길이, 셋째줄에 S

--1트--: 왜 틀려
오토마타로 구현하면 문제는 간단함. 

1. IOI오토마타 만든다
2. 문자열 순회하면서 I면 오토마타에 넣는다.
3. 끗

PN의 길이는 2N+1이므로, S의 끝에서 2N+1 이후 부터는 순회할 필요 없다.
len_s - n 까지만 루프.

0123456
1010101 7
101 3

'''