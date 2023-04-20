import sys
ip = sys.stdin.readline

m, n = map(int, ip().split())

for i in range(m, n+1):
    if i == 1: continue
    for j in range(2, int(i**(1/2)+1)):
        if i%j == 0: break
    else         : print(i)

''' 소수 구하기
M이상 N이하의 모든 소수를 출력하세요

--1트-- : 시간초과
에라토스테네스의 체? 이름이 맞나?
암튼 그거를 스마~트하게 구현해야 합니다.
이게 아마 범위 끝의 루트까지만 찾아봐도 됐던거 같음.

--2트--:
채를 왜 직접 만들어줘 너무 비효율적으로 했어
'''