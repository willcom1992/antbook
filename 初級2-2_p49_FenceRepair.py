import heapq
N = 3
L = [8, 5, 8]
heapq.heapify(L)

ans = 0
while len(L) > 1:
    x = heapq.heappop(L)
    y = heapq.heappop(L)
    ans += x+y
    heapq.heappush(L, x + y)

print(ans)