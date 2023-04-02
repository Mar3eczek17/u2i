def solution(N):
    binary = bin(N)[2:]  # convert to binary and remove the '0b' prefix
    max_gap = 0
    current_gap = 0
    counting = False

    for digit in binary:
        if digit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
            current_gap = 0
            counting = True
        elif counting:
            current_gap += 1

    return max_gap


# N is an integer within the range [1..2,147,483,647].
N = 9
print(solution(N))
