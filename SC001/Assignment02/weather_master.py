"""
File: weather_master.py
Name: 林劭懿 Ethan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program finds the maximum temperature, minimum temperature, average temperature,
	and	the cold days among user inputs.
	"""
	print('stanCode ' + 'Weather Master 4.0!')
	data = int(input('Next Temperature: ' + '(or -100 to quit)? '))
	if data == EXIT:
		print('No temperatures are entered.')
	else:
		maximum = data
		minimum = data
		sum_data = 0
		sum_n = 0
		cold_days = 0
		while True:
			data = int(input('Next Temperature: ' + '(or -100 to quit)? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if data != EXIT:
				sum_data = sum_data + data
				sum_n = sum_n + 1
			if EXIT < data < 16:
				cold_days = cold_days + 1

		avg = sum_data / sum_n
		print('Highest Temperature:　' + str(maximum))
		print('Lowest Temperature: ' + str(minimum))
		print('Average temperature: ' + str(avg))
		print('Cold days: ' + str(cold_days))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
