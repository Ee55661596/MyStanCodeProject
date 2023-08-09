"""
File: quadratic_solver.py
Name: 林劭懿 Ethan
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
	"""
	This program asks 3 inputs (a, b, and c) from users
	to compute the roots of equation:
	ax^2 + bx + c = 0.
	"""
	a = int(input(' Enter a : '))
	b = int(input(' Enter b : '))
	c = int(input(' Enter c : '))
	x1 = (-b + (b*b - 4*a*c)) / 2*a
	x2 = (-b - (b*b - 4*a*c)) / 2*a
	judg = b*b - 4*a*c
	if judg > 0:
		print('Two Roots : ' + str(x1) + ' & '+  str(x2))

	elif judg == 0:
		print('One Root : ' + str(x1) or str(x2))
	else:
		print('No Real Roots ')













# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
