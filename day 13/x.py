input = 1350

def wall(x,y):
    a = x*x + 3*x + 2*x*y + y + y*y + 1350
    nfo = sum(1 for c in bin(a) if c == "1")
    return (nfo % 2) == 1

def generate_maze(w=100,h=100):
    m = [[wall(x,y) for x in range(w)] for y in range(h)]
    return m

def print_maze(m,loc,target,visited=set()):
    for y,r in enumerate(m):
        n = "".join("O" if (x,y) == loc or (x,y) in visited else ("T" if (x,y) == target else ("#" if b else ".")) for x,b in enumerate(r))
        print(n)


def edges(m, pos):
    nn = [[-1,0], [1,0], [0,-1], [0,1]]
    for n in nn:
        x = pos[0]+n[0]
        y = pos[1]+n[1]
        if x >= 0 and y >= 0 and y < len(m) and x < len(m[y]) and m[y][x] == False:
            yield (x,y)
            
def bfs(m, loc, target, max=None):
    queue = []
    queue.append((0, loc))
    visited = set()
    visited.add(loc)
    while queue:
        steps, pos = queue[0]
        queue = queue[1:]
        for neigh in edges(m, pos):
            if neigh not in visited:
                visited.add(neigh)
                if max is None or steps < max - 1:
                    queue.append((steps+1, neigh))
                    if neigh == target:
                        print("steps: {}".format(steps+1))
    #print_maze(m, loc, target, visited)
    if max is not None:
        print(len(visited))


loc = 1,1
target = 31,39

m = generate_maze()
print_maze(m,loc,target)
print()

bfs(m, loc, target)
bfs(m, loc, target, max=50)