# p30
# nの階乗
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))


# フィボナッチ数列のn番目の数(再帰)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)

print(fib(6))

# p31
# フィボナッチ数列のn番目の数(再帰メモ化Ver)
memo = {}

def fib_memo(n):
    if n <= 1:
        return n
    if n in memo.keys():
        return memo[n]
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return fib_memo(n)

print(fib_memo(10))