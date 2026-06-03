# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    # left부터 right까지의 인덱스만 순회합니다.
    for k in range(left, right + 1):
        # 1차원 인덱스를 2차원 좌표(행, 열)로 변환
        row = k // n
        col = k % n

        # 행과 열의 인덱스 중 더 큰 값에 1을 더한 것이 해당 위치의 숫자가 됩니다.
        cell_value = max(row, col) + 1
        answer.append(cell_value)

    return answer


print(solution(4, 7, 14))
