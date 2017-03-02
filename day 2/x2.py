with open("input.txt", "r") as fp:
    data = fp.read().strip()

keypad = [
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "]
]

position = (2, 0)
movements = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}

result = ""
for line in data.split("\n"):
    for instruction in line:
        next_movement = movements[instruction]
        new_position = (position[0] + next_movement[0], position[1] + next_movement[1])
        if new_position[0] < 0 or new_position[0] > 4 or new_position[1] < 0 or new_position[1] > 4 or keypad[new_position[0]][new_position[1]] == " ":
            continue
        else:
            position = new_position
    result += keypad[position[0]][position[1]]

print result