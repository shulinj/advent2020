import re
import pprint

def main():
	with open("input_small.txt") as f:
		lines = f.readlines()

	print(solve(lines))

class Code:
	def __init__(self, instruction, number):
		self.instruction = instruction
		self.number = number
		self.has_touched = False 
	def __repr__(self):
		return str(vars(self))

def get_list(lines):
	code_list = []
	for line in lines:
		instruction, number = line.split(" ")
		number = int(number)
		code_list.append(Code(instruction, number))
	return code_list


def solve(lines):
	program = get_list(lines)

	# detect loop
	global_acc = 0
	i = 0 
	while i < len(program):
		curr = program[i]
		if curr.has_touched:
			return global_acc

		curr.has_touched = True

		if curr.instruction == 'nop':
			i += 1
		elif curr.instruction == 'acc':
			global_acc += curr.number
			i += 1
		elif curr.instruction == 'jmp':
			i += curr.number

if __name__ == "__main__":
    main()
