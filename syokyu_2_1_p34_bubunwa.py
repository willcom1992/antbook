# ビット全探索での実装
n = 4
al = [1,2,4,7]
k = 13

for i in range(2**n):
    sum  = 0
    for j in range(n):
        #ビットシフトを行い、もしもビットが立っていたら和に加える
        if 1 & (i >> j):
            sum += al[j]
            
    if sum == k:
        print('Yes')
        break

print('No')
