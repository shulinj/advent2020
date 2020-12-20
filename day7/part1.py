import re
import pprint

def main():
	with open("input.txt") as f:
		lines = f.readlines()

	print(solve(lines))

def get_map(lines):
	inner_colors_to_outer = {}

	for line in lines:
		line = line.strip()
		if not line:
			continue
		outer, inner_str = line.split("bags contain")
		inner_strs = inner_str.split(",")
		for ic in inner_strs:
			ic = ic.strip()
			words = ic.split(" ")
			inner_color = words[1] + " " + words[2]
			if inner_color not in inner_colors_to_outer:
				inner_colors_to_outer[inner_color] = []
			inner_colors_to_outer[inner_color].append(outer.strip())
	return inner_colors_to_outer

def solve_recursion(m, cc):
	if cc == 'other bags.':
		return set()

	if cc not in m:
		return set([cc])

	next_colors = m[cc]
	count = 0 

	found = set(m[cc])
	for nc in next_colors:
		r_found = solve_recursion(m, nc)
		for r in r_found:
			found.add(r)

	return found



def solve(lines):
	m = get_map(lines)
	f = solve_recursion(m, 'shiny gold')
	pprint.pprint(m)
	print f
	return len(f)

if __name__ == "__main__":
    main()
