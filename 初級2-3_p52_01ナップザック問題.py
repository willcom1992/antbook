# bit全探索
n = 4
lst = [[2,3],[1,2],[3,4],[2,2]]
w = 5

ans = 0
for i in range(2 ** n):
    weight = 0
    value = 0
    for j in range(n):
        if 1 & (i >> j):
            weight += lst[j][0]
            value += lst[j][1]
    if weight <= w:
        ans = max(ans, value)

print(ans)