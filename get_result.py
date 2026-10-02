def get_result(marks):
	"""Return the student's result based on their marks."""
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Pass"
	return "Fail"


if __name__ == "__main__":
	try:
		marks = int(input("Enter the student's marks: "))
		print(get_result(marks))
	except ValueError:
		print("Please enter a valid number of marks.")