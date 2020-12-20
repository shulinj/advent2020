

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))


def solve(list):
	dlist = {}
	for x in list:
		dlist[int(x)] = 1


	for x in dlist:
		y = 2020-x
		if y in dlist:
			return x*(2020-x)

if __name__ == "__main__":
    main()