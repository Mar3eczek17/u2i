def solution(A):
    zeros = 0
    passing = 0
    for i in A:
        if i == 0:
            zeros += 1
        else:
            passing += zeros
    if passing > 1000000000:
        return -1
    else:
        return passing



A = [0,1,0,1,1]
print(solution(A))