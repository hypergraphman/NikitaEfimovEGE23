f = open('26.txt')
n = int(f.readline())
a = [0] * 80
b = [0] * 20
c = []
for _ in range(n):
    t1, t2, cat = f.readline().split()
    t1 = int(t1)
    t2 = int(t2)
    c.append((t1, t1 + t2, cat))
c.sort()
count_par_a = 0
count_not_par = 0
for car in c:
    is_par = False
    if car[2] == 'A':
        for i in range(len(a)):
            if a[i] <= car[0]:
                a[i] = car[1]
                is_par = True
                break
    if car[2] == 'B' or not is_par:
        for i in range(len(b)):
            if b[i] <= car[0]:
                b[i] = car[1]
                is_par = True
                break
    if car[2] == 'A' and is_par:
        count_par_a += 1
    if not is_par:
        count_not_par += 1
print(count_par_a, count_not_par)