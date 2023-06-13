f = open('26-120.txt')
m, n = map(int, f.readline().split())
a = []
for amount_par in map(int, f.readline().split()):
    a.append([0] * amount_par)
cars = []
for _ in range(n):
    t1, t2, cat = map(int, f.readline().split())
    cars.append((t1, t1 + t2, cat))
cars.sort()
kat = [0] * m
count_not_par = 0
for car in cars:
    is_par = False
    for n_par in range(len(a)):
        for i in range(len(a[n_par])):
            if car[2] == n_par and not is_par:
                if a[n_par][i] <= car[0]:
                    a[n_par][i] = car[1]
                    is_par = True
                    break
    if is_par:
        kat[car[2]] += 1
    else:
        count_not_par += 1
i_mx = 0
for i in range(len(kat)):
    if kat[i] >= kat[i_mx]:
        i_mx = i
mx = 0
for i in range(i_mx, len(a)):
    for j in range(len(a[i])):
        if a[i][j] > mx:
            mx = a[i][j]
print(mx, count_not_par)