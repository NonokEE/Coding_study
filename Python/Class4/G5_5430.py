import sys
ip = sys.stdin.readline

from collections import deque

t = int(ip())
for _ in range(t):
    func_combination = ip().strip()
    length = int(ip())
    if length:
        #문자열 입력을 정수 배열(데크) 형태로 변경
        arr = ip().strip()
        arr = deque(map(int,arr[1:len(arr)-1].split(",")))
       
    else:
        #문자열 길이가 0으로 입력되면 위 전처리를 할 수 없음
        ip() #그래도 입력은 받아야 함
        arr = []
    
    left_or_right = 0 # 왼쪽을 pop할거면 0, 오른쪽을 pop할거면 1 (원래 상태면 0, 뒤집힌 상태면 1)
    error_flag = False

    # 함수 처리
    for func in func_combination:
        # 뒤집기
        if func == 'R':
            left_or_right = 1 - left_or_right
        
        # 삭제
        else:
            # 남은 길이가 있어야 삭제 가능
            if length:
                if left_or_right: #오른쪽 pop(뒤집힌 상태)
                    arr.pop()
                else:             #왼쪽 pop(원래 상태)
                    arr.popleft()
                length -= 1
            # 남은 길이가 없을 경우 error flag 활성화
            else:
                error_flag = True
                break
        
    
    # 결과 출력
    if error_flag: 
        print("error")
    else: 
        if left_or_right:
            arr.reverse()
        print("["+",".join(list(map(str, arr)))+"]")
        
''' AC
시간 1초 메모리 256MB

정수 배열 연산을 하기 위한 AC라는 언어를 만들었대.
R(뒤집기) D(버리기)라는 함수가 있대.

R은 배열에 있는 수의 순서를 뒤집는다.
D는 첫 번째 수를 버린다. -> 배열이 비어있으면 에러 발생
함수를 조합해서 한번에 사용할 수 있다.
ex) RDD면 뒤집고 다음 처음 두 수 버리기

배열 초기 값이랑 수행할 함수 주어졌을 때, 최종 결과를 구하라.

- 입력 -
첫 줄에 TC 개수 T. 최대 100
각 TC에 수행할 함수 p가 주어짐. p의 길이는 1이상 100,000이하
다음 줄에는 배열에 이미 들어있는 수의 개수 n이 주어짐. 0이상 100,000이하
그 다음에는 배열 원소들이 괄호 식으로 나열됨. 각 값은 1이상 100이하
p와 n의 합은 70만 이하

각 TC의 결과를 함수형태로 출력하되, 에러의 경우는 error 출력

--1트--: 일단 성공
스마트한 방법이 있을까?
딱히 없을 것음. 굳~이 찾는다면 연결리스트로 구현하는건데 메모리도 그다지 크지 않아.
deque를 쓰면 정말 쉬운 문제임. 너무 쉬워서 오히려 이상함.
일단 deque써서 해보고 

되면 deque날먹 빼서 해보고
안되면 다른 스마트한 방법을 해보자
'''