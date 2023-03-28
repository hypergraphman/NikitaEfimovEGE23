a = [int(x) for x in open('17-332.txt').readlines()]
b = list(filter(lambda x: x % 17 == 0, a))
sr_b = sum(b) / len(b)
c = [0] * 37
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if sum(map(int, str(p1))) == sum(map(int, str(p3))) and p2 < sr_b:
        c[sum(map(int, str(p2)))] += 1
ans = 0
for i in range(len(c)):
    if c[i] > c[ans]:
        ans = i
print(sum(c))
print(ans)
