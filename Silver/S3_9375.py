import sys
ip = sys.stdin.readline

TC = int(ip())

for _ in range(TC):
    n = int(ip())
    closet = {}
    for _ in range(n):
        name, part = ip().split()
        if part in closet.keys(): closet[part] += 1
        else: closet[part] = 2
    res = 1
    for val in list(closet.values()):
        res *= val
    print(res-1)

''' 패션왕 신해빈
같은 옷 조합은 절대로 다시 안 입는다.

첫 줄에 최대 100개의 TC가 주어짐.

각 TC의 첫 줄에는 의상의 수 n이 주어진다. (0<=n<=30)
다음 n개에는 의상의 이름과 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자, 같은 이름의 의상은 없다.

각 TC에 대하여, 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력.

--1트-- : 성공
그냥 수학 문제 아닌가?
같은 이름 의상은 없다 그랬으니까 문자열 앞에 것은 버리고 부위만 더해줌.
부위 개수가 몇 개가 될지는 모른다. 아무튼 모든 부위별 의류 개수를 곱해주면 됨.
이 때, 안 입는다는 경우도 있으니까 부위가 추가될 때 최소 1부터 시작임. 
즉, 첫 부위에 의류가 추가되면 2부터 시작.
다 벗는다는 선택지는 없으니까 결과에서 -1만 해주면 됨.
'''