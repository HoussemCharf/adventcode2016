import re 
import time

SAFE = "."
TRAP = "^"

def is_trap(a,b,c):
    return (a == TRAP and b == TRAP and c == SAFE) or (a == SAFE and b == TRAP and c == TRAP) or (a == TRAP and b == SAFE and c == SAFE) or (a == SAFE and b == SAFE and c == TRAP)

def generate_next_row(row):
    padded = SAFE + row + SAFE
    next_row = "".join(TRAP if is_trap(a,b,c) else SAFE for a,b,c in zip(padded, padded[1:], padded[2:]))
    return next_row
        
def generate_maze(initial, height):
    rows = [initial]
    while len(rows) < height:
        next = generate_next_row(rows[-1])
        rows.append(next)
    return "\n".join(rows)

def solve_safes(initial, height):
    maze = generate_maze(initial, height)
    return maze.count(SAFE)

def solve_iteratively_safes(initial, height):
    """
    Solve number of safes tiles with only having one row in memory at time
    """
    row = initial
    total = row.count(SAFE)
    for n in range(1, height):
        row = generate_next_row(row)
        total += row.count(SAFE)
    return total 
    

def run_test(rows):
    for row,next in zip(rows, rows[1:]):
        generated = generate_next_row(row)
        if generated != next:
            raise Exception("Next row generation failed. Expected: {}, actual: {}".format(next, generated))

def run_tests():
    run_test("""..^^.
.^^^^
^^..^""".splitlines())
    run_test(""".^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^""".splitlines())
    num = solve_safes(".^^.^.^^^^", 10)
    if num != 38:
        raise Exception("Failed to count safes. Expected: {}, actual: {}", 38, num)
    
if __name__ == "__main__":
    run_tests()
    
    with open("input.txt") as f:
        initial_line = f.read()
        
    safes = solve_safes(initial_line, 40)
    print("PART 1: Number of safe tiles in maze are: {}".format(safes))
    
    s = time.time()
    safes = solve_iteratively_safes(initial_line, 400000)
    e = time.time()
    print("PART 2: Number of safe tiles in maze are: {} (solved iteratively in {} seconds)".format(safes, e-s))
    
    s = time.time()
    safes = solve_safes(initial_line, 400000)
    e = time.time()
    print("PART 2: Number of safe tiles in maze are: {} (solved with whole maze in memory in {} seconds)".format(safes, e-s))