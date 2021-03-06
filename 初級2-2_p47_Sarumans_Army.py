import bisect
n = 6
r = 10
x = [1,11,20,30,35,50]
# 昇順
x.sort()

# 最初の点を決める
idx = bisect.bisect_right(x, x[0]+r)-1
now = x[idx]
cnt = 1

while True:
    if now+r >= max(x):
        break
    # 次に打つべき数字のインデックスを取得
    idx = bisect.bisect_right(x,x[idx+1] + r)

    # リストの範囲外なら終了
    if idx <= n-1:
        now = x[idx]
        cnt += 1
    else:
        cnt += 1
        break

print(cnt)