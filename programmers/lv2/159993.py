# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    start_pos = lever_pos = end_pos = None

    for i, row in enumerate(maps):
        if 'S' in row:
            start_pos = (i, row.index('S'))
        if 'E' in row:
            end_pos = (i, row.index('E'))
        if 'L' in row:
            lever_pos = (i, row.index('L'))

    def bfs(start, end):

        queue = deque([start])
        visited = [[-1] * m for _ in range(n)]
        visited[start[0]][start[1]] = 0

        while queue:
            x, y = queue.popleft()

            if (x, y) == end:
                return visited[x][y]

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

        return -1

    time_to_lever = bfs(start_pos, lever_pos)
    if time_to_lever == -1:
        return -1

    time_to_exit = bfs(lever_pos, end_pos)
    if time_to_exit == -1:
        return -1

    return time_to_exit + time_to_lever


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
