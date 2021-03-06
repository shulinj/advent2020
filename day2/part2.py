def main():
	f = open("input.txt")
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	print(solve(lines))

class PasswordData:
	def __init__(self, line):
		r, c, p = line.split(" ")
		self.low, self.high = self.get_range(r)
		self.character = self.get_char(c)
		self.password = p

	def get_range(self, range_str):
		l, h = range_str.split("-")
		return int(l), int(h)

	def get_char(self, char_str):
		c, _ = char_str.split(":")
		return c

	def is_valid(self):
		return (self.password[self.low-1] == self.character and self.password[self.high-1] != self.character) or (self.password[self.low-1] != self.character and self.password[self.high-1] == self.character) 


def solve(lines):
	# translate
	valid_passwords = 0
	for line in lines:
		password = PasswordData(line)
		if password.is_valid():
			valid_passwords += 1
	return valid_passwords


if __name__ == "__main__":
    main()