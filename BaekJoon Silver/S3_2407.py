import sys
ip = sys.stdin.readline

n, m = map(int, ip().split())
if m >= (n//2): m = n-m

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n)//(factorial(n-m)*factorial(m)))

''' 조합
시간 2초 메모리 128MB

nCm을 출력하세요

- 입력 -
n, m
둘 다 5이상 100이하, n >= m

- 출력-
nCm

--1트--: 결과
수학 문젠디 nCm이 뭔지 까먹음

n! 
ㅡ
m! * (n-m)!

이긴 한디
n 부터 1씩 빼면서 r개 / r! 임

nCm = nC(n-m) 이라서 개수 줄여주는게 좋다.

근데 이게 시간 걸릴 것 같진 않은데


'''