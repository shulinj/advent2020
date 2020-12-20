def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines, 1, 1) * solve(lines, 3, 1) * solve(lines, 5, 1) * solve(lines, 7, 1) * solve(lines, 1, 2))

def solve(lines, right, down):
	# build map
	m = []
	for line in lines:
		m.append(list(line))

	count = 0

	row = down
	column = right
	for i, line in enumerate(m):
		if i == 0 or i%row != 0:
			continue

		rlen = len(line) - 1 # newline

		if line[column%rlen] == "#":
			count += 1
		column +=right

	return count

if __name__ == "__main__":
    main()