import sys
ip = sys.stdin.readline

num_man, num_party = map(int, ip().split())
man_dict = {}
for i in range(1, num_man+1):
    man_dict[i] = set([])

party_dict = {}
for i in range(1, num_party+1):
    party_dict[i] = set([])

temp = list(map(int, ip().split()))
man_queue = temp[1:]

for party in range(1, num_party+1): #딕셔너리(인접리스트) 초기화
    temp = list(map(int, ip().split()))
    arr = temp[1:]
    for p in range(temp[0]):
        man_dict[arr[p]].add(party)
        party_dict[party].add(arr[p])

### 루프 준비
from collections import deque

man_know = [False for _ in range(num_man + 1)]
party_know = [False for _ in range(num_party+1)] 

man_queue = deque(man_queue) #진실을 알고 있는 최초의 사람들로 큐 시작
party_queue = deque([])

### 루프 시작
while man_queue:
    cur_man = man_queue.popleft()

    # 방문 이력 없으면 순회 시작
    if not man_know[cur_man]:
        corrupted = list(man_dict[cur_man])    #그 사람이 가는 파티를 받아온다
        for i in range(len(corrupted)):        #아직 처리하지 않은 파티면 큐에 추가
            if not party_know[corrupted[i]]:
                party_queue.append(corrupted[i])
        man_know[cur_man] = True

    # 파티 처리 시작
    while party_queue:
        cur_party = party_queue.popleft()

        # 처리안한 파티일 경우 처리
        if not party_know[cur_party]:
            corrupted = list(party_dict[cur_party]) #그 파티 참가자들 받아오고
            for i in range(len(corrupted)):         #아직 처리 안된 참가자면 큐에 추가
                if not man_know[corrupted[i]]:
                    man_queue.append(corrupted[i])
            party_know[cur_party] = True
### res
res = -1
for pt in party_know:
    if not pt: res += 1
print(res)

''' 거짓말
시간 2초 메모리 128MB

과장할 수도 있고 그냥 말할 수도 있다.
청중 중에 진실을 아는 사람이 있다.
진실을 알고 있거나 알게 될 사람이 있는 자리에선 과장하면 안된다.
과장할 수 있는 최대 파티 개수를 구하라

- 입력 -
첫 줄에 사람 수 N과 파티수 M              1이상 50 이하
둘째 줄에는 진실을 아는 사람의 수와 번호   0이상 50이하
셋째줄부터 M개의 파티에 오는 사람들        각 파티 최소 1명, 50이하

--1트--: 성공
그냥 정직하게 살면 안되겠니?

n번 파티 딕셔너리 - 파티 참가자
n번 사람 딕셔너리 - 그 사람이 참가하는 파티

딕셔너리는 다 만들었는데 이제 어떻게 한담?
1. 진실 아는 사람이 가는 파티는 오염시킨다.
2. 오염된 파티 안에 있는 사람은 진실을 알게된다
한 바퀴 돌려서 남은 False 개수 하면 될 듯한데

한바퀴 가지고는 안됨.
그래프로 생각해야될 것 같긴 한데
그래프 두개 와리가리하는 탐색을 하면 어떨까 그닥 구현이 어려울 것 같진 않음
'''