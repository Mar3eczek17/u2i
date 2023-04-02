# 3.4. Exercise
def slow_solution(n):
    result = 0
    for i in range(n):
        for j in range(i + 1):
            result += 1
    return result


n = 100
print(slow_solution(n))


def slow_solution(n):
    result = n * (n + 1) // 2
    return result


n = 100
print(slow_solution(n))
