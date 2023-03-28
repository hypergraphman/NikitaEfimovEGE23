def f(s, c, m, type):
    if s > 33:
        return c % 2 == m % 2
    if c == m:
        return 0
    moves = []
    if type != 1:
        moves.append(f(s + 1, c + 1, m, 1))
    if type != 2:
        moves.append(f(s + 2, c + 1, m, 2))
    if type != 3:
        moves.append(f(s * 2, c + 1, m, 3))
    # moves = [f(s+1, c+1, m), f(s+2, c+1, m), f(s * 2, c+1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for x in range(1, 33):
    for y in range(1, 5):
        if f(x, 0, y, 0):
            print(x, y)
            break