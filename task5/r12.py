# def avt(n):
#     a1 = n // 100
#     a2 = n // 10 % 10
#     a3 = n % 10
#     d = [a1 * 10 + a2, a2 * 10 + a1,
#          a1 * 10 + a3, a3 * 10 + a1,
#          a3 * 10 + a2, a2 * 10 + a3
#         ]
#     mx = 0
#     mn = 100
#     for el in d:
#         if 10 <= el <= 99:
#             if el > mx:
#                 mx = el
#             if el < mn:
#                 mn = el
#     return mx - mn
from itertools import permutations


def avt(n):
    a = []
    for d1, d2 in permutations(str(n), r=2):
        t = int(d1 + d2)
        if 10 <= t <= 99:
            a.append(t)
    return max(a) - min(a)


i = 100
while avt(i) != 40:
    i += 1
print(i)

# for i in range(100, 1000):
#     if avt(i) == 40:
#         print(i)
#         break
