import math

def is_simple_silly_number(n: int) -> bool:
    stringified = str(n)
    return(len(stringified) % 2) == 0 and (stringified[:int(len(stringified) / 2)] == stringified[int(len(stringified) / 2):])

def repeats_digits(stringified: str, digit_count: int, times: int):
    startIndices = [x for x in range(0, digit_count, digit_count // times)]
    endIndices = [x for x in range(digit_count // times, digit_count + 1, digit_count // times)]

    startIndex = startIndices[0]
    endIndex = endIndices[0]
    firstSubstring = stringified[startIndex:endIndex]
    for i in range(1, len(startIndices)):
        startIndex = startIndices[i]
        endIndex = endIndices[i]
        currentSubstring = stringified[startIndex:endIndex]
        if currentSubstring != firstSubstring:
            return(False)
    return(True)

def is_silly_number(n: int) -> bool:
    stringified = str(n)
    digit_count = len(stringified)

    for repeat_time in range(2, digit_count + 1):
        if (digit_count % repeat_time == 0) and repeats_digits(stringified, digit_count, repeat_time):
            return(True)

    return(False)


# read input
with open("input2.txt", 'r') as file:
    text = file.read()[:-1]

    # matrix where rows are ranges, first column start, second column end nums
    id_ranges = [x.split('-') for x in text.split(',')]

# id_ranges = [[11,22], 
#              [95,115], 
#              [998,1012], 
#              [1188511880,1188511890], 
#              [222220,222224], 
#              [1698522,1698528], 
#              [446443,446449], 
#              [38593856,38593862], 
#              [565653,565659], 
#              [824824821,824824827], 
#              [2121212118,2121212124]]

simple_silly_numbers = []
all_silly_numbers = []
for subrange in id_ranges:
    start = int(subrange[0])
    end = int(subrange[1])
    for i in range(start, end + 1):
        if is_simple_silly_number(i):
            simple_silly_numbers.append(i)
            all_silly_numbers.append(i)
        elif is_silly_number(i):
            all_silly_numbers.append(i)

print(f"Simple silly numbers: {simple_silly_numbers}")
print(f"All silly numbers: {all_silly_numbers}")

print(f"""Q1: The sum of all simple silly numbers is {sum(simple_silly_numbers)}.
Q2: The sum of all silly numbers is {sum(all_silly_numbers)}.""")
