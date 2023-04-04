# 6.1. Selection sort
def selectionSort(A):
    n = len(A)
    for k in range(n):
        minimal = k
        for j in range(k + 1, n):
            if A[j] < A[minimal]:
                minimal = j
        A[k], A[minimal] = A[minimal], A[k]  # swap A[k] and A[minimal]
    return A


A = [5, 2, 8, 14, 1, 16]
print(selectionSort(A))

# 6.2. Counting sort
def countingSort(A, k):
    n = len(A)

