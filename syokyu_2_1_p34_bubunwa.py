# ビット全探索での実装
n = 4
al = [1, 2, 4, 7]
k = 13

# すべてのパターンを2進数で表現するので2のn乗通り用意
for i in range(2 ** n):
    sum = 0

    # 各桁ごとにビットが立っているか調べる
    for j in range(n):
        # もしも対象の桁のビットが立っていたら和に加える
        if 1 & (i >> j):
            sum += al[j]

    if sum == k:
        print('Yes')
        break

print('No')
