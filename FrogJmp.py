def solution(X, Y, D):
    # Implement your solution here
    distance = Y - X
    jumps = distance // D
    if distance % D != 0:
        jumps += 1
    return jumps


X = 10
Y = 85
D = 30
print(solution(X, Y, D))
