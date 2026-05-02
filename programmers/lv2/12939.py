# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"


print(solution("4 1 2 5"))
