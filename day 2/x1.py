with open("input.txt","r") as f:
  data = f.read().strip()
mapa = [["1","2","3"],
       ["4","5","6"],
       ["7","8","9"]
       ]
intia =(1,1) 
movements = {"U": (-1, 0),    "R": (0, 1),    "D": (1, 0),    "L": (0, -1)}
result = ""
for line in data.split("\n"):
    for instruction in line:
        next_Move = movements[instruction]
        new_pos = (intia[0]+ next_Move[0],intia[1]+ next_Move[1])
        if new_pos[0] < 0 or new_pos[0] > 2 or new_pos[1] < 0 or new_pos[1] > 2:
            continue
        else:
          intia = new_pos
    result += mapa[intia[0]][intia[1]]

print result

