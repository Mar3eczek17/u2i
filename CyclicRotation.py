def solution(A, K):
    # Implement your solution here
    print([A[-1]])
    print(A[:-1])
    print([A[-1]] + A[:-1])
    def rotation(A):
        return [A[-1]] + A[:-1]

    if len(A) == 0:  # inf loop
        return A

    for i in range(K):
        A = rotation(A)
    return A


A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))
