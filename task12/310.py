lst = set()
for i in range(204):
    s = '1' * i + '2' + '1' * (203 - i)
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)
    lst.add((len(s), s))
print(max(lst))
print(lst)