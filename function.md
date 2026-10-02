# Functions in Python

A function is a reusable block of code that performs a specific task. Instead of writing the same lines multiple times, you define a function once and call it whenever needed. Functions help make programs shorter, easier to understand, easier to test, and easier to maintain.

## Why do we use functions?

Functions solve a very common programming problem: repetition.

Without functions, the same instructions may be copied again and again. This leads to:

- repeated code
- difficult maintenance
- greater chance of mistakes
- poor code organization
- harder debugging and testing

With functions, you can:

- reuse logic
- reduce repetition
- organize code into meaningful sections
- write cleaner programs
- test smaller parts of the program separately

Example:

```python
print("sandhya")
print("apoorva")
print("spoorti")
print("bhagirathi")
```

The above prints the same type of message four times. This is repetitive. A function can simplify it:

```python
def welcome(name):
    print("welcome", name)

welcome("sandhya")
welcome("apoorva")
welcome("spoorti")
welcome("bhagirathi")
```

This is much cleaner and reusable.

---

## What exactly is a function?

A function is a named block of code that can be executed whenever needed.

It usually contains:

- a unique function name
- optional parameters
- a body of statements
- an optional return value

A function can be used to perform a task like adding numbers, validating input, printing a message, or processing data.

### Basic function syntax

```python
def function_name(parameters):
    # body of the function
    statement 1
    statement 2
    return value    # optional
```

The `def` keyword tells Python that we are defining a function.

---

## Defining vs calling a function

### Defining a function

```python
def greet():
    print("hello")
```

This only defines the function. It does not run the code inside it yet.

### Calling a function

```python
greet()
```

This executes the function body and prints the message.

So,

- definition creates the function
- call runs the function

---

## Function without parameters

A function may not need any input values.

```python
def welcome():
    print("welcome to Nighan2 Labs")

welcome()
```

This is the simplest form of a function.

It is useful when the function does not depend on external input.

---

## Function with parameters

A parameter is a variable used inside the function definition. An argument is the actual value passed when the function is called.

```python
def welcome(name):
    print("welcome", name)

welcome("sandhya")
```

Here:

- `name` is the parameter
- `"sandhya"` is the argument

A function may have one parameter or many parameters.

### Example with multiple parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This prints:

```python
30
```

---

## Return statement

The `return` statement is one of the most important parts of a function.

A function can either:

- print something and display output
- return a value back to the caller

### Difference between `print()` and `return`

```python
def add(a, b):
    print(a + b)
```

This displays the result on the screen, but the function does not send the result back for further use.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

This is better because the result is sent back to the caller. Then the caller can store it, compare it, or print it later.

### Important point

`return` immediately exits the function.

```python
def text():
    return 10
    print("hello")
```

The line `print("hello")` never executes because Python exits the function as soon as it reaches `return`.

---

## Multiple return values

Python allows a function to return more than one value.

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)
print(y)
print(z)
```

Output:

```python
15
5
50
```

This works because Python returns a tuple of values.

---

## Default parameters

A default parameter provides a value when the caller does not pass one.

```python
def greet(name="sandhya"):
    print("hello", name)

greet()
greet("apoorva")
```

Output:

```python
hello sandhya
hello apoorva
```

Default parameters are useful when a value is optional.

---

## Positional arguments

Python matches arguments to parameters by position.

```python
def student(name, age):
    print(name, age)

student("sandhya", 21)
```

This works because the first argument goes to `name` and the second goes to `age`.

---

## Keyword arguments

Keyword arguments pass values using the parameter name.

```python
def student(name, age):
    print(name, age)

student(age=21, name="sandhya")
```

This works because names are explicitly matched.

The order does not matter when using keyword arguments.

---

## Positional and keyword arguments together

```python
def student(name, age, course):
    print(name, age, course)

student("sandhya", 21, "BCA")
```

This uses positional arguments.

```python
def student(name, age, course):
    print(name, age, course)

student(name="sandhya", age=21, course="BCA")
```

This uses keyword arguments.

### Important rule

A positional argument cannot appear after a keyword argument in the same function call.

```python
def student(name, age, course):
    print(name, age, course)

student("spoorti", age=21, "BCA")
```

This is invalid and raises a syntax error.

---

## Variable-length arguments: `*args`

Sometimes you may not know how many arguments will be passed.

`*args` collects extra positional arguments into a tuple.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

Output:

```python
30
60
15
```

Here, `numbers` is a tuple containing all the incoming arguments.

This is useful when a function should accept any number of values.

---

## Variable-length keyword arguments: `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def student(**details):
    print(details)

student(name="sandhya", age=21, course="BCA")
```

Output:

```python
{'name': 'sandhya', 'age': 21, 'course': 'BCA'}
```

Here, `details` is a dictionary of all the passed keyword arguments.

This is useful when the number of named values is unknown in advance.

---

## Combining positional and keyword arguments

A function can have a general structure like this:

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

example(1, 2, 3, 4, 5, name="sandhya", age=21)
```

This function contains:

- a required positional parameter: `a`
- an optional positional parameter: `b`
- extra positional values in `*args`
- extra keyword values in `**kwargs`

---

## Scope: local vs global variables

Scope defines where a variable can be used.

### Local variable

```python
def test():
    x = 10
    print(x)

test()
```

`x` is local to the function. It exists only inside `test()`.

### Global variable

```python
x = 100

def test():
    print(x)

test()
```

`x` is global, so the function can read it.

### Important rule

```python
def test():
    x = 10

print(x)
```

This will raise an error because `x` is local to `test()` and not accessible outside.

---

## Using `global`

If you want to modify a global variable inside a function, you must use the `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

Output:

```python
1
```

Using global variables is sometimes necessary, but it is often better to pass values as arguments and return results instead of relying on global state.

This makes code more reusable and easier to test.

---

## Functions calling other functions

Functions can call other functions.

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

Output:

```python
30
```

This is a very common pattern in real software development. One function may validate data, another may calculate result, another may save data, and another may display it.

Typical flow:

```text
main -> validate -> calculate -> save -> display
```

---

## Example of a complete function-based program

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    x = 10
    y = 5
    total = add(x, y)
    difference = subtract(x, y)

    print("Sum:", total)
    print("Difference:", difference)


main()
```

This program shows how functions can be used to divide a task into simple, meaningful steps.

---

## Best practices for functions

- use descriptive names
- keep functions focused on one task
- avoid too many parameters
- prefer returning values over printing inside deeply reusable logic
- use default values when appropriate
- avoid unnecessary global variables
- write small functions that are easy to test

Example of a good function:

```python
def calculate_area(length, width):
    return length * width
```

This is clear, simple, and reusable.

---

## Summary

Functions are a fundamental part of Python programming.

They allow you to:

- reuse code
- reduce repetition
- organize logic
- simplify debugging
- improve maintainability
- build large programs from smaller components

A function can accept parameters, return values, use defaults, and work with positional or keyword arguments. It may also call other functions and use local or global scope depending on the design.

In short, functions make programs cleaner, modular, and easier to understand.

---

## Final note

Understanding functions is essential for writing effective Python programs. They are the building blocks of structured and reusable code. Once you master function creation, parameter passing, and return values, you are ready for more advanced programming topics such as modules, classes, recursion, and larger application design.


23. function calling flow

def multiply(a,b):
    return a*b
results = multiply(5,4)
explain flow 

24. functions are objects 
def greet():
    print("hello")
    x=greet
    x()
x now refers to the function object 

25. passing a function to the another function 
def square(x):
return x*x
def process(function,value):
    return (value)
print(process(square,5))       

this introduces higher order functions

26. lambda functions
square = lambda x: x*x
print(square(5))

lambda is an ananymous function expression commonly used for small operations
e.g: numbers = [1,2,3,4]
     result=list(map(lambda :x*2,numbers))
     print(result)

27. recursion
    def countdown(n):
        if n==0 :
           return
        print(n)   
        countdown(n-1)
    countdown(5)
  a recursive function calls itself

28. function documentation
   def add(a,b):
   "" "" "" return the sum of two numbers "" "" ""
   return a+b    

   print(add.__.__)
   this introduces professional python habbit 

29. type hints
    for modern python
    def add(a:int,b:int)->int:
    return a+b

    communicate indented types to developers and tools :pyhton generally doesn't enforce them automatically at runtime 

a practical program
smart electricity bill
def  calculate_bill(units):
    if units<=100:
       amounts = unit*2
    elif units <=200:
    amounts=100*2+(units-100)*4
    else:
    amount = 100*2 + 100*4 + (units-200*6)
    return amount+100
units = int(input(enter units))
bill = calculate_bill(units)
    print("bill","variable bill")  

    why did we create calculate_bill() instead of writing everything inn the main program?
    bcz of separtion of responsibility , reusability, testing,readability,maintainance

30. function design
 a good function generally as input,processing and output 

31.dont create giant functions 

bad 
def student_system():
# 200 lines
input
# validation
# calculation
# database
# printing

better
def get_students():
def validate_students():
def calculate_students():
def save_result():
display_result
this introduces single responsibility without making the function more efficient