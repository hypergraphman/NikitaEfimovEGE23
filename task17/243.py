def f(s, c, p):
    if s == c and s in p:
        return 1
    if s < 40 or s > 49 or s in p:
        return 0
    return f(s + 1, c, p + (s,)) + f(s + 3, c, p + (s,)) + f(s - 1, c, p + (s,)) + f(s - 3, c, p + (s,))


print(f(42, 42, tuple()))