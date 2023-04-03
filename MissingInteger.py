def solution(A):
    A = set(filter(lambda x: x > 0, A))

    i = 1
    while i in A:
        i += 1
    return i


A = [1, 3, 6, 4, 1, 2]
print(solution(A))
