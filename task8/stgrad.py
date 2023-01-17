from itertools import product

alf = 'vavavava'
k = 0
for word in product(alf, repeat=6):
    word = ''.join(word)
    if word.count('v') < word.count('a'):
        k += 1
print(k)