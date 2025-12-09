current = 50 
q1_counter = 0
q2_counter = 0
# solution = [1, 2, 5, 7, 8, 9, 12, 13]

with open("input1.txt", 'r') as file:
    print("Start at 50")

    for i, line in enumerate(file):
        print(line[:-1])
        direction = line[0]
        magnitude = int(line[1:])

        if direction == 'L': # subtract
            old = current
            current = (current - magnitude) % 100
            q2_counter += (current + magnitude) // 100 + int(current == 0) - int(old == 0) # 2nd question
        elif direction == 'R': # add
            q2_counter += (current + magnitude) // 100 # 2nd question
            current = (current + magnitude) % 100
        else:
            raise Exception("This was not supposed to happen")

        # q2_counter += int(current == 0) # 1st question
        # print(f"Currently at: {current}. Counter: {q2_counter}. Correct count: {solution[i]}")
        print(f"Currently at: {current}. Counter: {q2_counter}.")
        q1_counter += int(current == 0)

print(f"""
The final counts are:
Q1: {q1_counter}
Q2: {q2_counter}
""")
