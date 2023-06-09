def solution(A):
    # Implement your solution here
    left = A[0]
    right = sum(A[1::])
    diff = abs(left - right)

    for p in range(1, len(A)):
        ldiff = abs(left - right)
        if ldiff < diff:
            diff = ldiff
        left += A[p]
        right -= A[p]

    return diff


A = [3, 1, 2, 4, 3]
print(solution(A))
