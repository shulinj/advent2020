import re

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

def solve(lines):
	groups = [set()]
	for line in lines:
		if line == "\n":
			groups.append(set())
			continue
		last = len(groups) -1
		for char in line:
			if char != "\n":
				groups[last].add(char)

	result = 0
	for group in groups:
		result = result + len(group)

	return result

if __name__ == "__main__":
    main()
