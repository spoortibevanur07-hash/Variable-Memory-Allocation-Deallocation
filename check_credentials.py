def check_credentials(username, password):
	"""Return whether the username and password are valid."""
	if username == "admin" and password == "python123":
		return "Valid user"
	return "Invalid user"


if __name__ == "__main__":
	username = input("Enter username: ")
	password = input("Enter password: ")
	print(check_credentials(username, password))