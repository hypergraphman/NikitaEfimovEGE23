# from functools import reduce
#
# reduce(lambda x, y: x*y, map(int, '1234'))
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 1
#     return f(n - 1) + f(n - 2)
a = [None, 2, 1]


for i in range(3, 50):
    a.append(a[-1] + a[-2])
    print(i, a[i])