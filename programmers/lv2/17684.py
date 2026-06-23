# https://school.programmers.co.kr/learn/courses/30/lessons/17684

# def solution(msg):
#     answer = []
#     dictionary = []
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for char in alphabet:
#         dictionary.append(char)
#     i = 0
#     while i < len(msg):
#         temp = ''
#         answer_temp = 0
#         for j in range(i, len(msg)):
#             temp += msg[j]
#             if temp in dictionary:
#                 answer_temp = max(answer_temp, list(dictionary).index(temp)+1)
#                 i = j + 1
#             else:
#                 dictionary.append(temp)
#                 break
#         answer.append(answer_temp)
#     return answer


def solution(msg):
    answer = []

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dictionary = {char: i + 1 for i, char in enumerate(alphabet)}

    next_index = 27

    p = 0
    while p < len(msg):
        q = p + 1
        while q <= len(msg) and msg[p:q] in dictionary:
            q += 1

        w = msg[p:q-1]
        answer.append(dictionary[w])

        if q <= len(msg):
            dictionary[msg[p:q]] = next_index
            next_index += 1

        p = q - 1

    return answer
