import sys
ip = sys.stdin.readline

str1 = ip().strip()
str2 = ip().strip()
dp = [0 for _ in range(len(str2))]

for i in range(len(str1)):
    count = 0
    for j in range(len(str2)):
        if count < dp[j]:
            count = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = count+1

print(max(dp))

''' LCS
시간 2초 메모리 256MB

두 문자열. 최장 부분수열 구하셈

- 입력 -
각 줄에 문자열 하나씩. 총 2개. 전부 대문자고 최대 1000글자
둘이 길이 같다고 한 적 없음.

- 출력-
LCS 길이

--1트--: 답지
가장 긴 뭐시기를 응용할 수 있을 것 같은데 여긴 문자열이 2개란 말이지?

'''