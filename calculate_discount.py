def calculate_discount(purchase_amount):
	"""Return the discount and final payable amount for a purchase."""
	if purchase_amount < 0:
		raise ValueError("Purchase amount cannot be negative.")

	if purchase_amount >= 5000:
		discount_rate = 0.20
	elif purchase_amount >= 3000:
		discount_rate = 0.10
	elif purchase_amount < 300:
		discount_rate = 0.05
	else:
		discount_rate = 0

	discount_amount = round(purchase_amount * discount_rate, 2)
	return {
		"Discount amount": discount_amount,
		"Final payable amount": round(purchase_amount - discount_amount, 2),
	}


if __name__ == "__main__":
	try:
		purchase_amount = float(input("Enter the purchase amount: "))
		for result, amount in calculate_discount(purchase_amount).items():
			print(f"{result}: {amount:.2f}")
	except ValueError:
		print("Please enter a valid non-negative purchase amount.")