import re, itertools
swapl = r"swap letter (.) with letter (.)"
swapp = r"swap position (.) with position (.)"
rotl = r"rotate left (\d+) steps?"
rotr = r"rotate right (\d+) steps?"
rot = r"rotate based on position of letter (.)"
rev = r"reverse positions (.) through (.)"
move = r"move position (.) to position (.)"

def scramle(passwd, data):
    passwd = list(passwd)
    for line in data.splitlines():
        f = False
        for a,b in re.findall(swapp, line):
            a = int(a)
            b = int(b)
            passwd[a], passwd[b] = passwd[b], passwd[a]
            f = True
        for a,b in re.findall(swapl, line):
            for i,c in enumerate(passwd):
                if c == a:
                    passwd[i] = b
                elif c == b:
                    passwd[i] = a
            f = True
        for r in re.findall(rotl, line):
            r = int(r) % len(passwd)
            passwd = passwd[r:] + passwd[:r]
            f = True
        for r in re.findall(rotr, line):
            r = int(r) % len(passwd)
            passwd = passwd[-r:] + passwd[:-r] 
            f = True
        for c in re.findall(rot, line):
            i = passwd.index(c)
            if i >= 4:
                i += 2
            else:
                i += 1
            i = i % len(passwd)
            passwd = passwd[-i:] + passwd[:-i]
            f = True 
        for a,b in re.findall(rev, line):
            a = int(a)
            b = int(b)
            passwd = passwd[:a] + list(reversed(passwd[a:b+1])) + passwd[b+1:]
            f = True
        for a,b in re.findall(move, line):
            a = int(a)
            b = int(b)
            c = passwd[a]
            del passwd[a]
            passwd.insert(b,c)
            f = True
        if not f:
            print("Not modified")
        #print(line, passwd)
    return "".join(passwd)

pw = scramle("abcde", """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""")
print("Test: {}".format(pw))

with open("input.txt") as f:
    data = f.read()
passwd = "abcdefgh"

# PART 1
pw = scramle(passwd, data)
print("Part 1: {}".format(pw))
      
# PART 2
goal = "fbgdceah"
for s in itertools.permutations(goal):
    mut = scramle(s, data)
    if mut == goal:
        print("Part 2: {}".format("".join(s)))
        break