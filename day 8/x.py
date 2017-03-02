import re, numpy as np

def display(s):
    print('\n'.join(''.join('X' if p else ' '  for p in row) for row in s))

def run(width, height, lines):
    s = np.zeros((height, width), dtype=bool)
    for line in lines:
        p = re.split(r'[ =]', line)
        if p[0] == 'rect':
            w, h = map(int, p[1].split('x'))
            s[:h, :w] = True
        elif p[0] == 'rotate':
            if p[1] == 'row':
                cy, n = int(p[3]), int(p[5])
                s[cy] = np.roll(s[cy], n)
            else:
                cx, n = int(p[3]), int(p[5])
                s[:,cx] = np.roll(s[:,cx], n)
    return s

answer = run(50, 6, open('input.txt'))
print('Answer #1:', np.sum(answer))
print('Answer #2:')
display(answer)