import sys
ip = sys.stdin.readline

n = int(ip())

temp_max = [0,0,0]
temp_min = [0,0,0]

total_max = [0,0,0]
total_min = [0,0,0]

for _ in range(n):
    cur = list(map(int, ip().split()))

    #현재 각 3개를 숫자에 대하여, 이전 회차를 고려하여 최선의 선택지를 고름
    for i in range(3):
    
        #첫번째를 고른 경우 이전루프의 0 또는 1중 선택
        if i == 0 :
            total_max[0] = cur[0] + max(temp_max[0], temp_max[1])
            total_min[0] = cur[0] + min(temp_min[0], temp_min[1])

        #두번쨰를 고른 경우 셋 중 선택
        elif i == 1:
            total_max[1] = cur[1] + max(temp_max[0], temp_max[1], temp_max[2])
            total_min[1] = cur[1] + min(temp_min[0], temp_min[1], temp_min[2])

        #세번째 -> 1빼고 선택
        else:
            total_max[2] = cur[2] + max(temp_max[1], temp_max[2])
            total_min[2] = cur[2] + min(temp_min[1], temp_min[2])

    #루프 거치고 나면 total배열에는 현재 입력된 각 숫자 + 이전회차 중 가장 나은 선택지 저장됨. 갱신
    temp_max = total_max[:]
    temp_min = total_min[:]

#최종적으로 남은 숫자들에서 최고값만 출력하면 됨.
print(max(total_max), min(total_min))



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

--2트--:
이전거 한번만 고려하면 안되려나
메모리가 터질 일은 없으니까 방법이 잘못된건데

조건문이 길어지면 틀린다. 100줄 넘어가면 뭔가 잘못된거임.
한번만 비교하는건 아무래도 상관 없을 것 같은데,
그냥 매 회차마다 비교를 해버리는게?

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