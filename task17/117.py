def f(s, k):
    if k == 7:
        a.add(s)
        return 1
    if k > 7:
        return 0
    return f(s + 1, k + 1) + f(s + 5, k + 1) + f(s * 3, k + 1)


a = set()
f(1, 0)
print(len(a))