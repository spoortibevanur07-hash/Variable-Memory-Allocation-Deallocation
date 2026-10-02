def check_eligibility(marks, attendance, has_backlog):
	"""Return whether a student meets the eligibility requirements."""
	if marks >= 60 and attendance >= 75 and not has_backlog:
		return "Eligible"
	return "Not eligible"


if __name__ == "__main__":
	try:
		marks = float(input("Enter the student's marks: "))
		attendance = float(input("Enter the attendance percentage: "))
		has_backlog = input("Does the student have a backlog? (yes/no): ").strip().lower() == "yes"
		print(check_eligibility(marks, attendance, has_backlog))
	except ValueError:
		print("Please enter valid numbers for marks and attendance.")