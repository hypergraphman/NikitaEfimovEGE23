def ntp(n, p):
    alf = '0123456789ABCDEF'
    r = ''
    while n != 0:
        r = alf[n % p] + r
        n //= p
    return r


for z in range(10):
    for y in ['', '00', '000'] + list(range(0, 1000)):
        n = f'3{z}458{y}3'
        t = ntp(int(n), 9)
        f = True
        for x in range(len(t) - 1):
            if t[x] < t[x+1]:
                f = False
        if f:
            print(n, sum(map(int, t)), t)