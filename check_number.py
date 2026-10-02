def check_number(number):
	"""Report whether a number is even/odd and divisible by 3 and 5."""
	return {
		"Even or odd": "Even" if number % 2 == 0 else "Odd",
		"Divisible by 3": "Yes" if number % 3 == 0 else "No",
		"Divisible by 5": "Yes" if number % 5 == 0 else "No",
	}


if __name__ == "__main__":
	try:
		number = int(input("Enter an integer: "))
		for result, answer in check_number(number).items():
			print(f"{result}: {answer}")
	except ValueError:
		print("Please enter a valid integer.")