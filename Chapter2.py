shopping = ['bread', 'butter', 'cheese']
shopping += ['eggs']
print(shopping)
print(len(shopping))


def negative(temperatures):
    N = len(temperatures)
    days = 0
    for i in range(N):
        if temperatures[i] < 0:
            days += 1
    return days


temperatures = [25, 42, -10, -5, 0, -10, 15, 20, 30]
print(negative(temperatures))


# Negative air temperature — simplified.
def negative(temperatures):
    days = 0
    for i in temperatures:
        if i < 0:
            days += 1
    return days


temperatures = [25, 42, -10, -5, 0, -10, 15, 20, 30]
print(negative(temperatures))


# Given array A consisting of N integers, return the reversed array
def reverse(A):
    A.reverse()
    return A


A = [1, 15, 2, 88, 66, 94, 51, 2, 7, 9]
print(reverse(A))
