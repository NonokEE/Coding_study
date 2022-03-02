import sys
ip = sys.stdin.readline

N = int(ip())
xy = []
for i in range(N): xy.append(list(map(int, ip().split())))

xy.sort(key=lambda x:(x[1], x[0]))
for i in range(N): print(xy[i][0], xy[i][1])

'''
정렬 문제.
N개의 2차원 좌표 입력 받고, Y를 오름차순으로, Y가 같으면 X를 오름차순으로 정렬하여 줄력
sort에 key로 lambda식을 쓰는 문제

*lambda식 쓰는법
lambda x: x+10
x가 결과, : 뒤가 표현식

sort에서 쓰려면 정렬 기준을 표현식으로 해주면 됨.
'''