import re
import pprint

def main():
	with open("input.txt") as f:
		lines = f.readlines()

	print(solve(lines))

class Code:
	def __init__(self, instruction, number):
		self.instruction = instruction
		self.number = number
	def __repr__(self):
		return str(vars(self))

def get_list(lines):
	code_list = []
	for line in lines:
		instruction, number = line.split(" ")
		number = int(number)
		code_list.append(Code(instruction, number))
	return code_list

def loop_detected(program):
	has_touched = [False] * len(program)
	global_acc = 0
	i = 0 
	while i < len(program):
		curr = program[i]
		if has_touched[i]:
			return True, 0

		has_touched[i] = True

		if curr.instruction == 'nop':
			i += 1
		elif curr.instruction == 'acc':
			global_acc += curr.number
			i += 1
		elif curr.instruction == 'jmp':
			i += curr.number
	return False, global_acc


def solve(lines):
	program = get_list(lines)

	for codeline in program:
		if codeline.instruction == 'nop':
			codeline.instruction = 'jmp'
			detected, global_acc = loop_detected(program)
			if not detected:
				return global_acc
			else:
				codeline.instruction = 'nop'

		elif codeline.instruction == 'jmp':
			codeline.instruction = 'nop'
			detected, global_acc = loop_detected(program)
			if not detected:
				return global_acc
			else:
				codeline.instruction = 'jmp'
	return -1 # wrong answer


if __name__ == "__main__":
    main()
