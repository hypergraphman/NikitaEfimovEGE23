a = list(map(int, open('17.d4.txt')))

mn = min(a)
mx = max(a)
sr = (mx + mn) / 2

r = []
for p1, p2 in zip(a[:len(a) // 2], a[-1: -len(a) // 2 - 1: -1]):
    if (p1 < sr and p2 > sr) or (p1 > sr and p2 < sr):
        r.append(p1 + p2)
print(len(r), max(r))

# 2120 14972