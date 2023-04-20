import sys
ip = sys.stdin.readline

n = int(ip())
image = [list(map(int, " ".join(ip().split()))) for _ in range(n)]

def pimage(image):
    for line in image:
        print(line)
    print()

def slicing(image, length):
    up = image[:length]
    down = image[length:]

    lup = []
    rup = []
    ldonw = []
    rdown = []
    for i in range(length):
        lup.append(up[i][:length])
        rup.append(up[i][length:])
        ldonw.append(down[i][:length])
        rdown.append(down[i][length:])

    return lup, rup, ldonw, rdown

def image_sum(image):
    res = 0
    for line in image:
        res += sum(line)
    return res

def comp(image:list, length):
    val = image_sum(image)
    max_size = length**2
    if   val == 0       : print("0", end="")
    elif val == max_size: print("1", end="")
    else                :
        print("(", end="")
        pieces = slicing(image, length//2)
        for piece in pieces: comp(piece, length//2)
        print(")", end="")

comp(image, n)

''' 쿼드트리
정사각형 이미지를 가로 중앙, 세로 중앙으로 사등분해서
좌상, 우상, 좌하, 우하 순으로 압축.
각 사분면이 모두 같으면 0 또는 1로 표현 가능.
다른게 섞여있으면 그 부분을 또 사등분해서 반복.
각 사분면은 한 괄호 안에 들어감.

-입력-
첫 줄에 이미지 크기 N(변의 길이)주어짐(무조건 2의 제곱수이고 1이상 64이하)
두번째 줄 부터 문자열 N개가 들어와서 이미지 표현. 

--1트-- : 어디서 틀린거야

1074랑 유사한 문제로 보인다. 이런걸 뭐라고 하더라? 파편화? ㄴㄴ 분할 정복
괄호로 표현해주는 거 보니까 재귀함수로 짜야될 것 같기도 하고?
재귀 안쓰는 방법이 생각이 안남. 재귀로 합니다.

! 놀라운 사실
numpy 안쓰면 2차원 배열 슬라이싱이 안된다! 슬라이싱 하기 전 부분까지 직접 찾아가서 해줘야한다!

! 놀라운 사실 2
numpy 안쓰면 2차원 배열 sum도 안된다!

--2트--:
아마 전부 0이거나 전부 1인 경우에 대해 예외처리가 안되어있는듯 하다.
순서를 좀 바꿔줘야될듯. 지금은 무작정 자르고나서 판단하는데, 판단하고 잘라야 맞다.

이전 로직은 맞는데, 길이가 1인 경우에 무조건 4개 다 출력하는게 아님
하나하나 출력할 때도 있고, 합쳐서 출력할 때도 있음

예외 1. 전부 같은 경우
예외 2. 아예 길이 1짜리인 경우

전부 같으면 괄호가 나오면 안됨
나눠야 하는 경우만 재귀하고 아닌 경우엔 재귀 할 필요 없잖아
그리고 아닌 경우에만 괄호가 출력되면 됨.

'''