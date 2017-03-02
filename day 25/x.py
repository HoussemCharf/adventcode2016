import itertools, re

with open("input.txt") as f:
	data = f.read()

class Computer(object):
    
    def __init__(self, a = 0, b = 0, c = 0, d = 0, debug = False):
        self.inst = []
        self.reg = {"a": a, "b": b, "c": c, "d": d}
        self.debug = debug
        self.debug_tgl = False
        self.signals = []
    
    def run(self, m):
        self.addr = 0
        inst_max = len(self.inst)
        while 0 <= self.addr < inst_max:
            inst = self.inst[self.addr]
            method = getattr(self, inst[0])
            method(*inst[1:])
            if len(self.signals) == m:
            	return
    
    def feed(self, args):
        self.inst.append(args)
    
    def mulplus(self, x, y, z):
        if self.debug: print("MUL " + x + " " + y + " " + z)
        self.reg[z] += self.reg[x] * self.reg[y]
        self.addr += 1

    def cpy(self, x, y):
        if self.debug: print("CPY " + x + " " + y)
        if self.isnumber(x):
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
        if self.isnumber(x):
            val = int(x)
        else:
            val = self.reg[x]
        if val != 0:
            if self.isnumber(y):
                self.addr += int(y)
            else:
                self.addr += self.reg[y]
        else:
            self.addr += 1

    def isnumber(self, a):
        try:
            int(a)
            return True
        except Exception as e:
            return False

    def nop(self):
    	self.addr += 1
            
    def tgl(self, x):
        if self.debug: print("TGL " + x)
        if self.debug_tgl: print("TGL " + x + " with a as " + str(self.reg["a"]))
        if x.isdigit():
            val = int(x)
        else:
            val = self.reg[x]
        ptr = self.addr + val
        if self.debug_tgl: print("Addr: " + str(val) + " as " + str(ptr))
        if 0 <= ptr < len(self.inst):
            inst = self.inst[ptr][0]
            if inst == "inc":
                self.inst[ptr][0] = "dec"
                if self.debug_tgl: print("inc -> dec")
            elif inst == "dec":
                self.inst[ptr][0] = "inc"
                if self.debug_tgl: print("dec -> inc")
            elif inst == "tgl":
                self.inst[ptr][0] = "inc"
                if self.debug_tgl: print("tgl -> inc")
            elif inst == "cpy":
                self.inst[ptr][0] = "jnz"
                if self.debug_tgl: print("cpy -> jnz")
            elif inst == "jnz":
                self.inst[ptr][0] = "cpy"
                if self.debug_tgl: print("jnz -> cpy")
        self.addr += 1
    def out(self, x):
    	if self.isnumber(x):
    		self.signals.append(x)
    	else:
    		self.signals.append(self.reg[x])
    	self.addr += 1

def check_with_longer(a):
	computer = Computer(a=a)
	for line in data.splitlines():
		args = line.replace(",", "").split()
		computer.feed(args)
	computer.run(100)
	every_second_same1 = all(a == b for a,b in zip(computer.signals[0::2], computer.signals[2::2]))
	every_second_same2 = all(a == b for a,b in zip(computer.signals[1::2], computer.signals[3::2]))
	different_in_turns = all(a != b for a,b in zip(computer.signals, computer.signals[1:]))
	print("a={}, signals={}".format(a,computer.signals))
	return every_second_same1 and every_second_same2 and different_in_turns

def solve(data):
	for a in range(1,1000):
		computer = Computer(a=a)
		for line in data.splitlines():
	   		args = line.replace(",", "").split()
			computer.feed(args)
		computer.run(10)
		#print("a={}, signals={}".format(a,computer.signals))
		if computer.signals == [0,1,0,1,0,1,0,1,0,1]:
			if check_with_longer(a):
				print("Solved with A = {}".format(a))
				return
		if computer.signals == [1,0,1,0,1,0,1,0,1,0]:
			if check_with_longer(a):
				print("Solved with A = {}".format(a))
				return

if __name__ == "__main__":
	if True: # Hand coded optimization
		data = data.splitlines() 
		data[3] = "mulplus b c d"
		data[4] =  "cpy 0 c"
		data[5] =  "cpy 0 b"
		data[6] =  "nop"
		data[7] =  "nop"
		data = "\n".join(data)

	solve(data)