def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

def solve(lines):
	# build map
	m = []
	for line in lines:
		m.append(list(line))

	count = 0
	column = 3
	for i, row in enumerate(m):
		if i == 0:
			continue

		rlen = len(row) - 1 # newline

		print("".join(testrow), column%rlen, row[column%rlen])

		if row[column%rlen] == "#":
			count += 1
		column +=3

	return count



if __name__ == "__main__":
    main()