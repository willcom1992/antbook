n = 5
sl = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

ts = []
for s, t in zip(sl, t):
    ts.append([t, s])

# 終わり時間で昇順にソート
ts.sort()

now = 0  # 現在時刻
cnt = 0
# 選べる仕事の中で、終了時間が最も早いものを貪欲的に選ぶ
for i in range(n):
    if ts[i][1] < now:
        now = ts[i][0]
        cnt += 1
print(cnt)
