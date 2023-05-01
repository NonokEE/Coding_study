import sys
ip = sys.stdin.readline

n, m = map(int, ip().split())
nums = list(map(int, ip().split()))

for _ in range(m):
    i, j = map(int, ip().split())
    i -= 1
    print(sum(nums[i:j]))


''' 구간 합 구하기 4
시간 1초 메모리 256MB

수가 N개 주어졌을 떄, i번째 수부터 j번째 수 까지 합을 구하세요..?

- 입력 -
첫 줄에 숫자갯수 n과 합을 구해야하는 횟수 M을 준다
둘 째 줄에 n개의 수를 준다. (1000 이하의 자연수)
셋째줄 부터 범위 i와 j

--1트--: 시간초과
뭐야 이게
'''