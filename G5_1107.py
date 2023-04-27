import sys
ip = sys.stdin.readline

n = ip().strip()
m = int(ip())
broken = []
if m: 
    broken = list(map(int, ip().split()))

cur = '100'
res = 0

# 자릿 수 올리거나 내릴 때 10 되거나 -1 된거 정리
def digit_organize(num:list):
    # 10 정리
    for i in range(len(num)-1, 0, -1):
        if num[i] > 9:
            num[i] -= 10
            num[i-1] += 1
    if num[0] > 9:
        num[0] -= 10
        num = [1] + num
    # -1 정리
    for i in range(len(num)-1, 0, -1):
        if num[i] < 0:
            num[i] += 10
            num[i-1] -= 1
    if num[0] == 0:
        if len(num) > 1: num = num[1:]
    return num

# 고장난 부분 찾기. 없으면 None 반환
def get_broken_point(num, broken:list):
    for digit in range(len(num)):
        if int(num[digit]) in broken:
            return digit
    else:
        return None

# 로직 #
if n == '100':
    res = 0
elif not broken:
    res = min(len(n), abs(int(n) - 100))
elif len(broken) == 10:
    res = abs(int(n) - 100)
else:
    INF = 99999999
    candidate = [abs(int(n) - 100)]  #일단 어떤 경우에도 쌩으로 이동하는거랑은 비교해야됨

    # 버튼 고장난 부분 검사
    point = get_broken_point(n, broken)

    if point == None: # 고장 해당 없다면 그냥 누르면 되고, 그게 웬만하면 int(n) - 100과 함께 최소의 경우가 될 것.
        candidate.append(len(n))

    # 눌러야 할 버튼이 고장난 경우
    else:
        ########
        # 고장난 자리 올리기
        higher = list(map(int,list(n))) #숫자 리스트로 변경

        # 1. 아랫 자리들 가능한 작은 수로 변경
        num = 0
        while num in broken: num += 1

        for i in range(point+1, len(higher)):
            higher[i] = num

        # 2. 바꿀 자리 포함 윗 자리 재점검
        while (point != None):
            higher[point] += 1 #바꿀 자리 바꾸기
            higher = digit_organize(higher) 
            point = get_broken_point(higher, broken)
            
            higher_integerized = int("".join(list(map(str, higher))))
            count = higher_integerized - int(n) + len(higher)
            if count > candidate[0]: #생으로 옮기는것보다 비효율적이게 되면 볼 필요도 없음
                break
        else:    
            candidate.append(count)

        ########
        # 고장난 자리 내리기
        lower = list(map(int,list(n)))
        point = get_broken_point(lower, broken)

        # 1. 아랫 자리들 가능한 큰 수로 변경
        num = 9
        while num in broken: num -= 1

        for i in range(point+1, len(lower)):
            lower[i] = num

        # 2. 바꿀 자리 포함 윗 자리 재점검
        while point != None:
            lower[point] -= 1 #바꿀 자리 바꾸기
            lower = digit_organize(lower) 
            point = get_broken_point(lower, broken)

            lower_integerized = int("".join(list(map(str, lower))))
            count = int(n) - lower_integerized + len(lower)
            if count > candidate[0]: 
                break
        else:    
            candidate.append(count)    

    res = min(candidate)

print(res)


''' 리모컨
시간 2초 메모리 256MB

0~9번 버튼, +, -가 있다. 
플마 누르면 +1 -1로 채널 이동, 채널 0에서 - 누르면 아무일 없음.
채널은 무한대 만큼 있다.

N채널로 이동하고 싶다 치고
어떤 버튼이 고장났는지 주어졌을 때, 
채널 N으로 이동하기 위해 버튼을 최소 몇번 눌러야하는지 구하셈

초기 채널 시작은 100번 채널


- 입력 -
첫 줄에목적지 채널 N(0이상 500,000이하)
둘째 줄에 고장난 버튼 개수 M(0이상 10이하)
고장난 버튼이 있는 경우에만 세번째 줄 들어오고, 어떤 버튼 고장났는지 주어짐. 중복은 X



--1트--: 틀렸습니다
오랜만에 무식한 문제가 나온 것 같습니다. 탐색 알고리즘 아닌거같음.
시간이 꽤 널널하다

1. 고장난 버튼이 없다면
목적지 채널의 자릿수 vs (목적채널 - 현재 채널) 중 작은거

2. 고장난게 있다면
가능한 경우 다 해보는게 낫나?

12345로 가는데
3 4가 고장났다 치고

1. 안고장난 자리수는 넘기기

12까지는 패스

3이 고장났으니 3을 +1하거나 -1 한다.

+1한 경우는 뒷자리를 0으로, 불가능하면 1, 2, 3 이렇게 올려줌
-1한 경우는 뒷자리를 

+1이랑 -1도 불가능하면 +2, +3 이렇게 감.

만약
9000 인데 9가 고장났으면?
8888로은 가능하고
10000으로 해줘야지


'''