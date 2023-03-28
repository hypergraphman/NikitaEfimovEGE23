from collections import defaultdict

procs = defaultdict(int)
for line in open('22-45.txt').readlines():
    id, t, relations = line.split('\t')
    t = int(t)
    relations = relations.strip('"').split('; ')
    if relations[0] == '0':
        procs[id] = t
    else:
        procs[id] = t + max(map(lambda x: procs[x], relations))
print(max(procs.values()))