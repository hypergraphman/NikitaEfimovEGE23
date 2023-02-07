def divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


p = 136
while len(divs(p)) != 3:
    p += 1
print(p)