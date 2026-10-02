def calculate(first_number, second_number):
	"""Return the results of the basic arithmetic operations."""
	if second_number == 0:
		raise ValueError("The second number must not be zero for division operations.")

	return {
		"Addition": first_number + second_number,
		"Subtraction": first_number - second_number,
		"Multiplication": first_number * second_number,
		"Division": first_number / second_number,
		"Floor division": first_number // second_number,
		"Remainder": first_number % second_number,
	}


if __name__ == "__main__":
	try:
		first_number = int(input("Enter the first number: "))
		second_number = int(input("Enter the second number: "))
		results = calculate(first_number, second_number)

		for operation, result in results.items():
			print(f"{operation}: {result}")
	except ValueError as error:
		print(error)
