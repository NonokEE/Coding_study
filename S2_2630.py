def pfield(arr):
    for line in arr:
        print(line)
##

import sys
ip = sys.stdin.readline

n = int(ip())
field = [list(map(int, ip().split())) for _ in range(n)]
blue, white = 0, 0

def getSum(arr):
    res = 0
    for line in arr: res += sum(line)
    return res

def cutPaper(paper, n):
    lu, ld, ru, rd = [], [], [], []
    for line in range(len(paper)):
        if line < n:
            lu.append(paper[line][:n])
            ru.append(paper[line][n:])
        else:
            ld.append(paper[line][:n])
            rd.append(paper[line][n:])

    return lu, ld, ru, rd

def judgePaper(paper:list, n):
    paperSum = getSum(paper)
    if paperSum == n**2:
        global blue
        blue += 1
    elif paperSum == 0:
        global white
        white += 1
    else:
        n = n//2
        lu, ld, ru, rd = cutPaper(paper, n)
        judgePaper(lu, n)
        judgePaper(ld, n)
        judgePaper(ru, n)
        judgePaper(rd, n)

judgePaper(field, n)
print(white)
print(blue)
         
''' 색종이 만들기
시간 1초 메모리 128MB

정사각형 칸으로 이루어진 정사각형 종이가 있다.
각 정사각형은 하얀색이나 파란색으로 칠해져있다.
규칙에 따라 잘라서 댜앙한 크기를 가진 정사각형의 흰색/파란색 색종이를 만들거다.

n*n크기 정사각형으로 시작 (n은 2^k이고, k는 1이상 7이하의 자연수)
전체가 같은 색이 아니면 4등분. 이걸 각각에 반복한다.
최종적으로 파란색(1)과 하얀색(0)의 개수를 출력하세요

- 입력 -
첫 줄에 한 변의 길이 N
둘째줄부터 종이 정보

--1트--: ??? 뭐야 했던거네?
이거 숱하게 했던 분할 정복.
근데 연습할 겸 그냥 쌩으로 다시 해보자.
'''