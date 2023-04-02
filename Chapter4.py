# 4.1: Counting elements — O(n + m)
def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


print(counting([2, 3, 6], 8))


# 4.1. Exercise
# 4.2: Swap the elements
def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[j]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False


m = 5
A = [1, 3, 4]
B = [1, 5, 2]
print(slow_solution(A, B, m))


# 4.3: Swap the elements — O(n + m).
def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
    d //= 2
    count = counting(A, m)
    for i in range(n):
        if 0 <= B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False


m = 5
A = [1, 4, 4]
B = [1, 5, 2]
print(fast_solution(A, B, m))
