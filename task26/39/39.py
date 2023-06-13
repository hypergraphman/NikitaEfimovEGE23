f = open('text.txt')
n, m = map(int, f.readline().split())
anot180 = []
a180 = []
for el in f.readlines():
    t = int(el)
    if 180 <= t <= 200:
        a180.append(t)
    else:
        anot180.append(t)
a180.sort(reverse=True)
anot180.sort()
k = 0
i = 0
while m < a180[i]:
    m -= a180[i]
    k += 1
    i += 1
i = 0
while m < anot180[i]:
    m -= anot180[i]
    k += 1
    i += 1
while True:
    i -= 1
    m += anot180[i]
    k -= 1
    for j in range(len(anot180) - 1, i - 1, -1):
        if m >= anot180[j]:
            m -= anot180[j]
            k += 1
            del anot180[j]
            break
    if i == j:
        break
print(k)