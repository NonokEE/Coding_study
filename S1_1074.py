import sys
ip = sys.stdin.readline

N, r, c = map(int, ip().split())

# init
res = 0
length = 2**N
size = length**2

while size > 1:
    # 사분면 찾기
    if r < length/2: # 0,1사분면
        if c < length/2: quadrant = 0
        else           : quadrant = 1
    else:            # 2,3사분면
        if c < length/2: quadrant = 2
        else           : quadrant = 3

    res += (size/4) * quadrant

    # 축소
    size /= 4
    length /= 2
    match quadrant:
        case 1: c -= length
        case 2: r -= length
        case 3:
            c -= length
            r -= length

print(int(res))

''' Z
크기가 2^N * 2^N인 2차원 정사각형 배열이 있다. (변 길이가 무조건 2의 제곱수인 정사각형 배열)
이걸 Z 스텝으로 탐색하고자 한다.
제일 작은 Z를 그려서 커져나가는 방식. 프랙탈을 생각하면 된다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는가?
!! r행 c열 이거도 0부터 시작하는듯.

--1트-- : ezpz
수학?

0   1   2   3
4   5   6   7
8   9  10  11
12 13  14  15

0. 결과는 0부터 시작
1. 제일 끝 숫자는 당연히 사각형의 크기, size를 기록.
2. 제일 큰 사각형부터 시작해서 4등분한다. 
    좌상 = 0사분면
    우상 = 1사분면
    좌하 = 2사분면
    우하 = 3사분면
   이라고 하자. 찾고자 하는 위치가 몇 사분면인지 찾는다.
   -> 변의 길이/2보다 작은지 큰지로 판별 가능.
3. [(size/4) * N사분면]을 결과에 더해준다.
    ex) 크기가 16일 때, 0사분면이라면 0, 1사분면이라면 4, 3사분면이라면 12
        즉, 각 사분면의 가장 좌상값.
4. 사분면으로 좁혀들어간다.
    1) size = size/4
    2) length = length/2
    3) 찾을 좌표
        0사분면 <- 변화X
        1사분면 <- 열 = 열 - 절반이 된 length (*위에서 이미 절반 해놨기 때문에 그냥 빼면 됨.)
        2사분면 <- 행 = 행 - 절반이 된 length
        3사분면 <- 1사분면과 2사분면 둘 다 해줌.
    !) 좁아진 사분면의 첫 숫자는 0이다.
5. 이 과정을 size가 0이 될 때 까지 한다.

이렇게 하면 그냥 무난~하게 재귀적으로 해결할 수 있을 듯.
시간 걸리려나...
'''