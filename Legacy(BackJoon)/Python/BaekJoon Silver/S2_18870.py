import sys
ip = sys.stdin.readline

n = int(ip())
temp = list(map(int, ip().split()))

xs = [[temp[i], i] for i in range(n)]
xs.sort()

i = 0
level = 0

while i < n:
    same_range = i+1
    for j in range(i+1, n):
        if xs[i][0] == xs[j][0]:
            same_range += 1
        else:
            break
    for changed in range(i, same_range):
        xs[changed][0] = level

    i = same_range
    level += 1

xs.sort(key=lambda x:x[1])

for i in range(n):
    print(xs[i][0], end=" ")

''' 좌표 압축
시간 2초 메모리 512MB

수직선 상에 N개의 좌표 x1,x2,x3,...,xn이 있다. 이걸 압축할거다.
xi를 압축한 x'i의 값은 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야한다?
압축해봐라

- 입력 -
첫 줄에 N
둘째 줄부터 x들

--2트--: 정답
정렬이 당연히 더 빠른 방법이라는 사실을 알면서 왜 그런 무의미한 짓으로 시간을 낭비하셨나요?

--1트--: ㅋㅋ 얌전히 정렬해
문제를 못알아듣게 내는게 트랜드인가

x1 = 2
x2 = 4
x3 = -10
x4 = 4
x5 = -9

일 때
x'1은 2
x'2는 3
x'3은 0
x'4는 3
x'5는 1

그니까 그냥 배열 안에서 나보다 큰 작은게 몇 개인지 새라는거 아냐;; 말을 어렵게 해;;
이거 그냥 태그 붙혀줘서 내림차순 정렬한 다음에 개수 새고 다시 태그순으로 정렬해서 결과 뽑으면 되는거잖아.

더 똑똑한 방법을 써볼까요?
1. 최솟값만큼 전부 빼고 i를 더해준다.
2. 가장 작은거 비활성화하고 반복
3. 언제까지? 전부 비활성화될 때 까지
근데 이거 반복 오지는데 생각보다 시간 안많아서 시간 걸릴수도 ㅋㅋ
걸리면 정렬하는 방법으로 해

'''