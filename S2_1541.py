import sys
ip = sys.stdin.readline

from collections import deque

exp = ip().strip()
nums = deque([])
oper = deque([])

s = 0
for i in range(len(exp)):
    if exp[i] == '+':
        nums.append(exp[s:i])
        s = i+1
        oper.append('+')
    elif exp[i] == '-':
        nums.append(exp[s:i])
        s = i+1
        oper.append('-')
else:
    nums.append(exp[s:len(exp)])

nums = list(map(int, nums))

minus = len(nums)
for i in range(len(oper)):
    if oper[i] == '-':
        minus = i
        break

res = 0

for i in range(min(len(nums), minus+1)):
    res += nums[i]
for i in range(minus+1, len(nums)):
    res -= nums[i]

print(res)


''' 잃어버린 괄호
시간 2초 메모리 128MB

양수 + - 괄호가지고 식 만들고 괄호 다 지웠음.
괄호 적절히 쳐서 식의 값을 최소로 만들려 한다.

- 입력 -
0~9, +, -로만 이루어진 식이 주어짐. 
수는 6자리 이상 나타나진 않음.
0으로 시작할 수도 있음.
총 길이는 50이하.
-로 시작하진 않음.

- 출력-
괄호를 적당히 쳤을 때의 최솟값을 출력

--2트--:
10+100-10+100-100-100
이론은 맞는데 알고리즘을 잘못 짠듯?

--1트--: 틀
일단 파싱은 센스것 하시고,
괄호 개수제한도 없으니까 -가 가장 커지면 됨.
사실상 마이너스가 하나라도 있으면 뒤의 것들은 전부 마이너스로 쳐도 되는거지.
괄호에 속으면 안됨.
마이너스가 하나라도 있으면, 그 이후는 전부 마이너스로 적용한다.

'''