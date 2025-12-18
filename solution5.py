# returns -1 if not fresh
def isFresh(ingredient: int, fresh_indices: list[list[int]]) -> int:
    freshness = [fresh_range[0] <= ingredient and ingredient <= fresh_range[1] for fresh_range in fresh_indices]
    if any(freshness):
        return(freshness.index(True))
    else:
        return(-1)

with open("input5.txt", 'r') as file:
    text = file.read()[:-1]

lines = text.split("\n")

# print(lines)

separatorIndex = lines.index("")

# fresh ranges 
fresh_ranges = []
ingredients = []
for i in range(separatorIndex):
    fresh_ranges.append(list(map(int, lines[i].split("-"))))

for i in range(separatorIndex + 1, len(lines)):
    ingredients.append(int(lines[i]))

fresh_ingredient_count = sum([isFresh(ingredient, fresh_ranges) != -1 for ingredient in ingredients])

print(f"The number of fresh ingredients is: {fresh_ingredient_count}")

fresh_ranges.sort()

unique_fresh_ID_ranges = [fresh_ranges[0]]

for fresh_range in fresh_ranges[1:]:
    fresh_range_start = fresh_range[0]
    fresh_range_end = fresh_range[1]

    # check first digit
    first_digit_freshness = isFresh(fresh_range_start, unique_fresh_ID_ranges)

    # first digit already contained
    if first_digit_freshness != -1:
        contained_in = first_digit_freshness
        # second digit also contained
        if isFresh(fresh_range_end, unique_fresh_ID_ranges) != -1:
            continue
        # second digit not yet contained
        else:
            # expand maximum
            unique_fresh_ID_ranges[contained_in][1] = fresh_range_end

    # first digit not yet contained
    else:
        second_digit_freshness = isFresh(fresh_range_end, unique_fresh_ID_ranges)

        # second digit already contained
        if second_digit_freshness != -1:
            #expand minimum
            unique_fresh_ID_ranges[second_digit_freshness][0] = fresh_range_start
        else:
            # second digit not yet contained
            # this points to disjoint fresh ranges
            unique_fresh_ID_ranges.append(fresh_range)


total_fresh_ID_count = 0
for fresh_ID_ranges in unique_fresh_ID_ranges:
    rangeStart = fresh_ID_ranges[0]
    rangeEnd = fresh_ID_ranges[1]
    rangeLength = rangeEnd + 1 - rangeStart
    total_fresh_ID_count += rangeLength

print(f"The number of fresh ingredient IDs is: {total_fresh_ID_count}")
print(unique_fresh_ID_ranges)



