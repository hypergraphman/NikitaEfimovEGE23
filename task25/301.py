from re import fullmatch


def is_prime(n):
    if n == 1:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


for i in range(1, 10**5):
    if is_prime(i) and fullmatch(r'1\d2\d*0\d*2\d1', str(i**2)):
        print(i ** 2, i)
