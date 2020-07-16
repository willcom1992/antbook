# 硬貨の問題、貪欲法
c1 = 3
c5 = 2
c10 = 1
c50 = 3
c100 = 0
c500 = 2
A = 620

cl = [[1,c1],[5,c5],[10,c10],[50,c50],[100,c100],[500,c500]]
# 降順にソート
cl.sort(reverse=True)

ans = 0
for i in range(6):
    ans += min(A//cl[i][0],cl[i][1])
    A -= min(A//cl[i][0],cl[i][1])*cl[i][0]
    if A == 0:
        break
print(ans)