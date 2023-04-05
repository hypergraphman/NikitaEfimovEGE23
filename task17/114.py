def f(s, c, k):
    if s == c:
        a.append(k)
        return 1
    if s > c:
        return 0
    return f(s + 1, c, k + 1) + f(s + 2, c, k + 1) + f(s * 2, c, k + 1)


a = []
f(1, 28, 0)
print(a.count(min(a)))