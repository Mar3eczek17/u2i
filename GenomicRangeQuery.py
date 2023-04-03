def solution(S, P, Q):
    d = {"A": 0, "C": 1, "G": 2, "T": 3}
    n = len(S)
    pref = [[0, 0, 0, 0]] * (n + 1)
    for i in range(0, n):
        pref[i] = [x for x in pref[i - 1]]
        pref[i][d[S[i]]] += 1
    lst = []
    for i in range(0, len(P)):
        if Q[i] == P[i]:
            lst.append(d[S[P[i]]] + 1)
        else:
            x = 0
            while x < 4:
                if pref[Q[i]][x] - pref[P[i] - 1][x] > 0:
                    lst.append(x + 1)
                    break
                x += 1
    return lst


S, P, Q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
print(solution(S, P, Q))
