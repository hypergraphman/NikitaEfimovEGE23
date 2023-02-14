g = {
    'A': 'B',
    'B': 'V',
    'V': 'GYE',
    'G': 'ED',
    'Z': 'DKL',
    'Y': 'NZ',
    'D': 'YEK',
    'E': 'Y',
    'L': 'M',
    'K': 'L',
    'M': 'NAZ',
    'N': 'ABVZ'
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
path('Y', 'Y', 'Y')
print(len(paths))
