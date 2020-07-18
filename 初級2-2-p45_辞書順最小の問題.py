from collections import deque

N = 6
S = 'ACDBCB'

sl = deque(list(S))

T = ''
for i in range(N):
    # 末尾が小さい
    if sl[0] > sl[-1]:
        T += sl.pop()

    # 先頭が小さい
    elif sl[0] < sl[-1]:
        T += sl.popleft()

    # 先頭も末尾も同じ場合
    else:
        # slとslの逆順を比較
        if list(sl) >= list(reversed(sl)):
            T += sl.pop()
        else:
            T += sl.popleft()

print(T)
