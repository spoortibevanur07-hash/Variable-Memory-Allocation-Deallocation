# Python Functions

A function is a reusable, named block of code that performs a task. Functions help reduce repetition, organize a program into smaller parts, and make logic easier to test and maintain.

## Why use functions?

Without functions, similar instructions may need to be copied throughout a program. Repeated code is harder to update and makes mistakes more likely. A function lets you write an operation once and reuse it with different inputs.

```python
def welcome(name):
    print("Welcome,", name)


welcome("Asha")
welcome("Ravi")
```

## Define and call a function

Use the `def` keyword to define a function. The indented statements form its body. Defining a function does not run it; calling the function does.

```python
def greet():
    print("Hello!")


greet()
```

The parentheses in `greet()` are part of the call. A function can also be defined without parameters, as above, or with parameters that receive input values.

## Parameters and arguments

A **parameter** is a name in a function definition. An **argument** is a value supplied when the function is called.

```python
def welcome(name):
    print("Welcome,", name)


welcome("Asha")
```

Here, `name` is a parameter and `"Asha"` is the argument. A function can accept multiple parameters:

```python
def add(first, second):
    return first + second


print(add(10, 20))  # 30
```

## Return values

`return` sends a result back to the code that called the function. The caller can store the result, use it in another calculation, or display it.

```python
def add(first, second):
    return first + second


total = add(10, 20)
print(total)  # 30
```

`print()` displays a value; it does not return that value to the caller. If a function reaches the end without a `return` statement, it returns `None`. A `return` statement also ends the current function call immediately, so statements after it are not executed.

```python
def describe_number(number):
    if number < 0:
        return "negative"
    return "zero or positive"
```

Python functions can return multiple values. They are packaged as a tuple and can be unpacked by the caller.

```python
def calculate(first, second):
    return first + second, first - second, first * second


sum_result, difference, product = calculate(10, 5)
print(sum_result, difference, product)  # 15 5 50
```

## Passing arguments

### Positional arguments

Positional arguments are assigned to parameters by their order in the call.

```python
def show_student(name, age):
    print(name, age)


show_student("Asha", 21)
```

### Keyword arguments

Keyword arguments identify parameters by name. Their order does not matter.

```python
def show_student(name, age):
    print(name, age)


show_student(age=21, name="Asha")
```

Positional arguments must come before keyword arguments in a call. For example, `show_student("Asha", age=21)` is valid, but `show_student(name="Asha", 21)` is not.

### Default parameter values

A default value makes an argument optional when the function is called.

```python
def greet(name="there"):
    print("Hello,", name)


greet()         # Hello, there
greet("Asha")   # Hello, Asha
```

Parameters with defaults should follow required parameters in the function definition.

### Arbitrary positional arguments: `*args`

Use `*args` when a function should accept any number of extra positional arguments. Inside the function, those arguments are available as a tuple.

```python
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_all(10, 20))          # 30
print(add_all(1, 2, 3, 4, 5))  # 15
```

### Arbitrary keyword arguments: `**kwargs`

Use `**kwargs` to collect extra keyword arguments. Inside the function, they are available as a dictionary.

```python
def show_details(**details):
    print(details)


show_details(name="Asha", age=21, course="Python")
# {'name': 'Asha', 'age': 21, 'course': 'Python'}
```

These parameter forms can be combined. Required parameters come first, followed by optional positional parameters, `*args`, and `**kwargs` as needed.

```python
def describe(first, second="default", *extra, **details):
    print(first)
    print(second)
    print(extra)
    print(details)


describe("hello", "world", "again", language="Python")
```

## Variable scope

Scope determines where a name can be accessed.

### Local variables

A variable assigned inside a function is local to that function unless declared otherwise.

```python
def show_value():
    value = 10
    print(value)


show_value()
# print(value)  # NameError: value is not defined here
```

### Global variables

A function can read a global variable, but assigning to a global name from inside a function requires a `global` declaration.

```python
count = 0


def increment():
    global count
    count += 1


increment()
print(count)  # 1
```

Prefer passing values as arguments and returning results when practical. This keeps functions easier to reuse and test and avoids hidden changes to shared state.

## Functions calling other functions

A function can call another function and use its return value.

```python
def add(first, second):
    return first + second


def display_total():
    total = add(10, 20)
    print(total)


display_total()  # 30
```

## How a function call flows

When Python evaluates `multiply(5, 4)`, it finds the function, assigns `5` to `first` and `4` to `second`, runs the function body, and gives the returned value back to the caller.

```python
def multiply(first, second):
    return first * second


result = multiply(5, 4)
print(result)  # 20
```

The returned value is assigned to `result` after the function finishes.

## Functions are objects

In Python, a function is an object. You can assign it to another variable and call it through that name. Do not add parentheses when assigning the function itself; parentheses would call it immediately.

```python
def greet():
    print("Hello!")


say_hello = greet
say_hello()  # Hello!
```

## Higher-order functions

A higher-order function accepts another function as an argument or returns a function. Because functions are objects, they can be passed around like other values.

```python
def square(number):
    return number * number


def process(operation, value):
    return operation(value)


print(process(square, 5))  # 25
```

## Lambda expressions

A `lambda` expression creates a small anonymous function. It contains one expression and returns that expression's value. Use `def` for functions that need multiple statements or a descriptive reusable definition.

```python
square = lambda number: number * number
print(square(5))  # 25
```

Lambda expressions are sometimes useful with functions such as `map()`:

```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda number: number * 2, numbers))
print(doubled)  # [2, 4, 6, 8]
```

For this simple transformation, a list comprehension is often easier to read:

```python
doubled = [number * 2 for number in numbers]
```

## Recursion

Recursion is when a function calls itself. A recursive function needs a **base case** that stops the calls, and a recursive case that moves toward that base case.

```python
def countdown(number):
    if number <= 0:  # Base case
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(3)
```

The output is `3`, `2`, `1`, then `Done!`. Without a reachable base case, recursion continues until Python raises a `RecursionError`. For simple repetition, a loop is often more appropriate.

## A complete example

Functions can divide a program into small, meaningful steps.

```python
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def main():
    first = 10
    second = 5
    print("Sum:", add(first, second))
    print("Difference:", subtract(first, second))


main()
```

## Function-writing guidelines

- Choose descriptive names that explain the function's purpose.
- Keep each function focused on a clear task.
- Return values when callers need to reuse or further process a result.
- Use parameters instead of relying on global state where practical.
- Avoid unnecessary parameters and overly complicated functions.
- Add a docstring when a function's purpose or expected inputs are not obvious.

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width
```

## Summary

Functions package behavior into reusable units. They can receive values through parameters, return results to their callers, and call or be passed to other functions. Understanding arguments, return values, scope, and recursion provides a strong foundation for writing clear Python programs.