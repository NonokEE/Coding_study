import sys
ip = sys.stdin.readline

n = int(ip())
field = []

last_maxindex = 1
last_max = 0
total_max = 0

last_minindex = 1
last_min = 0
total_min = 0

last_center = 0

for _ in range(n):
    cur = list(map(int, ip().split()))

    #최대값이 여러 개 있으면 가급적 가운데 것 선택
    maxval = max(cur)
    minval = min(cur)

    for i in range(3):
        if cur[i]==maxval:
            maxind = i
            if i==1:
                break
    for i in range(3):
        if cur[i]==minval:
            minind = i
            if i==1:
                break

    ## 최댓값
    # 이전에 1이었으면 현재 중에서 아무거나 뽑으면 된다.
    if last_maxindex == 1:
        last_maxindex = maxind
        last_max = maxval
        total_max += last_max

    # 이전에 양끝값이었으면 
    else:
        # 현재 뽑을게 같거나 1이면 그대로 가도 된다.
        if (maxind == 1) or (maxind == last_maxindex):
            last_maxindex = maxind
            last_max = maxval
            total_max += last_max

        #반대쪽을 뽑아야 하는 경우, 반대쪽 빼고 최대값 + 이전회차 최대값 vs 최댓값 + 이전회차 가운데. 같으면 전자 선택
        else:
            if maxind == 0: temp_maxval = max(cur[:2])
            else          : temp_maxval = max(cur[1:])

            #현재 최고값을 포기하는게 나은 경우
            if (temp_maxval + last_max) >= maxval + last_center:
                last_maxindex = cur.index(temp_maxval)
                last_max = temp_maxval
                total_max += last_max

            #이전걸 바꿔주는게 나은 경우)
            else:
                total_max -= last_max

                last_maxindex = maxind
                last_max = maxval
                total_max += last_center
                total_max += maxval

    ## 최솟값
    # 이전에 1이었으면 현재 중에서 아무거나 뽑으면 된다.
    if last_minindex == 1:
        last_minindex = minind
        last_min = minval
        total_min += last_min

    # 이전에 양끝값이었으면 
    else:
        # 현재 뽑을게 같거나 1이면 그대로 가도 된다.
        if (minind == 1) or (minind == last_minindex):
            last_minindex = minind
            last_min = minval
            total_min += last_min

        #반대쪽을 뽑아야 하는 경우, 반대쪽 빼고 최대값 + 이전회차 최대값 vs 최댓값 + 이전회차 가운데. 같으면 전자 선택
        else:
            if minind == 0: temp_minval = min(cur[:2])
            else          : temp_minval = min(cur[1:])

            #현재 최고값을 포기하는게 나은 경우
            if (temp_minval + last_min) >= minval + last_center:
                last_minindex = cur.index(temp_minval)
                last_min = temp_minval
                total_min += last_min

            #이전걸 바꿔주는게 나은 경우)
            else:
                total_min -= last_min

                last_minindex = minind
                last_min = minval
                total_min += last_center
                total_min += minval

    last_center = cur[1]

print(total_max, total_min)


''' 내려가기
시간 1초 메모리 4MB..?
N줄에 0이상 9이하의 숫자가 3개씩 적혀있다.

첫 줄에서 시작해서 마지막 줄에서 끝날건데,
우선 첫 줄의 수 3개 중 하나를 골라서 시작한다.
그리고 다음 줄로 내려가는데, 바로 위에서 골랐던 칸을 고르거나, 그 칸에 인접한 칸만 고를 수 있다.

이 때 얻을 수 있는 최대 점수랑 최소 점수를 구하세용

- 입력 -
첫 줄에 N
다음부터 N번째 줄의 숫자 3개

--1트--: 틀렸습니다~!
이것도 DP인데 어떻게 머리를 쓰느냐..
DP의 핵심은 순차를 쪼개고 점화식으로 만드는 것이다.
내려가는 회차를 쪼갤 수가 있을 것으로 보이는데

1회차만 있으면 현재 값 중에서만 고르면 돼
2회차가 있으면 전 값을 참고해야 함.
아무튼 한쪽 끝 값을 고르고 싶으면 이전 회차가 가운데거나 현재랑 같아야 함.

따라서 현재 고를 수 있는게 3개면 아무거나
현재 고를 수 있는게 한쪽 끝이랑 가운데면 2개중 아무거나 or 이전 시차에서 가운데 뽑고 현재 아무거나

메모리 부족 뜨면 필드 미리 선언 안하는 방식으로 수정
가면서 봐도 되긴 할듯

'''