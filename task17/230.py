def f(s, e, cmd):
    if s == e:
        return 1
    if s > e:
        return 0
    return (f(s + 1, e, 1) if cmd != 1 else 0) + (f(s * 2, e, 2) if cmd != 2 else 0) + (f(s + 3, e, 3) if cmd != 3 else 0)


# print(f(5001, 45789, 0))
# print(f(5001, 5005, 0))

dp = [[] for _ in range(45790)]
dp[5001] = [(1, 0)]
for i in range(5001, 45790):
    if dp[i]:
        for i_cmd in 1, 2, 3:
            s = 0
            for k, cmd in dp[i]:
                if i_cmd != cmd:
                    s += k
            if i_cmd == 1 and i + 1 < 45790:
                dp[i + 1].append((s, i_cmd))
            elif i_cmd == 2 and i * 2 < 45790:
                dp[i * 2].append((s, i_cmd))
            elif i_cmd == 3 and i + 3 < 45790:
                dp[i + 3].append((s, i_cmd))

s = 0
for k, cmd in dp[45789]:
    s += k
print(s)