

import re
import itertools 
import md5

data = "pvhmgsws"

def solve(initial):
    m = md5.new()
    m.update(initial)
    newMD5 = m.hexdigest()
    DIR = [[0, 1,"U"], [0, -1,"D"], [-1,0,"L"], [1,0,"R"]]
    queue = [(1,4,newMD5,"")]
    # PART 1
    maxs = -1
    # PART 2
    best = None
    while queue:
        (x,y,salt,seq) = queue[0]
        queue = queue[1:]
        
        for i, dir in enumerate(DIR):
            if salt[i] in "bcdef":
                nx = x+dir[0]
                ny = y+dir[1]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                
                nseq = seq + dir[2]
                if nx == 4 and ny == 1:
                    if not best:
                        best = nseq
                    if len(nseq) > maxs:
                        maxs = len(nseq)
                    continue
                
                m = md5.new()
                m.update(initial)
                m.update(nseq)
                newMD5 = m.hexdigest()

                queue.append((nx, ny, newMD5, nseq))
                
    print("PART 1: {}: {}".format(initial, best))
    print("PART 2: {}: {}".format(initial, maxs))


solve("ulqzkmiv")

solve(data)