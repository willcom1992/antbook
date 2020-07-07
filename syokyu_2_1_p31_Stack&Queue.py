# スタックとキュー
from collections import deque

s = deque([])  # []
s.append(1)  # [1]
s.append(2)  # [1, 2]
s.pop()  # [1]
s.pop()  # []

q = deque([])  # []
q.append(1)  # [1]
q.append(2)  # [1, 2]
q.popleft()  # [2]
q.popleft()  # []
