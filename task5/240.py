# sposob 1
n = 123
r = ''
while n > 0:
    d = n % 10
    r = f'{d:b}'.rjust(4, '0') + r
    n //= 10
# 000100100011
print(r)

# sposob 2
n = 123
r = ''
for d in str(n):
    r += f'{int(d):b}'.rjust(4, '0')
print(r)
