import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
poke_list = []
poke_dict = {}

for i in range(N):
    poke_name = ip().strip()
    poke_list.append(poke_name)
    poke_dict[poke_name] = i+1

for i in range(M):
    prob = ip().strip()
    try: print(poke_list[int(prob)-1])
    except: print(poke_dict[prob])

'''
첫 줄에 포켓몬 개수 N과 맞춰야하는 문제 개수 M 주어짐. (1 <= N, M <= 100,000, 자연수)
즉, N개는 배열이고 이후 M개가 문제다.

둘째 줄부터 1번부터 N번에 해당하는 포켓몬 이름이 들어옴.
포켓몬 이름은 모두 영어(첫 글자만 대문자거나 마지막만 대문자.) (2 <= 이름 길이 <= 20)
문제가 알파벳으로 들어오면 포켓몬 번호를 출력, 포켓몬 번호가 들어오면 문자 출력.
---
찾을라면 그냥 찾아도 되긴 하는데, 바로바로 끄집어 낼라면 숫자->영문명 리스트랑 영문명->숫자 딕셔너리 둘 다 있어야 될듯.
'''