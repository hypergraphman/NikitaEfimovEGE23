from functools import lru_cache


@lru_cache
def f(n):
    pass


for i in range(2000):
    f(i)


print(f(2000))