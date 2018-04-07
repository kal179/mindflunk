


# Brainfuck Interpreter

# Intro:
# Brainfuck has 8 instructions, which are 
# turing complete which basically means that 
# they can read-write-manipulate Long array(tape) 
# of memory according to instructions
# PLUS PLUS bf interpreter does not have any 
# statements, clearly it's a plain turing language.
 
# References:
# Check out:
#    ||
#   _||_
#   \  /
#    \/
#  http://www.muppetlabs.com/~breadbox/bf/
#  https://en.wikipedia.org/wiki/Brainfuck

# Lil Extra:
# The interpreter uses direct instruction 
# interpretation to execute the instructions
# The memory consists of 30,000 memory cells
# each cell can store upto 1byte of memory


import sys


class BrainScrew:
	def __init__(self, fname):
		# Read instructions from bf source file
		self.instructions = str(open(fname, "r").read())
		# Memory cells to store guess what "data"
		self.memory = [0]*30000		
		# memory cell pointer
		self.cell_ptr = 0


	def run_fck(self):
		# instruction counter
		i = 0

		while i < len(self.instructions):
			# Check each individual possibility of instructions
			# that can occur in bf and execute 'em accordingly
			
			if self.instructions[i] == ">":
				# Move ptr to next memory cell 
				if self.cell_ptr+1 <= 30000:
					self.cell_ptr += 1
				else:
					# Memory pointer overflow
					print("Traceback Error: \n  >Looks like you want to store \n   memory at locations that do not exist, \n   You only have 30000 memory cells!")
					sys.exit(1)

			elif self.instructions[i] == "<":
				# Move ptr to next memory cell 
				if self.cell_ptr-1 >= 0:
					self.cell_ptr -= 1
				else:
					# Memory pointer underflow
					print("Traceback Error: \n  > Seriously, \n   No support for negative memory location/indexing")
					sys.exit(1)

			elif self.instructions[i] == "+":
				# Increment byte at current memory location
				if self.memory[self.cell_ptr]+1 <= 255:
					self.memory[self.cell_ptr] += 1
				else:
					# Memory overflow error
					print("Traceback Error: \n  > I guess 1 byte(2**8 bits) can store only upto signed -127 to 127 and unsigned 0 to 255 still i gave ya'll \n   signed option of -255 to 255, but looks like you exceeded that as well, \n   Suggestion move to next memory cell!")
					sys.exit(0)

			elif self.instructions[i] == "-":
				# Decrement byte at current memory location
				if self.memory[self.cell_ptr]-1 > -256:
					self.memory[self.cell_ptr] -= 1
				else:
					# Memory underflow error
					print("Traceback Error: \n  > I guess 1 byte(2**8) can store only upto signed -127 to 127 and signed 255 still i gave ya'll \n  signed option of -255 to 255, but looks like you exceeded that as well, \n  Suggestion move to next memory cell!")
					sys.exit(1)

			elif self.instructions[i] == ".":
				# Print byte at current memory cell
				print(chr(self.memory[self.cell_ptr]))

			elif self.instructions[i] == ",":
				# Input val and store it in current memory cell
				temp =  int(input())
				if not(temp > 255 or temp < -255):
					self.memory[self.cell_ptr] = temp
				else:
					# Memory error
					print("Traceback Error: \n  > C'mon 1 byte cannot store values greater than 255 and smaller than -255 \nin my BrainFuck Machine!!")
					sys.exit(1)


			# WORKING ON '[', ']' INSTRUCTIONS
			# TRYING TO IMPLEMENT 'EM using STACK
			# TO STORE THE LOOPS LOCATION 

			else:
				# Invalid instruction error
				print("Traceback Error: \n  >%s instruction does not exist \nin brainfuck!\n\n " % self.instructions[i])
				sys.exit(1)
			

			# Don't want an infinite loop do we??!!
			i+= 1	


# Run interpreter
# in terminal like following
# user@user~$ python brainfuck.py filename.bf

if __name__ == "__main__":
	BrainScrew(sys.argv[1]).run_fck()
