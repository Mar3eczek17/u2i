def solution(N):
    br = str(bin(N))[2:]
    br_group = False
    br_highest = 0
    bin_zero_counter = 0
    for char in br:
        if char == '1':
            if br_highest < bin_zero_counter:
                br_highest = bin_zero_counter
            br_group = True
            bin_zero_counter = 0
        elif br_group:
            bin_zero_counter += 1
    return br_highest



# N is an integer within the range [1..2,147,483,647].
N = 32
print(solution(N))
