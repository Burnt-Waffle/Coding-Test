# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    closet = dict()
    answer = 1
    for s in clothes:
        closet[s[1]] = closet.get(s[1], 0) + 1
    for v in closet.values():
        answer *= (v + 1)
    return answer - 1
