# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    current_max_day = 0
    for progress, speed in zip(progresses, speeds):
        days_left = (100 - progress + speed - 1) // speed
        if current_max_day >= days_left:
            answer[-1] += 1
        else:
            current_max_day = days_left
            answer.append(1)
    return answer


print(solution([93, 30, 55], [1, 30, 5], [2, 1]))
