import re

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

def passport_is_valid(s):
	m = {
		"ecl":0, "pid":0 ,"eyr":0, "hcl":0,
		"byr":0, "iyr":0, "hgt":0
	}

	fields = re.split(' |\n', s)
	for field in fields:
		if field == "":
			continue
		k, _ = field.split(":")
		if k in m:
			m[k] = 1

	for v in m.values():
		if v == 0:
			return False
	return True

def solve(lines):
	parsed_lines = [""]

	for line in lines:
		if line == "\n":
			parsed_lines.append("")
			continue
		i = len(parsed_lines) - 1
		parsed_lines[i] = parsed_lines[i] + line

	#import pdb; pdb.set_trace()
	count = 0 
	for line in parsed_lines:
		if passport_is_valid(line):
			count += 1

	return count

if __name__ == "__main__":
    main()