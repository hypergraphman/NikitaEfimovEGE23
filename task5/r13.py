def alg(n):
    step1 = f'{n:b}'
    step2 = step1 + str(sum(map(int, step1)) % 2)
    step3 = step2 + str(sum(map(int, step2)) % 2)
    return int(step3, 2)


print(alg(28))
i = 1
while alg(i) <= 77:
    i += 1
print(i)