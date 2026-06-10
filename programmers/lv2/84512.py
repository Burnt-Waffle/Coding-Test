# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']

    def dfs(a):
        nonlocal count, answer
        if a == word:
            answer = count
            return
        if len(a) >= 5:
            return
        for v in vowels:
            if answer != 0:
                return
            count += 1
            dfs(a + v)

    dfs("")
    return answer


print(solution("AAAAE"))
