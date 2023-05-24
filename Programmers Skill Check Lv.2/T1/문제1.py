import sys
ip = sys.stdin.readline

def solution(number, k):
    k = int(k)
    front_max_index = number.index(max(number)) #가장 큰 숫자의 index = 가장 큰 숫자 앞의 숫자 개수
    temp = number

    # 밀 수 있는 숫자보다 많으면 못 민다. 밀 수 있을 때 까지 반복
    while (front_max_index > 0) and (front_max_index > k):
        temp = number[:front_max_index]
        front_max_index = temp.index(max(temp))

    k = k - front_max_index
    number = number[front_max_index:]

    # 남은 k 횟수만큼 뒷자리 밀기
    flag = False
    for _ in range(k):
        if flag:
            number = number[:len(number)-1]
        else:
            for i in range(1, len(number)-1):
                if number[i] < number[i+1]:
                    number = number[:i] + number[i+1:]
                    break
            else:
                flag = True
                number = number[:len(number)-1]

    return number

###
print(solution("1231234", 3))


''' 
어떤 숫자에서 k개 숫자를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하라

1924에서 1,2 제거하면 94니까 가장 크지.

- 입력 -
number, k
둘 다 문자열로 들어옴.

number는 2자리 이상 1,000,000자리이하
k는 1이상 number자릿수 미만 자연수.

- 출력-
가장 큰 숫자를 반환하되, 걔도 문자열로.

--1트--: 결과
단순 구현으로 생각했을 때

1. 전체 숫자 중 가장 큰 자릿수를 찾는다.
2. 앞자리 숫자들 지워버린다.
    #1 앞자리 숫자들 개수 > 지울 수 있는 숫자 개수
    앞자리 숫자들 중 가장 큰 숫자를 찾고, 그 앞을 민다.
    밀어낼 수 있는 숫자들 개수와 같아질 때 까지 반복.

    #2 앞자리 숫자들 개수 < 지울 수 있는 숫자 개수
    일단 앞자리 숫자들을 다 밀고, 남은 개수만큼 가장 작은 숫자들을 민다.

    #3 앞자리 숫자들 개수 = 지울 수 있는 숫자 개수
    그냥 밀면 됨
'''