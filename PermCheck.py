def solution(A):
    if min(A) == 1 and max(A) == len(A) == len(set(A)): return 1
    return 0



print(solution([4,2,1,3]))
print(solution([4,1,3]))
print(solution([4,2,1,4]))
print(solution([4,2,5,3]))