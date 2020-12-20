import re
import pprint

def main():
	with open("input.txt") as f:
		lines = f.readlines()

	print(solve(lines))

class Bag:
	def __init__(self, color, number):
		self.color = color
		self.number = number

	def __repr__(self):
		return str(vars(self))

def get_map(lines):
	outer_to_inner = {}

	for line in lines:
		line = line.strip()
		if not line:
			continue
		outer_color, inner_str = line.split("bags contain")
		inner_strs = inner_str.split(",")
		for ic in inner_strs:
			ic = ic.strip()
			words = ic.split(" ")
			num = 0 if words[0] == "no" else int(words[0])
			inner_color = Bag(words[1] + " " + words[2], num)

			outer_color = outer_color.strip()
			if outer_color not in outer_to_inner:
				outer_to_inner[outer_color] = []
			outer_to_inner[outer_color].append(inner_color)
	return outer_to_inner

def recurse(mapping, curr_color):
	if curr_color not in mapping:
		return 1
	next_list = mapping[curr_color]
	current_result = 0
	for bag in next_list:
		current_result += bag.number + bag.number * recurse(mapping, bag.color)
	return current_result


def solve(lines):
	m = get_map(lines)
	pprint.pprint(m)
	return recurse(m, "shiny gold")


if __name__ == "__main__":
    main()
