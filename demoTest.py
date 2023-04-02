# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A = set(filter(lambda x: x > 0, A))

    # Find the smallest missing positive integer
    i = 2
    while i in A:
        i += 1

    print(i)


A = [1, 3, 6, 4, 1, 2]
B = [1, 2, 3]
solution(A)
solution(B)
