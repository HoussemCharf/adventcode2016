import itertools, re

with open("input.txt") as f:
	data = f.read()

def distance(maze, a, b):
	L = len(maze)
	width = maze.index("\n") + 1
	goes = [-width, -1, 1, width]
	start = maze.index(a)
	queue = [(start, 0)]
	visited = set()
	visited.add(start)
	while queue:
		state, steps = queue[0]
		queue = queue[1:]
		for n in goes:
			next = state+n
			if 0 <= next < L and maze[next] != "#" and next not in visited:
				visited.add(next)
				if maze[next] == b:
					return steps + 1
				else:
					queue.append((next, steps+1))

def find_numbers(maze):
	n = []
	t = 0
	while t < 9:
		try:
			maze.index(str(t))
			n.append(t)
		except:
			pass
		t += 1
	return n

def connect(G, n, R, dist = 0, visited=None, back=False):
	if visited is None:
		visited = list()
		visited.append(n)
	min_dist = 10000
	for m in R:
		if m not in visited and n != m:
			vis = list(visited)
			vis.append(m)

			d = G[(n,m)]
			total = dist + d
			if len(vis) == len(R):
				plus = G[(m,0)] if back else 0
				return total+plus, vis
			else:
				d, o = connect(G, m, R, total, vis, back)
				if d < min_dist:
					min_dist = d
					min_order = o
	return min_dist, min_order

def solve(maze):
	t = find_numbers(maze)
	t = max(t)+1
	d = dict()
	for i in range(0, t):
		for j in range(i+1, t):
			dist = distance(maze, str(i), str(j))
			d[(i,j)] = dist
			d[(j,i)] = dist
	# Shortest connecting graph
	v,o = connect(d, 0, range(0,t))
	print(o)
	print(v)
	v,o = connect(d, 0, range(0,t), back=True)
	print(o)
	print(v)

def test():
	maze = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""
	print(distance(maze, "0", "4"))
	print(distance(maze, "4", "1"))
	print(distance(maze, "1", "2"))
	print(distance(maze, "2", "3"))

if __name__ == "__main__":
	test()
	solve(data)