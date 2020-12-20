

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(int(line))
	f.close()

	print(solve(lines))


def solve(list):
	dlist = {}
	for i in range(len(list)):
		for j in range(len(list)):
			if i == j:
				continue
			x = list[i]
			y = list[j]
			if 2020-x-y < 0:
				continue
			dlist[2020-x-y] = [x, y]

	for x in list:
		if x in dlist:
			return x*dlist[x][0]*dlist[x][1]

if __name__ == "__main__":
    main()