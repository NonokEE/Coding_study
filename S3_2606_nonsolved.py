import sys
ip = sys.stdin.readline

N = int(ip())
L = int(ip())




'''
한 컴퓨터가 웜에 걸리면, 그 컴퓨터와 네트워크 상 연결되어 있는 모든 컴퓨터는 웜에 걸린다.
1번 컴퓨터가 웜에 걸릴 때, 웜에 걸리는 컴퓨터 수를 구하라

첫 줄에는 컴퓨터 수(100 이하)
각 컴퓨터에는 1번부터 차례대로 번호.
둘째 줄에는 연결 쌍 개수
세번째 줄부터 연결 정보
--1트--
그냥 그래프 탐색 아님?
+ 파이썬에서 클래스 쓸 때, __init__ 안에 써야 인스턴스 변수고, 그냥 생으로 쓰면 클래스 변수(static)임;
--2트--
클래스 꼼수 쓰지 말고 그냥 정석으로 (인접 행렬, 인접 리스트)로 하자...
'''