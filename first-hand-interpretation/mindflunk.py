


# This is a big change
# if you saw last version of this code!
#  -- shift from oop to functions

# But this code looks much better and 
# works alike

# See: Readme.txt file 
# for introduction, info!


import sys


def cleansing_agent(_collection, lookup):
	# To clean file of non-instruction characters
	return [instr for instr in _collection if instr in lookup]


def files_got_content(fname):
	
	# To execute instructions, first we need to
	# read 'em from source file
	f_contents = open(fname, "r")
	temp = f_contents.read()
	f_contents.close()
	return temp


def build_index_map(_ops, _init, _end):
	
	# To build a map with locations
	# of loops i.e. key-value pairs of start index
	# and end index of loops
	index_map = {}

	# Top most-value of list(stack) will be location of latest 
	# start index encountered by for-loop, necessary for correct
	# matching of indexes
	cache = []

	for i in range(0, len(_ops)):
		# put encountered start indexes of loops in cache stack
		if _ops[i] == _init:
			cache.append(i)

		# when encountered with end of loop
		# form corresponding key value pairs
		# and clear cache
		elif _ops[i] == _end and len(cache):
			index_map[cache[-1]] = i 
			del cache[-1]
	
	return index_map


def run_fck(fname):
	# extract instructions from file, clean 'em
	instructions = cleansing_agent(list(str(files_got_content(fname))), [ ">", "<", "+", "-", ".", ",", "[", "]" ])
	instr_ptr = 0

	# Infinite memory cells and its cell pointer
	memory = [0]
	cell_ptr = 0

	# loop locations
	loops = build_index_map(instructions, "[", "]")
	if not loops:
		print("\nTraceback error:\n\t> Looks like you have a broken loop chain in u r source\n")
		sys.exit(0)
	loop_init = None


	# execute instructions
	while instr_ptr < len(instructions):
		
		# > move pointer to next memory cell
		if instructions[instr_ptr] == ">":
			memory.append(0)
			cell_ptr += 1
		
		# < move pointer to last memory cell
		elif instructions[instr_ptr] == "<":
			if cell_ptr-1 >= 0:
				cell_ptr -= 1
			else:
				print("\nTraceback error: \n\t> Instruction, address: %s, %d \n\t> Guess what, this version does \n\tnot support negative indexing(memory location)\n" %(instructions[instr_ptr], instr_ptr))
				sys.exit(1)
		
		# + increment byte at memory cell
		elif instructions[instr_ptr] == "+":
			if memory[cell_ptr]+1 <= 255:
				memory[cell_ptr] += 1
			else:
				print("\nTraceback error: \n\t> Instruction, address: %s, %d \n\t> In 1byte unsigned max val. you can fit is from 0 to 255(256 in total), \n\tI think you should move to next memory cell\n" %(instructions[instr_ptr], instr_ptr))
				sys.exit(1)
		
		# - decrement byte at memory cell
		elif instructions[instr_ptr] == "-":
			if memory[cell_ptr]-1 >= -255:
				memory[cell_ptr] -= 1
			else:
				print("\nTraceback error: \n\t> Instruction, address: %s, %d \n\t> To complement unsigned byte, you can store max -255\n\tSo, maybe move to next cell or \n\tforget about brainfuck!\n" %(instructions[instr_ptr], instr_ptr))
				sys.exit(0)
		
		# . output ascii(or unicode) encoded byte at memory cell
		elif instructions[instr_ptr] == ".":
			if memory[cell_ptr] >= 0:
				print(memory[cell_ptr])    # For Debugging
				#sys.stdout.write(chr(memory[cell_ptr]))
			else:
				print(memory[cell_ptr])     # For Debugging
				#sys.stdout.write(str(memory[cell_ptr]))
		
		# , input byte and store it in memory cell
		elif instructions[instr_ptr] == ",":
			memory[cell_ptr] = int(input())

		# [ move past corresponding ']' if byte at memory cell is 0(1> is true, 0 is false)
		elif instructions[instr_ptr] == "[":
			if memory[cell_ptr] == 0:
				instr_ptr = loops[instr_ptr]   # -1 since +1 at end of loop
			else: 
				loop_init = instr_ptr
		
		# ] end of loop(while)	
		elif instructions[instr_ptr] == "]":
			instr_ptr = loop_init-1   # -1 since +1 at end of loop


		# Don't want an infinite loop do we??!!
		instr_ptr += 1


# Run instructions
if __name__ == "__main__":
	run_fck(sys.argv[1])
