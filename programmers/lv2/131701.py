# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    n = len(elements)
    extended_arr = elements * 2
    unique_sums = set()
    for length in range(1, n+1):
        current_sum = sum(extended_arr[0:length])
        unique_sums.add(current_sum)

        for start in range(1, n):
            current_sum = current_sum - \
                extended_arr[start-1] + extended_arr[start+length-1]
            unique_sums.add(current_sum)

    return len(unique_sums)


print(solution([7, 9, 1, 1, 4]))
