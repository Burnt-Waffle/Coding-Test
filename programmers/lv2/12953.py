# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = get_lcm(answer, arr[i])
    return answer


def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)


print(solution([2, 6, 8, 14]))
