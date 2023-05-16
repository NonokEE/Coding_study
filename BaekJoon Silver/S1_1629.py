import sys
ip = sys.stdin.readline

A, B, C = map(int, ip().split())

def power(a,b):
    if b == 1:
        return a%C
    else:
        temp = power(a, b//2)
        if b%2:
            return temp * temp * a % C
        else:
            return temp * temp % C

print(power(A, B))

''' 곱셈
시간 0.5초 메모리 128MB

자연수 A를 B번 거듭제곱할겁니다. 너무 클 수 있으니까 이걸 C로 나눈 나머지를 구하세요.

- 입력 -
첫 줄에 A B C. 전부 int 범위 내 자연수

- 출력-
(A^B)/C

--1트--: 결과
단순한 문제는 절대 아니고, 분할정복을 이용한 거듭제곱이라
나머지가 도나?

3 n 10 이라 하면

3 9 27 81 243 
3 9 7 1 3 9 7 1 

나머지라는게 결국 돌긴 할거임.

1. 나머지 안돌때까진 그냥 계산하면서 나머지 열에 넣는다
2. 돌기 시작하면 그때부터 직접적으로 연산 안하고, 나머지 개수랑 남은 연산 횟수로 계산

그리고
27 // 10 = 7이면
그 다음 수가 나머지라고 가정해도 상관 없음

A B C 전부 정수 최대 범위까지 가능하니까, 계산 잘못하면 폭발함.

'''