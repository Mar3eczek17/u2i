"""
Write a function solution that, given integer N, returns the
smallest non-negative integer whose individual digits sum to N.

Examples:
1. Given N=16, the function should return 79. there are many
numbers whose digits sum to 16 (for example: 79,97,808,5551,
22822, ets.). the smallest such number is 79.

2. Given N=19, the sunction should return 199 (the sum of digits
 is 1 + 9 + 9 = 19).

3. Given N=7, the function should return 7.

Assume that:
- N is an integer within the range [0..50].

In your solution, focus on correctness, the performance of your
solution will not be the focus of the assessment.
"""


def solution(N):
    # Implement your solution here
    if N == 0:
        return 0
    for i in range(1, 10 ** 5):
        if sum(int(d) for d in str(i)) == N:
            return i


print(solution(N=7))
