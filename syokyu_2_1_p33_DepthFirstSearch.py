n = 4
a = [1,2,4,7]
k = 13

def dfs(i, sum):
    if i == n:
        return sum == k

    # a[i]を未使用
    if dfs(i+1, sum):
        return True

    # a[i]を使用
    if dfs(i+1, sum + a[i]):
        return True

    return False

if dfs(0, 0):
    print('YES')
else:
    print('NO')
#end