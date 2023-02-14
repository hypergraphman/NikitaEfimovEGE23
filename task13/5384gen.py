g = {
    'A': 'B',
    'B': 'VZ',
    'V': 'G',
    'G': 'ZYD',
    'Z': 'AV',
    'Y': 'AZ',
    'D': 'YAEK',
    'E': 'IA',
    'I': 'A',
    'K': 'E'
}


def path(s, e, p):
    if len(p) > 1 and s == e:
        paths.add(p)
        return None
    if len(set(p)) < len(p):
        return None
    for v in g[s]:
        path(v, e, p + v)


paths = set()
path('Z', 'Z', 'Z')
print(len(paths))
