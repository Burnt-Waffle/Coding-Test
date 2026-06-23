# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# def solution(dirs):
#     visited = set()

#     x1, y1 = 0, 0

#     for d in dirs:
#         x2, y2 = x1, y1

#         if d == 'U':
#             y2 = y1 + 1
#         elif d == 'D':
#             y2 = y1 - 1
#         elif d == 'R':
#             x2 = x1 + 1
#         elif d == 'L':
#             x2 = x1 - 1

#         if -5 <= x2 <= 5 and -5 <= y2 <= 5:
#             visited.add((x1, y1, x2, y2))
#             visited.add((x2, y2, x1, y1))

#             x1 = x2
#             y1 = y2

#     return len(visited) // 2


def solution(dirs):
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    x, y = 0, 0

    visited = set()

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))

            x, y = nx, ny

    return len(visited // 2)
