from fnmatch import fnmatch
from re import fullmatch

for n in range(2023, 10**10, 2023):
    if fullmatch(r'1\d2139\d*4', str(n)):
        print(n, n // 2023)