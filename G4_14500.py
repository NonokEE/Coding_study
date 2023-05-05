import sys
ip = sys.stdin.readline

def Flatten(arr):
    res = []
    for line in arr: res += line
    return res

def Convolution(arr1, arr2):
    h1, w1 = len(arr1), len(arr1[0])
    h2, w2 = len(arr2), len(arr2[0])
    rh = h1 - h2 + 1
    rw = w1 - w2 + 1

    temp1 = Flatten(arr1)
    temp2 = Flatten(arr2)

    res = [[0 for _ in range(rw)] for _ in range(rh)]

    # 결과의 각 칸마다
    for i in range(rh):
        for j in range(rw):
            
            # 필터의 값
            for x in range(h2):
                for y in range(w2):
                    res[i][j] += (arr1[x+i][y+j] * arr2[x][y])

    return res

def max_2d(arr):
    res = 0
    for line in arr:
        res = max(max(line), res)
    return res

###
n, m = map(int, ip().split())
field = [list(map(int, ip().split())) for _ in range(n)]

b1 = [[1,1,1,1]]         # ㅡ
b2 = [[1],[1],[1],[1]]   # ㅣ
b3 = [[1,1],[1,1]]       # ㅁ

b4 = [[1,0],[1,0],[1,1]] # ㄴ
b5 = [[1,1,1],[1,0,0]]
b6 = [[1,1],[0,1],[0,1]]
b7 = [[0,0,1],[1,1,1]]

b8 = [[0,1],[0,1],[1,1]] # 반전 ㄴ
b9 = [[1,0,0],[1,1,1]]
b10 = [[1,1],[1,0],[1,0]]
b11 = [[1,1,1],[0,0,1]]

b12 = [[1,0],[1,1],[0,1]] # s
b13 = [[0,1,1],[1,1,0]]

b14 = [[0,1],[1,1],[1,0]] # 반전 s
b15 = [[1,1,0],[0,1,1]]

b16 = [[1,1,1],[0,1,0]] # ㅗ
b17 = [[0,1],[1,1],[0,1]]
b18 = [[0,1,0],[1,1,1]]
b19 = [[1,0],[1,1],[1,0]]

blocks = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]

res = []
for b in blocks:
    res.append(Convolution(field, b))

for i in range(19):
    res[i] = max_2d(res[i])

print(max(res))


''' 테트로미노
시간 2초 메모리 512MB

폴리노미오란?
- 정사각형은 서로 겹치면 안된다
- 도형은 모두 연결되어 있어야 한다.
- 정사각형의 변끼리 연결되어 있어야 한다.

정사각형 4개짜리가 테트로미노이고, 테트리스 블록들이다.

n*m 짜리 종이 위에 테트로미노 하나를 놓을거임.
종이의 각 칸 위에서는 정수가 하나씩 쓰여있다.
테트로미노 하나를 딱 놔서 걔가 먹은 칸들에 적혀있는 수의 합이 최대가 되도록 하라.
회전이나 대칭도 ㅇㅋ

- 입력 -
첫 줄에 종이 크기 n m
다음부터 종이 정보

--1트--: 이게 정답이라고? 
어우 씨 어려운데? 다 해봐야되는거 아님? 똑똑한 방법이 도저히 생각이 안나는데?
Convolution을 응용할 수 있으면 좋은데말야. 그거 말곤 방법 없을듯?
합성곱을 졸라 똑똑하게 구할 수 있는 방법이 있었는데..

그닥 똑똑한 방법이 아니라 시간 걸릴 것 같은데요 이거
일단 해보지 뭐 마땅한 것도 없으니
O^5 맛좀 봐라 ㅋㅋ
'''