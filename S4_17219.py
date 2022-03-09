import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
site_dict = {}

for _ in range(N): 
    site, pw = ip().split()
    site_dict[site] = pw

for _ in range(M):
    print(site_dict[ip().strip()])


'''
첫 줄에 사이트 주소의 수 N과 비번찾으려는 사이트 수 M이 주어짐.
두번쨰 줄부터 N번 -> 사이트주소 비밀번호    (사이트 주소 중복 없음)(비밀번호는 무조건 알파벳 대문자)(둘 다 20자 이내)
그 다음부터 비번 찾으려는 사이트 수 입력됨. 이상한 사이트는 입력 안됨.

--1트--
그냥 해시다. 

'''