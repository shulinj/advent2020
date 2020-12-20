import re
import pprint

# when your code isn't beautiful )':
last_result = 258585477

def main():
	with open("input.txt") as f:
		lines = f.readlines()
	print(solve(lines))

def solve(lines):
	numbers = [int(l) for l in lines]
	sums = []
	for i, n in enumerate(numbers):
		if i == 0:
			sums.append(n)
			continue
		sums.append(sums[i-1] + n)

	prev = {} # number to index
	for i, s in enumerate(sums):
		if i != 0 and abs(last_result-s) in prev:
			high = i
			low = prev[abs(last_result-s)] + 1
			return min(numbers[low:high+1]) + max(numbers[low:high+1])
		prev[s] = i

	return -1 

if __name__ == "__main__":
    main()
