# 幅優先探索で実装
from collections import deque

N = 10
M = 10
maze = ['#S######.#',
        '......#..#',
        '.#.##.##.#',
        '.#........',
        '##.##.####',
        '....#....#',
        '.#######.#',
        '....#.....',
        '.####.###.',
        '....#...G#']

# 番兵化、およびスタート地点とゴール地点の取得
sy, sx = 0, 0
gy, gx = 0, 0
for i in range(N):
    if 'S' in maze[i]:
        sy = i + 1
        sx = maze[i].index('S') + 1
    elif 'G' in maze[i]:
        gy = i + 1
        gx = maze[i].index('G') + 1
    maze[i] = list('#' + maze[i] + '#')
maze.insert(0, ['#'] * (M + 2))
maze.append(['#'] * (M + 2))

# スタート地点の座標(y,x)とコスト(0)を設定
q = deque([[sy, sx, 0]])
# 重複した探索を避けるため、スタート地点は探索済みにしておく
maze[sy][sx] = '#'

while q:
    y, x, depth = q.popleft()
    if [y, x] == [gy, gx]:
        print(depth)
        break

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for d in directions:
        if maze[y + d[0]][x + d[1]] != '#':
            q.append([y + d[0], x + d[1], depth + 1])
            maze[y + d[0]][x + d[1]] = '#'
