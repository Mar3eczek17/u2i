def solution(N, A):
    res = [0] * N
    max_val = 0
    last_update = 0
    n1 = N + 1
    for i in A:
        if i < n1:
            if res[i - 1] < last_update:
                res[i - 1] = last_update

            res[i - 1] += 1

            if res[i - 1] > max_val:
                max_val = res[i - 1]
        else:
            last_update = max_val

    for i in range(len(res)):
        if res[i] < last_update:
            res[i] = last_update

    return res


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))
