import sys
from heapq import heappush, heappop

class G:
	id2idx = {}
	idx2id = [0]
	idx = 1
	edge = [[]]

DISTANCE_MULTIPLE = 100

g = G()

def get_idx(id):
	i = g.id2idx.get(id, 0)
	if i == 0:
		i = g.idx
		g.id2idx[id] = i
		g.idx2id.append(id)
		g.edge.append([])
		g.idx = g.idx + 1
	return i

def add_edge(start, end, distance):
	s = get_idx(start)
	e = get_idx(end)
	g.edge[s].append((e, distance))

# 123.45 -> 12345
# 123.4599 -> 12345
# 123 -> 12300
# 123.4 -> 12340
# .5 -> 50
def stof100(s):
	result = 0
	place = 2
	is_decimal_place = False
	for ch in s:
		if ch == '.':
			is_decimal_place = True
			continue
		result *= 10
		result += ord(ch) - ord('0')
		if is_decimal_place:
			place -= 1
			if place == 0:
				break
	while place > 0:
		result *= 10
		place -= 1
	return result


def load():
	sys.stdin.readline()
	for line in sys.stdin.readlines():
		line = line.strip()
		data = line.split(",")
		# println(data)
		s = int(data[2])
		e = int(data[3])
		d = stof100(data[5])
		if is_debug:
			print(f"line: {line} s: {s} e: {e} D: {d}")
		add_edge(s, e, d)

def dijkstra(start, end):
	s = get_idx(start)
	e = get_idx(end)

	MAX_INT32 = 2147483647 # 2^31-1 - this is not the max value of python Number but good for this benchmark
	size = g.idx
	d = [MAX_INT32] * size
	prev = [0] * size

	queue = []
	heappush(queue, (0, s))

	visited = 0
	while len(queue) > 0:
		distance, here = heappop(queue)
		if distance > d[here]:
			continue
		visited += 1
		if is_debug:
			print(f"visiting: {here} distance: {distance}")
		for to, weight in g.edge[here]:
			w = distance + weight
			if w < d[to]:
				prev[to] = here
				d[to] = w
				heappush(queue, (w, to))
	print("visited:", visited)

	n = e
	result = [g.idx2id[n]]

	while d[n] != MAX_INT32 and n != s and n != 0:
		n = prev[n]
		result.append(g.idx2id[n])

	return int(d[e] / DISTANCE_MULTIPLE), result

def main():
	count = int(sys.argv[1])
	global is_debug
	is_debug = len(sys.argv) > 2 and sys.argv[2] == "debug"

	load()
	print("loaded nodes:", g.idx)

	route = []
	for i in range(1,count+1):
		s = g.idx2id[i*1000]
		distance, route = dijkstra(s, g.idx2id[1])
		print("distance:", distance)

	result = "route: "
	for id in route:
		result = result + str(id) + " "
	print(result)

main()
