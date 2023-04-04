def solution(A):
    idx_max = len(A) + 1
    idx_min, avg_min = 0, sum(A[0:2]) / 2
    if idx_max == 2:
        return idx_min

    for idx in range(3, idx_max):
        idx2, idx3 = idx - 2, idx - 3
        avg_tmp2 = sum(A[idx2:idx]) / 2
        avg_tmp3 = sum(A[idx3:idx]) / 3
        idx_min, avg_min = min_check(avg_min, avg_tmp2, idx_min, idx2)
        idx_min, avg_min = min_check(avg_min, avg_tmp3, idx_min, idx3)
    return idx_min


def min_check(avg_min, avg_tmp, idx_min, idx_tmp):
    if avg_tmp < avg_min:
        return idx_tmp, avg_tmp
    else:
        return idx_min, avg_min


A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))
