# greedy search for largest n digit numbers

def find_largest_two_digit_num(num_as_string: str) -> int:
    digits = list(num_as_string)
    digits_int = [int(x) for x in digits]
    first_digit = max(digits_int[:-1])
    first_digit_index = digits_int.index(first_digit)
    second_digit = max(digits_int[(first_digit_index + 1):])

    return(int(f"{first_digit}{second_digit}"))


def find_largest_N_digit_num(num_as_string: str, n: int=12) -> int:
    digits = list(num_as_string)
    digits_int = [int(x) for x in digits]

    answer_digits = []
    for position in range(1, n):
        digits_after = n - position
        largest_digit = max(digits_int[:(-digits_after)])
        largest_digit_index = digits_int.index(largest_digit)
        answer_digits.append(largest_digit)
        digits_int = digits_int[(largest_digit_index + 1):]

    # last digit
    answer_digits.append(max(digits_int))

    return(int(f"{''.join([str(x) for x in answer_digits])}"))


banks = []
with open("input3.txt", 'r') as file:
    for line in file:
        banks.append(line[:-1])


total_joltage_q1 = 0
total_joltage_q2 = 0

for bank in banks: 
    total_joltage_q1 += find_largest_two_digit_num(bank)
    total_joltage_q2 += find_largest_N_digit_num(bank)

# solutions
print(total_joltage_q1)
print(total_joltage_q2)
