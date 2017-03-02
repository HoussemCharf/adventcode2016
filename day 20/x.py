with open("input.txt") as f:
    data = f.read()

# MERGE algorithm
def merge(blocked):
    new = []
    current = None
    for block in blocked:
        if current is None:
            current = block
        else:
            if current[1] + 1 >= block[0]:
                current = [current[0], max(block[1], current[1])]
            else:
                new.append(current)
                current = block
    new.append(current)
    return new
       
# Read input as sorted pairs [start, end]
blocked = []
for line in data.splitlines():
    alku,loppu = line.split("-")
    blocked.append([int(alku), int(loppu)])
blocked.sort()

# Merge any overlapping ranges
b = merge(blocked)

# PART 1
print(b[0][1] + 1)

# Count how many are between pieces:
# Note: assumes that last blacklist ends at 4294967295
total = 0
for previous, current in zip(b, b[1:]):
    count = current[0] - previous[1] - 1
    total += count
# PART 2:
print(total)