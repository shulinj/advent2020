import re

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
	result = 0
	for line in lines:
		r = row(line[0:7])
		c = column(line[7:10])
		if (r * 8 + c) > result:
			result = r * 8 + c
	return result


if __name__ == "__main__":
    main()
