import sys
ip = sys.stdin.readline

# 입력
num_node = int(ip())
node_distance = []
node_fuel = []
for _ in range(num_node):
    dis, sat = map(int, ip().split())
    node_distance.append(dis)
    node_fuel.append(sat)

dest, cur_fuel = map(int, ip().split())

# 알고리즘
"""
1. 현재 연료로 갈 수 있는 최대 거리를 측정
    
    1-1. 최대 거리에 도착했다면 편의점 카운트 출력하며 종료
    1-2. 가능한 노드를 전부 들렀으나 다음 미방문 노드에 도달할 수 없는 경우에도 종료
    1-3. 둘 다 아니라면 지금까지 들르지 않은, 방문할 수 있는 노드 중 가장 연료 많은 것을 먹는다. 카운트 +1. (가면서 먹으나 나중에 먹으나 상관 없음. 결과론적인거라.)
    
"""
count = 0
flag = 0
cur_node = 0
not_visited = [i for i in range(len(node_distance))]
for _ in range(num_node): 
    if (cur_fuel >= dest) or flag: # 도달했거나 가능한 방문이 없는 경우 루프 종료   
        break

    # 현재 연료로 가능한 최대거리 편의점 찾기
    for i in range(cur_node, len(node_distance)):
        if cur_fuel >= node_distance[i]: cur_node = i

    # 최대 거리 내 편의점 중 가장 연료가 많은, 방문하지 않은 곳 찾기
    candidate = node_fuel[0:cur_node+1]   #최대 거리 내 편의점 목록, 즉 후보
    temp = len(candidate)
    flag = 1

    for _ in range(temp):
        max_fuel = max(candidate)   #최대 연료 산출 및 인덱스 찾기
        max_index = candidate.index(max_fuel)

        if max_index in not_visited: #방문하지 않은 곳이라면 현재 연료에 더해주고 방문처리
            cur_fuel += max_fuel
            not_visited.remove(max_index)
            count += 1
            flag = 0
            break
        else: #이미 방문한 곳이라면 후보에서 제거 (실제로 remove하면 index혼동이 오므로, 연료를 -1로 만들어주는 방법으로)
            candidate[max_index] = -1

if cur_fuel >= dest: print(count)# 도달했다면 카운트 출력  
else: print(-1)

''' 수민이맨
1km당 포만감 1 감소, 포만감 0이면 움직일 수 없음
가는 길에 편의점이 있어서 포만감을 올릴 수 있다. 
수민이의 포만감 상한은 없지만 편의점에서 얻을 수 있는 포만감 최대치는 있는듯?

편의점 들르는 횟수는 최소화 하고 싶다. 
편의점 위치, 각 편의점에서 얻을 수 있는 포만감이 주어질 때 편의점에 들르는 횟수 구하는 프로그램

! 도달할 수 없는 경우도 있다. 이떈 -1 출력
! 편의점 최소 1개

"
연료는 소모되도록 계산할 필요는 없음. 연료 총량이 목적지보다 크거나 같으면 도달 가능

논점1. 알고리즘
지금 가진걸로 다음 거 갈 수 있으면 건너뛰어? 근데 지금까지 것들 다 필요하면 어캄?

논점2. 도달불가능한 경우
전체 거리가 문제가 아니고, 갈 수 있는 곳 다 들러도 다음 노드 도착 못하는 경우도 있음.

1. 일단 연료 떨어질 때 까지 최대한 가본다.
    1-0. 갈 수 없다면 -1 출력 후 종료
    1-1. 최대 거리에 도착했다면 편의점 카운트 출력하며 종료
    1-2. 아니라면 지금까지 들른 곳 중 가장 연료 많은 것을 먹는다. 편의점 카운트 +1. (가면서 먹으나 나중에 먹으나 상관 없음. 결과론적인거라.)
         그리고 다시 1로 간다.

'''