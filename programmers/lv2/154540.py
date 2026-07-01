# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# from collections import deque
import sys
sys.setrecursionlimit(100000)


def solution(maps):
    answer = []
    max_x = len(maps[0])
    max_y = len(maps)
    visited = [[False] * max_x for _ in range(max_y)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        nonlocal day
        if visited[y][x] == True:
            return
        else:
            visited[y][x] = True

        if maps[y][x] != 'X':
            day += int(maps[y][x])
        else:
            return

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                dfs(new_x, new_y)

    for i in range(max_x):
        for j in range(max_y):
            if not visited[j][i] and maps[j][i] != 'X':
                day = 0
                dfs(i, j)
                if day != 0:
                    answer.append(day)

    if not answer:
        return [-1]
    else:
        return sorted(answer)


# def solution(maps):
#     max_y = len(maps)
#     max_x = len(maps[0])

#     visited = [[False] * max_x for _ in range(max_y)]
#     answer = []

#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]

#     def bfs(start_x, start_y):
#         queue = deque()
#         queue.append((start_x, start_y))
#         visited[start_y][start_x] = True

#         total = int(maps[start_y][start_x])

#         while queue:
#             x, y = queue.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if not (0 <= nx < max_x and 0 <= ny < max_y):
#                     continue

#                 if visited[ny][nx]:
#                     continue

#                 if maps[ny][nx] == 'X':
#                     continue

#                 visited[ny][nx] = True
#                 total += int(maps[ny][nx])
#                 queue.append((nx, ny))

#         return total

#     for y in range(max_y):
#         for x in range(max_x):
#             if not visited[y][x] and maps[y][x] != 'X':
#                 answer.append(bfs(x, y))

#     return sorted(answer) if answer else [-1]
