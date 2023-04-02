def solution(A):
    n = len(A) + 1
    result = n * (n + 1) // 2

    return result - sum(A)


A = [2, 3, 1, 5]
print(solution(A))
