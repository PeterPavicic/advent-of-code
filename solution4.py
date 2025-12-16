import re


def padMap(map: list[str]) -> list[str]:
    map.insert(0, '.' * columnCount)
    map.append('.' * columnCount)
    padded = [row.center(columnCount + 2, '.') for row in map]
    return(padded)


def checkSurroundings(map: list[str], rowIndex: int, columnIndex: int, max_rolls_of_paper: int=3) -> str:
    # returns . for empty spot, @ for inaccessible toilet paper, x for accessible toilet paper
    if map[rowIndex][columnIndex] == '.':
        return('.')

    TL = map[rowIndex - 1][columnIndex - 1]
    TC = map[rowIndex - 1][columnIndex]
    TR = map[rowIndex - 1][columnIndex + 1]
    CL = map[rowIndex][columnIndex - 1]
    CR = map[rowIndex][columnIndex + 1]
    BL = map[rowIndex + 1][columnIndex - 1]
    BC = map[rowIndex + 1][columnIndex]
    BR = map[rowIndex + 1][columnIndex + 1]

    surroundings = [TL, TC, TR, CL, CR, BL, BC, BR]
    paperCount = sum([x == '@' for x in surroundings])
    if paperCount <= max_rolls_of_paper:
        return('x')
    else:
        return('@')


with open("input4.txt", 'r') as file:
    input_map = file.read()

rows = input_map.split("\n")[:-1]
rowCount = len(rows)
columnCount = len(rows[0])

# padd all around with .
padded_map = padMap(rows)

rowCount += 2
columnCount += 2

new_map = ""

for rowInd in range(1, rowCount - 1):
    for colInd in range(1, columnCount - 1):
        new_map += checkSurroundings(padded_map, rowInd, colInd)
    new_map += '\n'

new_map = new_map[:-1]

# part 1
# print(new_map)
# print(f"The number of forklift-accessible paper rolls is {new_map.count('x')}")

# part 2

current_map = rows
total_removed = 0
round_counter = 1

while True:
    new_map = ""

    padded_map = padMap(current_map)

    for rowInd in range(1, rowCount + 1):
        for colInd in range(1, columnCount + 1):
            new_map += checkSurroundings(padded_map, rowInd, colInd)
        new_map += '\n'

    new_map = new_map[:-1]

    removed_count = new_map.count('x')

    if removed_count == 0:
        break
    
    total_removed += removed_count

    print(f"Round {round_counter}")
    print(f"Removed {removed_count} rolls of paper.\nNew map:")
    print(new_map)

    round_counter += 1
    current_map = re.sub(r"x", '.', new_map).split('\n')


print(f"End map: \n{new_map}")
print(f"Total removed: \n{total_removed}")
