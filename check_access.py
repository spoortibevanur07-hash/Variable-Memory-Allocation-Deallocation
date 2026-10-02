def check_access(age, has_id, is_employee):
	"""Return whether the person is allowed access."""
	if (age >= 18 and has_id) or is_employee:
		return "Access granted"
	return "Access denied"


if __name__ == "__main__":
	try:
		age = int(input("Enter age: "))
		has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"
		is_employee = input("Are you an employee? (yes/no): ").strip().lower() == "yes"
		print(check_access(age, has_id, is_employee))
	except ValueError:
		print("Please enter a valid age.")