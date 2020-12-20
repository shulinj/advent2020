
def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

def column(str):
	b = ""
	for x in str:
		if x == 'L':
			b = b + '0'
		else:
			b = b + '1'
	return int(b, 2)

def row(str):
	b = ""
	for x in str:
		if x == 'F':
			b = b + '0'
		else:
			b = b + '1'
	return int(b, 2)

def solve(lines):
	results = []
	for line in lines:
		r = row(line[0:7])
		c = column(line[7:10])
		res = r * 8 + c
		results.append(r * 8 + c)
	results.sort()

	print(results)

	prev = 0 
	for i, res in enumerate(results):
		if i == 0:
			prev = res
			continue
		if prev + 1 != res:
			return prev + 1
		prev = res

	return -1


if __name__ == "__main__":
    main()
