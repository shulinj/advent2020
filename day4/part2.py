import re
import functools

def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))


def hcl(s):
	if len(s) != 7:
		return False
	for i, c in enumerate(s):
		if i == 0:
			if s[i] != "#":
				return False
		else:
			if (s[i] < "0" or s[i] > "9") and (s[i] < "a" or s[i] > "f"):
				return False
	return True

def pid(s):
	return len(s) == 9 and reduce(lambda x, y: x*y, map(lambda x: 1 if x.isdigit() else 0, list(s))) == 1

def hgt(s):
	if "cm" not in s and "in" not in s: 
		return False 
	num = int(s[0:-2])
	if "cm" in s:
		return num >= 150 and num <= 193
	return num >= 59 and num <= 76


def passport_is_valid(s):
	# ):
	funcs = {
		"ecl": lambda ecl: ecl in ["amb","blu","brn","gry","grn","hzl","oth"], 
		"pid": pid ,
		"eyr": lambda eyr: len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030,
		"hcl": hcl,
		"byr": lambda byr: len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002, 
		"iyr": lambda iyr: int(iyr) >= 2010 and int(iyr) <= 2020, 
		"hgt": hgt
	}

	results = {
		"ecl":0, "pid":0 ,"eyr":0, "hcl":0,
		"byr":0, "iyr":0, "hgt":0
	}

	fields = re.split(' |\n', s)
	for field in fields:
		if field == "":
			continue
		k, v = field.split(":")
		if k in results and funcs[k](v) :
			results[k] = 1

	#print(results)
	for v in results.values():
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

	count = 0 
	for line in parsed_lines:
		if passport_is_valid(line):
			count += 1

	return count

if __name__ == "__main__":
    main()