# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    n = len(topping)
    if n == 1:
        return 0

    left_unique = [0] * n
    right_unique = [0] * n

    left_set = set()
    right_set = set()

    for i in range(n):
        left_set.add(topping[i])
        left_unique[i] = len(left_set)

    for i in range(n - 1, -1, -1):
        right_set.add(topping[i])
        right_unique[i] = len(right_set)

    answer = 0
    for i in range(n - 1):
        if left_unique[i] == right_unique[i + 1]:
            answer += 1

    return answer

# from collections import Counter

# def solution(topping):
#     answer = 0

#     set1 = Counter(topping)
#     set2 = set()

#     for t in topping:
#         set2.add(t)

#         set1[t] -= 1

#         if set1[t] == 0:
#             del set1[t]

#         if len(set1) == len(set2):
#             answer += 1

#     return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
