def calculate(a, operator, b):
	"""Calculate a binary arithmetic operation."""
	if operator not in ("+", "-", "*", "/", "//", "%", "**"):
		raise ValueError(f"Invalid operator: {operator}")

	if operator in ("/", "//", "%") and b == 0:
		raise ZeroDivisionError("Cannot divide by zero.")

	if operator == "+":
		return a + b
	if operator == "-":
		return a - b
	if operator == "*":
		return a * b
	if operator == "/":
		return a / b
	if operator == "//":
		return a // b
	if operator == "%":
		return a % b
	return a ** b


if __name__ == "__main__":
	try:
		a = float(input("Enter the first number: "))
		operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
		b = float(input("Enter the second number: "))
		print(calculate(a, operator, b))
	except (ValueError, ZeroDivisionError) as error:
		print(error)