import sys
ip = sys.stdin.readline

n = int(ip())
numbers = []
for i in range(n): numbers.append(int(ip()))

print("---")
# 산술평균
ans = sum(numbers)/n

if (abs(ans*10) - abs(int(ans)*10)) >= 5: 
    if ans>0: ans += 1
    else    : ans -= 1
print(int(ans))

# 중앙값
numbers.sort()
print(numbers[int(n/2)])

# 최빈값
field = [0 for _ in range(8001)]    # [0번 필드 = -4000] ~ [4000번 필드 = 0] ~ [8000번 필드 = 4000] ::: v
for num in numbers: field[num + 4000] += 1

mode = max(field)
candidate = []

for i in range(8001):
    if mode == field[i]: candidate.append(i-4000)

if len(candidate) == 1: print(candidate[0])
else:
    candidate.sort()
    print(candidate[1])
    
# 범위
print(numbers[n-1] - numbers[0])

''' 통계학
홀수 N이 있을 때,

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

절대값이 4000을 넘지 않는 N개의 정수가 주어질 때,
산술평균(소수점 첫 자리에서 반올림)
중앙값
최빈값(여러 개 있을 때는 두번째로 작은 값)
범위
를 출력한다.

--1트-- : 어디서 틀린겨?
정렬을 기본정렬로 하면 항상 시간 터지던데, 일단 귀찮으니까 그냥 해보자 ㅎ..
혹시 시간 터지면 머지소트 구현해서 ㄱㄱ

그런데 말입니다? 범위가 +- 4000밖에 안되는데 그냥 필드를 만드는게 낫지 않을까요~?
일단은 가능한 무식한 방법으로 해보죠.
'''