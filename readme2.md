# Simple Guide to the Operator Tasks

Each task uses a function to receive information, make a decision or calculation, and return a result. When a Python file is run directly, it asks for input and displays that result.

## Task 1: Basic Calculator

File: `operators.py`

The `calculate(first_number, second_number)` function performs six operations on two integers:

- Addition: adds the numbers.
- Subtraction: subtracts the second number from the first.
- Multiplication: multiplies the numbers.
- Division: divides the first number by the second.
- Floor division: divides and drops the fractional part.
- Remainder: returns what is left after division.

For example, with `10` and `3`, the results are `13`, `7`, `30`, about `3.33`, `3`, and `1`. The second number cannot be zero because division, floor division, and remainder require a nonzero divisor.

## Task 2: Check a Number

File: `task2.py`

The `check_number(number)` function checks whether the number is even or odd and whether it divides evenly by 3 and by 5. A remainder of zero means it divides evenly.

For example, `check_number(15)` reports odd, divisible by 3, and divisible by 5.

## Task 3: Check Marks

File: `task3.py`

The `get_result(marks)` function returns:

- `Distinction` for marks of 75 or more.
- `Pass` for marks from 35 through 74.
- `Fail` for marks below 35.

Distinction is checked first because those marks also meet the pass threshold. For example, `get_result(80)` returns `Distinction`.

## Task 4: Student Eligibility

File: `task4.py`

The `check_eligibility(marks, attendance, has_backlog)` function returns `Eligible` only when marks are at least 60, attendance is at least 75%, and `has_backlog` is `False`. If any one of these conditions is not met, it returns `Not eligible`.

For example, `check_eligibility(60, 75, False)` returns `Eligible`.

## Task 5: Check Login Details

File: `task5.py`

The `check_credentials(username, password)` function returns `Valid user` only when the username is exactly `admin` and the password is exactly `python123`. Any other combination returns `Invalid user`.

For example, `check_credentials("admin", "python123")` returns `Valid user`. This is a practice exercise; real applications should not store passwords directly in code.

## Task 6: Calculate a Purchase Discount

File: `task6.py`

The `calculate_discount(purchase_amount)` function returns the discount amount and the final amount to pay:

- Purchases of 5000 or more receive a 20% discount.
- Purchases from 3000 up to, but not including, 5000 receive a 10% discount.
- Purchases below 300 receive a 5% discount.
- The stated rules do not assign a discount from 300 through 2999, so that range receives no discount in this program.

For example, a purchase of `6000` has a discount of `1200` and a final cost of `4800`. Negative purchase amounts are rejected.

## Task 7: Check Access

File: `task7.py`

The `check_access(age, has_id, is_employee)` function returns `Access granted` when the person is at least 18 and has an ID, or when the person is an employee. Being an employee grants access even if the person is under 18 or does not have an ID.

For example, `check_access(16, False, True)` returns `Access granted`.

## Task 8: Look Up a Skill

File: `task8.py`

The `required_skills` list contains `python`, `SQL`, `git`, and `Html`. The `check_skill(skill_name)` function checks whether the exact text is in that list and returns `Skill available` or `Skill not available`.

The check is case-sensitive: `SQL` is available, but `sql` is not.

## Task 9: Calculator with an Operator

File: `task9.py`

The `calculate(a, operator, b)` function performs one operation based on the operator supplied. It supports `+`, `-`, `*`, `/`, `//`, `%`, and `**` (power).

For example, `calculate(2, "**", 3)` returns `8`. An unsupported operator raises an error, and division, floor division, or remainder by zero also raises an error.

## Task 10: Placement Eligibility and Category

File: `task10.py`

The `check_placement(age, marks, attendance, experience, has_backlog)` function returns placement eligibility and an experience category.

A candidate is eligible when marks are at least 60, attendance is at least 75%, and there is no backlog. The experience category is `Fresher` for 0 years, `Junior` for 1 or 2 years, and `Experienced` for more than 2 years.

For example, `check_placement(20, 60, 75, 0, False)` returns eligible `Yes` and category `Fresher`. The age argument is accepted, but age is not used in the eligibility rule because no age condition was specified. Experience values below 0 or between 0 and 1 are rejected because they do not match the listed categories.