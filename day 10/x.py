import re, collections


bot = collections.defaultdict(list)
output = collections.defaultdict(list)


with open('input.txt') as fp:
    instructions = fp.read().splitlines()


pipeline = {}
for line in instructions:
    if line.startswith('value'):
        n, b = map(int,re.findall(r'-?\d+', line))
        bot[b].append(n)
    if line.startswith('bot'):
        who, n1, n2 = map(int,re.findall(r'-?\d+', line))
        t1, t2 = re.findall(r' (bot|output)', line)
        pipeline[who] = (t1,n1),(t2,n2)


while bot:
    for k,v in dict(bot).items():
        if len(v) == 2:
            v1, v2 = sorted(bot.pop(k))
            if v1==17 and v2==61: print(k)
            (t1,n1),(t2,n2) = pipeline[k]
            eval(t1)[n1].append(v1)
            eval(t2)[n2].append(v2)


a,b,c = (output[k][0] for k in [0,1,2])
print(a*b*c)