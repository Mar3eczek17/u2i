def solution(A, B, K):
    # Handle special case where K = 2, because all numbers are divisible by 1
    if K == 1:
        return B - A + 1
    # Find the first multiple of K that is >= A
    first_multiple = ((A + K - 1) // K) * K
    # Find the last multiple of K that is <= B
    last_multiple = (B // K) * K
    # Calculate the number of multiples of K in the range [A..B]
    num_multiples = (last_multiple - first_multiple) // K + 1
    return num_multiples


print(solution(6, 11, 2))
