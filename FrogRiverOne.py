def solution(X, A):
    leaf_check, sum_step = [False] * X, 0
    # print(leaf_check)
    # print(sum_step)
    for sec, fall in enumerate(A):
        if(fall > X): continue
        if(not(leaf_check[fall-1])):
            leaf_check[fall-1] = True
            sum_step += 1
            if(sum_step == X): return sec
    return -1


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))
