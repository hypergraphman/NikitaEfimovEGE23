from re import fullmatch
from itertools import product

# for i in range(279, 10**11, 279):
#     if fullmatch(r'78\d56[13579]*321', str(i)):
#         print(i, i // 279)

all_num = ([''] +
    list(map(''.join, product('13579', repeat=1))) +
    list(map(''.join, product('13579', repeat=2))) +
    list(map(''.join, product('13579', repeat=3))))

res = []
for x in range(10):
    for y in all_num:
        n = int(f'78{x}56{y}321')
        if n % 279 == 0:
            res.append((n, n // 279))
res.sort()
print(*res, sep='\n')