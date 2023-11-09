import sys
ip = sys.stdin.readline

n, m = map(int, ip().split())
nums = list(map(int, ip().split()))
prefix_sum = [0 for _ in range(n+1)]    #prefix_sum[i] = sum(nums[0:i])

for i in range(n):
    prefix_sum[i+1] = nums[i] + prefix_sum[i]

for _ in range(m):
    i, j = map(int, ip().split())
    i -= 1

    print(prefix_sum[j] - prefix_sum[i])
    


''' 구간 합 구하기 4
시간 1초 메모리 256MB

수가 N개 주어졌을 떄, i번째 수부터 j번째 수 까지 합을 구하세요..?

- 입력 -
첫 줄에 숫자갯수 n과 합을 구해야하는 횟수 M을 준다
둘 째 줄에 n개의 수를 준다. (1000 이하의 자연수)
셋째줄 부터 범위 i와 j

--2트--: 잘~ 배웠습니다~
평범한 문제는 아닐거라고 생각하긴 했습니다
무식하게 짤거면 누가 못해

누적합과 구간합이라는 개념이 있습니다
누적합:
i번째 원소 = sum(0:i+1)

이걸 먼저 맹글어놓고,
누적합[i] - 누적합[j]를 하면 (i>j)
j+1 부터 i까지 더한 값이 됨

0 1 2 3 4 5
0 1 2 3

참고로 파이썬에 누적합 라이브러리가 있다고 합니다
accumulate

--1트--: 시간초과
뭐야 이게
'''