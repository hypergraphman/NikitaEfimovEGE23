def divs(n):
    r = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return sorted(r)


def is_prime(n):
    return len(divs(n)) == 2


print(divs(100))