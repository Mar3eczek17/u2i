def solution(A):
    # Implement your solution here
    if len(A) == 1:
        return A[0]
    A = sorted(A)
    print(A)
    for i in range(0, len(A), 2):
        if i + 1 == len(A):
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]


A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))
