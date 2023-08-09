"""
File: prime_checker.py
Name: 林劭懿 Ethan
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This number show when to stop
EXIT = -1


def main():
	"""
	This program is try to help people to find out whether the number is prime number
	"""
	print('Welcome to the prime checker!')
	data = int(input('n: '))
	if data == EXIT:
		print('Have a good one!')
	else:
		while True:
			if data > 1:
				# check  factors
				for i in range(2, data):
					if (data % i) == 0:
						print(str(data), " is not a prime number")
						break
				else:
					print(str(data), " is a prime number")

			# if input number is less than
			# or equal to 1, it is not prime
			else:
				print(str(data), " is not a prime number")
			data = int(input('n: '))
			if data == EXIT:
				print('Have a good one!')
				break








	# while True:
	# 
	# 	if data == EXIT:
	# 		break
	# 	if data > 1:
	# 		for i in range(2, data):
	# 			if data % i == 0:
	# 				print(str(data) + " is not a prime number.")
	# 				break
	# 
	# 			else:
	# 				print(str(data) + " is a prime number.")
	# 
	# 	else:
	# 		print(str(data) + " is not a prime number.")
	# 	data = int(input('n: '))
	# 
	# print('Have a good one!')









# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
