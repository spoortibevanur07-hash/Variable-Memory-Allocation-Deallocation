def check_placement(age, marks, attendance, experience, has_backlog):
	"""Return placement eligibility and category based on the given criteria.

	Age is accepted but does not affect eligibility because no age condition
	was specified.
	"""
	if experience == 0:
		category = "Fresher"
	elif 1 <= experience <= 2:
		category = "Junior"
	elif experience > 2:
		category = "Experienced"
	else:
		raise ValueError("Experience must be 0 or at least 1 year.")

	eligible = marks >= 60 and attendance >= 75 and not has_backlog
	return {
		"Placement eligible": "Yes" if eligible else "No",
		"Candidate category": category,
	}


if __name__ == "__main__":
	try:
		age = int(input("Enter age: "))
		marks = float(input("Enter marks: "))
		attendance = float(input("Enter attendance percentage: "))
		experience = int(input("Enter years of experience: "))
		has_backlog = input("Does the student have a backlog? (yes/no): ").strip().lower() == "yes"

		for result, answer in check_placement(age, marks, attendance, experience, has_backlog).items():
			print(f"{result}: {answer}")
	except ValueError as error:
		print(error or "Please enter valid numeric values.")