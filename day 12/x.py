import operator as op
import itertools
import copy

class Computer(object):
    
    def __init__(self, a = 0, b = 0, c = 0, d = 0, debug = False):
        self.inst = []
        self.reg = {"a": a, "b": b, "c": c, "d": d}
        self.debug = debug
    
    def run(self):
        self.addr = 0
        inst_max = len(self.inst)
        while 0 <= self.addr < inst_max:
            inst = self.inst[self.addr]
            method = getattr(self, inst[0])
            method(*inst[1:])
    
    def feed(self, args):
        self.inst.append(args)
    
    def cpy(self, x, y):
        if self.debug: print("CPY " + x + " " + y)
        if x.isdigit():
            self.reg[y] = int(x)
        else:
            self.reg[y] = self.reg[x]
        self.addr += 1
    
    def dec(self, x):
        if self.debug: print("DEC " + x)
        self.reg[x] -= 1
        self.addr += 1
        
    def inc(self, x):
        if self.debug: print("INC " + x)
        self.reg[x] += 1
        self.addr += 1
        
    def jnz(self, x, y):
        if self.debug: print("JNZ " + x + " " + y)
        val = None
        if x.isdigit():
            val = int(x)
        else:
            val = self.reg[x]
        if val != 0:
            self.addr += int(y)
        else:
            self.addr += 1

data="""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

computer = Computer()
for line in data.splitlines():
     args = line.replace(",", "").split()
     computer.feed(args)
     
computer.run()
print("TEST 1: Computer(a={}, b={}, c={}, d={})".format(computer.reg["a"], computer.reg["b"], computer.reg["c"], computer.reg["d"]))

with open("input.txt") as file:
    data = file.read()

computer = Computer()
for line in data.splitlines():
     args = line.replace(",", "").split()
     computer.feed(args)
     
computer.run()
print("PART 1: Computer(a={}, b={})".format(computer.reg["a"], computer.reg["b"]))

computer = Computer(c=1)
for line in data.splitlines():
     args = line.replace(",", "").split()
     computer.feed(args)
computer.run()
print("PART 2: Computer(a={}, b={})".format(computer.reg["a"], computer.reg["b"]))