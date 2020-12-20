import re
import pprint

def main():
	with open("input.txt") as f:
		lines = f.readlines()

	print(solve(lines))

def has_sum(num, all_nums, low, high):
	i = low
	copy = set() # doesn't work for numbers with duplicates
	while i < high:
		copy.add(all_nums[i])
		i += 1
	
	#print copy
	for n in copy:
		if n+n == num: # can't happen if there's no duplicates
			continue
		#print n, num-n
		if num-n in copy:
			return True
	return False

def solve(lines):
	numbers = [int(l) for l in lines]
	i = 25
	while i < len(numbers):
		if not has_sum(numbers[i], numbers, i-25, i):
			return numbers[i]
		i += 1

if __name__ == "__main__":
    main()
