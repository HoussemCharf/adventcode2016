with open("input.txt") as f:
    data = f.read()

import itertools
import re
import copy
        
def show(ef, floors, types):
    for f in range(3,-1,-1):
        p = []
        p.append("F{}".format(f+1))
        p.append("E " if ef == f else ". ")
        for type in types:
            p.append(type + "G" if type in floors[f]["G"] else ". ")
            p.append(type + "M" if type in floors[f]["M"] else ". ")
        print(" ".join(p))
    
def valid_state(floors):
    for floor in floors:
        for type in floor["M"]:
            if floor["G"] and type not in floor["G"]: 
                return False
    return True

def generate_moves(current, dir):
    for generator_size in range(0,3):
        for micro_size in range(1 if generator_size == 0 else 0,3-generator_size):
                for dG in itertools.combinations(current["G"], generator_size):
                    for dM in itertools.combinations(current["M"], micro_size):
                        yield (dir, dG, dM)

def moves(ef, floors, types):
    current = floors[ef]
    if ef < 3:
        next = floors[ef + 1]
        for move in generate_moves(current, +1):
            yield move
    if ef > 0:
        next = floors[ef - 1]
        for move in generate_moves(current, -1):
            yield move

def print_states(states, types):
    cur_f = None
    cur_l = None
    for s in states:
        f = [{"G":[], "M":[]} for x in range(4)]
        e = int(s[0])
        for c in s:
            if c.isdigit():
                cur_f = int(c)
            elif c == 'm':
                cur_l = f[cur_f]["M"]
            elif c == 'g':
                cur_l = f[cur_f]["G"]
            else:
                cur_l.append(c)
        show(e, f, types)
        print("\n")

def unpack(state):
    current_floors = [{"G":[], "M":[]} for x in range(4)]
    current_floor = int(state[0])
    floor = None
    for c in state:
        if c.isdigit():
            floor = int(c)
        elif c == 'm':
            cur_l = current_floors[floor]["M"]
        elif c == 'g':
            cur_l = current_floors[floor]["G"]
        else:
            cur_l.append(c)
    return current_floor, current_floors
            
def pack(current_floor, current_floors):
    # This is full state as one string
    full = "{}".format(current_floor) + "".join("{}{}{}".format(f, "g" + "".join(sorted(stuff["G"])) if stuff["G"] else "", "m" + "".join(sorted(stuff["M"])) if stuff["M"] else "") for f,stuff in enumerate(current_floors))
    
    # This is equivalent state config
    # Order all types with (floorG, floorM), then sort then and prepend elevator floor
    pos = {}
    for index,stuff in enumerate(current_floors):
        for prop in ("G", "M"):
            for item in stuff[prop]:
                if item not in pos:
                    pos[item] = {}
                pos[item][prop] = index
    pos = sorted([(p["G"], p["M"]) for p in pos.values()])
    equivalent = "{}{}".format(current_floor,pos)
    return full, equivalent

# BFS for solving
def solve_gen(current_floor, current_floors, types, steps = 0):
    states = set()
    queue = list()
    
    state, eq_state = pack(current_floor, current_floors)
    states.add(eq_state)
    queue.append((state,0,[state]))
     
    while queue:
        state, queue = queue[0], queue[1:]
        state, steps, prev = state
        current_floor, current_floors = unpack(state)

        # Is this solution?
        if current_floor == 3 and len(types) == len(current_floors[current_floor]["M"]) == len(current_floors[current_floor]["G"]):
            #show(current_floor, current_floors, types)
            sol = list(prev)
            sol.append(state)
            #print("Solved with {} steps, history:".format(steps))
            #print_states(sol, types)
            return steps

        
        M = moves(current_floor, current_floors, types) 
        for ed, Gd, Md in M:
            floors = copy.deepcopy(current_floors)
            ef = current_floor
            floors[ef]["G"] = [type for type in floors[ef]["G"] if type not in Gd]
            floors[ef]["M"] = [type for type in floors[ef]["M"] if type not in Md]
            ef = ef+ed
            floors[ef]["G"] += Gd
            floors[ef]["M"] += Md
            floors[ef]["G"].sort()
            floors[ef]["M"].sort()

            # Validate the move
            if not valid_state(floors):
                continue
            thestate, eq_thestate = pack(ef, floors)
            if eq_thestate not in states:
                states.add(eq_thestate)
                
                sol = list(prev)
                sol.append(thestate)
                queue.append((thestate,steps+1,sol))

def solve(current_floor, current_floors, types):
    # If we always move 2 up and 1 down.
    # Then this is the optimum solution
    distance = sum((len(current_floors[x]["G"]) + len(current_floors[x]["M"])) * 2 * (3-x) for x in range(3)) - 3*(len(current_floors)-1)
    print("The lower bound for the solution is: {}".format(distance))
 
    best = solve_gen(current_floor, current_floors, types)
    print("Best solution: {}".format(best))

def test_case():
    test_types = ("H", "L")
    test_floors = [
        {"G":[], "M":["H", "L"]},
        {"G":["H"], "M":[]},
        {"G":["L"], "M":[]},
        {"G":[], "M":[]},
    ]
    print("Test run")
    show(0, test_floors, test_types)
    solve(0, test_floors, test_types)

def as_symbol(word, symbols):
    if word in symbols:
        symbol = symbols[word]
    else:
        for c in word:
            if c.upper() not in symbols.values():
                symbol = symbols[word] = c.upper()
                break
    return symbol

def parse_input(data):
    reg = r"(\w+) generator|a (\w+)-compatible microchip"
    floors = [{"G":[], "M":[]} for x in range(4)]
    symbols = dict()

    for floor,line in enumerate(data.splitlines()):
        for generator,microchip in re.findall(reg, line):
            if generator:
                s = as_symbol(generator, symbols)
                floors[floor]["G"].append(s)
            if microchip:
                s = as_symbol(microchip, symbols)
                floors[floor]["M"].append(s)

    return symbols, floors

def part2(data):
    print("PART 2:")
        
    symbols, floors = parse_input(data)
    # Missing from original input
    e = as_symbol('elerium', symbols)
    d = as_symbol('dilithium', symbols)

    floors[0]["G"].extend([e,d])
    floors[0]["M"].extend([e,d])
    
    types = sorted([item[0] for stuff in floors for item in stuff["G"]])

    print(symbols)
    show(0, floors, types)
    solve(0, floors, types)

def part1(data):
    print("PART 1:")
    
    symbols, floors = parse_input(data)
    types = sorted([item[0] for stuff in floors for item in stuff["G"]])
    
    print(symbols)
    show(0, floors, types)
    solve(0, floors, types)
part1(data)
part2(data)

part1("""The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.""")
part2("""The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.""")