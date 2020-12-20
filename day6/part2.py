import re

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

def solve(lines):
	groups = [{}]
	group_sizes = [0]
	for line in lines:
		if line == "\n":
			groups.append({})
			group_sizes.append(0)
			continue
		last = len(groups) -1
		group_sizes[last] = group_sizes[last] + 1

		for char in line:
			if char != "\n":
				if char not in groups[last]:
					groups[last][char] = 0
				groups[last][char] = groups[last][char] + 1
				

	result = 0
	for i, group in enumerate(groups):
		group_size = group_sizes[i]
		print group
		print group_size
		for k, v in group.items():
			if v == group_size:
				result = result + 1

	return result

if __name__ == "__main__":
    main()
