"""
File: coin_flip_runs.py
Name: 林劭懿 Ethan
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	"""
	print("Let's flip a coin!")
	runs = int(input('Number of runs: '))
	flips = ''

	# generate random
	flip1 = r.randrange(0, 2)
	if flip1 == 0:
		flips += 'H'
	else:
		flips += 'T'
	run = 0
	is_in_a_row = False
	while True:
		flip2 = r.randrange(0, 2)
		if flip2 == 0:
			flips += 'H'
		else:
			flips += 'T'

	# find out whether there is a continuous variables
		if flip1 == flip2:
			if not is_in_a_row:
				run += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		flip1 = flip2

		# The breakpoint, the point to stop the program.
		if run == runs:
			print(flips)
			break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
