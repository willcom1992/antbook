import heapq
N = 3
L = [8, 5, 8]

# 優先度付きキュー
heapq.heapify(L)

ans = 0
while len(L) > 1:
    # 最も短い板
    x = heapq.heappop(L)
    # 次に短い板
    y = heapq.heappop(L)

    ans += x+y
    # 新しくできた板を優先度付きキューに追加
    heapq.heappush(L, x + y)

print(ans)


