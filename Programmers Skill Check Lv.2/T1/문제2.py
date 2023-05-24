def solution(s:str):
    s = s[1:-1].split("}")[0:-1]
    for i in range(len(s)):
        if s[i][0] == ",":
            s[i] = s[i][1:]

    for i in range(len(s)):
        if s[i][0] == "{":
            s[i] = s[i][1:]

    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(",")))

    s.sort(key = lambda x:len(x))
        
    answer = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in answer:
                answer.append(s[i][j])

    return answer

## 

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

''' 
n개의 요소를 가진 튜플을 n튜플이라고 한다.

원소 중복은 가능
순서가 다르면 다른 튜플
튜플의 원소 개수는 유한.

원소가 n개고 중복되는 원소가 없는 튜플이 주어질 때 
ex) 튜플 = (1,2,3)
-> {1}, {1,2}, {1,2,3} 이런식으로 표현핳ㄹ 수 있다.
그리고 집합은 원소 순서 바뀌어도 된다.

저런식으로 {}가 s로 주어질 때, s가 표현하는 튜플을 배열에 담아 return하세요

- 입력 -
s, 5이상 1,000,000이하
s는 숫자랑 { } ,로만 이루어져있다.
0으로 시작하는 경우는 없다.
원소는 1이상 100,000이하다.
리턴배열 길이는 1이상 500이하다.

- 출력-

--1트--: 결과
문자열 처리 문제네.
'''