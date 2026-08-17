# Python Programming Roadmap & Practice

A structured and beginner-friendly Python learning repository containing practical programs, examples, and exercises from basic programming concepts to object-oriented programming and intermediate Python.

This repository is designed to help students and beginners learn Python step by step through hands-on coding practice. Each major topic contains multiple programs so that concepts can be understood through implementation instead of theory only.

**Created by Ahmad Akhtar**

---

## About This Repository

This repository is a complete Python practice roadmap that starts from the very basics of Python programming and gradually moves toward more advanced concepts.

The main purpose of this repository is to:

* Build strong Python programming fundamentals
* Practice programming concepts through examples
* Improve problem-solving skills
* Understand Python syntax and logic
* Learn Object-Oriented Programming
* Practice arrays, strings, collections, functions, and recursion
* Understand modules, packages, and decorators
* Prepare for university assignments, programming labs, interviews, and personal projects

Most sections contain **20 or more Python programs** for practice.

---

## Topics Covered

### 1. Python Basics

This section introduces the basic concepts required to start programming in Python.

Topics include:

* Installing Python
* Running Python programs
* `print()` function
* Variables
* Data types
* Type conversion
* Taking input from the user
* Displaying output
* Arithmetic operators
* Comparison operators
* Logical operators
* Assignment operators

Example concepts:

```python
name = input("Enter your name: ")
print("Welcome,", name)
```

---

## 2. Conditions

Conditional statements allow a program to make decisions based on different situations.

Topics include:

* `if`
* `if-else`
* `if-elif-else`
* Nested conditions
* Multiple conditions
* Logical operators with conditions

Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")
```

This section contains different programs based on decision-making problems.

---

## 3. Loops

Loops are used when we want to repeat a block of code multiple times.

Topics include:

* `for` loop
* `while` loop
* Nested loops
* `break`
* `continue`
* Loop with conditions
* Range function

Example:

```python
for number in range(1, 6):
    print(number)
```

The programs in this section help develop strong programming logic.

---

## 4. Functions

Functions help divide a large program into smaller reusable blocks.

Topics include:

* Creating functions
* Calling functions
* Parameters
* Arguments
* Return values
* Default parameters
* Local variables
* Global variables
* Scope

Example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)
```

Functions make programs easier to understand, maintain, and reuse.

---

## 5. Recursion

Recursion is a programming technique where a function calls itself.

Topics include:

* Basic recursion
* Base condition
* Recursive calls
* Factorial using recursion
* Fibonacci using recursion
* Sum using recursion

Example:

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

This section helps understand recursive problem-solving techniques.

---

## 6. Python Collections

Python provides several built-in data structures for storing and managing data.

This repository covers:

### Lists

Lists store multiple values in a single variable.

```python
students = ["Ali", "Ahmed", "Sara"]

print(students)
```

Topics include:

* Creating lists
* Adding elements
* Removing elements
* Updating values
* Searching
* Sorting
* Looping through lists

---

### Tuples

Tuples are similar to lists but cannot normally be modified after creation.

```python
colors = ("Red", "Green", "Blue")

print(colors)
```

Topics include:

* Creating tuples
* Accessing elements
* Tuple operations
* Tuple unpacking

---

### Sets

Sets store unique values.

```python
numbers = {10, 20, 30, 30}

print(numbers)
```

Topics include:

* Adding values
* Removing values
* Union
* Intersection
* Difference

---

### Dictionaries

Dictionaries store data in key-value pairs.

```python
student = {
    "name": "Ahmad",
    "age": 21,
    "course": "Computer Science"
}

print(student["name"])
```

Topics include:

* Creating dictionaries
* Adding data
* Updating data
* Removing data
* Accessing keys and values
* Looping through dictionaries

---

## 7. One-Dimensional Arrays

Python commonly uses lists to represent one-dimensional arrays.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Programs in this section include:

* Array input
* Array output
* Sum of array elements
* Maximum value
* Minimum value
* Searching
* Sorting
* Reversing
* Counting values
* Updating array elements

---

## 8. Two-Dimensional Arrays

Two-dimensional arrays can be represented using nested lists.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)
```

Programs cover:

* Creating matrices
* Displaying matrices
* Matrix addition
* Matrix operations
* Row operations
* Column operations
* Diagonal elements
* Searching matrix elements

---

## 9. Strings

Strings are used to store text.

Example:

```python
message = "Python Programming"

print(message.upper())
print(message.lower())
```

Topics include:

* String creation
* String indexing
* String slicing
* String length
* String searching
* String replacement
* Uppercase and lowercase conversion
* String comparison
* Reversing strings
* Counting characters and words

---

## 10. File Handling

File handling allows Python programs to store and retrieve information from files.

Topics include:

* Creating files
* Reading files
* Writing files
* Appending data
* Text files
* CSV files
* File modes

Example:

```python
file = open("example.txt", "w")

file.write("Learning Python File Handling")

file.close()
```

Using the `with` statement:

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

---

## 11. Exception Handling

Exception handling allows programs to manage errors without stopping unexpectedly.

Topics include:

* `try`
* `except`
* `else`
* `finally`
* Multiple exceptions
* Custom exceptions

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")
```

---

## 12. Object-Oriented Programming

Object-Oriented Programming is one of the most important programming concepts.

This repository contains multiple OOP examples covering:

### Classes and Objects

```python
class Student:

    def display(self):
        print("Student object created")


student1 = Student()

student1.display()
```

---

### Constructors

```python
class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Ahmad")

print(student1.name)
```

---

### Inheritance

Inheritance allows one class to use features of another class.

Topics include:

* Single inheritance
* Multiple inheritance
* Multilevel inheritance
* Hierarchical inheritance

---

### Encapsulation

Encapsulation helps protect and organize class data.

---

### Polymorphism

Polymorphism allows the same method name to perform different operations.

---

### Abstraction

Abstraction is used to hide unnecessary implementation details and show only important functionality.

This OOP section contains multiple examples to help understand these concepts practically.

---

## 13. Modules and Packages

Modules and packages help organize large Python applications.

Topics include:

* `import`
* Importing specific functions
* Creating custom modules
* Creating packages
* Using built-in modules
* Installing external packages

Example:

```python
import math

print(math.sqrt(25))
```

---

## 14. pip

`pip` is Python's package manager.

It allows developers to install external Python libraries.

Example:

```bash
pip install requests
```

To view installed packages:

```bash
pip list
```

To uninstall a package:

```bash
pip uninstall requests
```

---

## 15. Virtual Environments

Virtual environments allow Python projects to maintain separate dependencies.

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on Linux or macOS:

```bash
source venv/bin/activate
```

Deactivate:

```bash
deactivate
```

---

## 16. Intermediate Python

After learning the fundamentals, this section introduces more powerful Python concepts.

Topics include:

* List comprehensions
* Lambda functions
* `map()`
* `filter()`
* Iterators
* Generators
* Advanced function techniques
* Pythonic programming concepts

---

## 17. List Comprehensions

List comprehensions provide a short and readable way to create lists.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

---

## 18. Lambda Functions

Lambda functions are small anonymous functions.

Example:

```python
square = lambda number: number * number

print(square(5))
```

---

## 19. map() and filter()

### map()

`map()` applies a function to each element of a collection.

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

### filter()

`filter()` selects elements that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

---

## 20. Iterators

An iterator allows values to be accessed one at a time.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

---

## 21. Generators

Generators produce values one at a time instead of storing all values in memory.

Example:

```python
def numbers():

    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)
```

Generators are useful when working with large amounts of data.

---

## 22. Decorators

Decorators allow us to add extra functionality to an existing function without modifying the original function directly.

Example:

```python
def my_decorator(function):

    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper


@my_decorator
def welcome():
    print("Welcome to Python")


welcome()
```

Decorators are commonly used in frameworks, APIs, authentication systems, logging, and other professional Python applications.

---

# Repository Structure

The repository follows a structured learning sequence.

```text
python-programming-roadmap/
│
├── 01_Python_Basics/
│
├── 02_Conditions/
│
├── 03_Loops/
│
├── 04_Functions/
│
├── 05_Recursion/
│
├── 06_Python_Collections/
│   ├── Lists/
│   ├── Tuples/
│   ├── Sets/
│   └── Dictionaries/
│
├── 07_1D_Arrays/
│
├── 08_2D_Arrays/
│
├── 09_Strings/
│
├── 10_File_Handling/
│
├── 11_Exception_Handling/
│
├── 12_Object_Oriented_Programming/
│
├── 13_Modules_and_Packages/
│
├── 14_Intermediate_Python/
│
├── 15_Decorators/
│
├── README.md
│
└── .gitignore
```

The exact folder names may vary slightly, but the repository follows this overall learning sequence.

---

# Number of Practice Programs

The repository contains hundreds of Python practice files.

Most major topics contain approximately **20 or more programs**, providing enough practice to understand each concept through actual coding.

The programs are designed to progress from simple examples to slightly more challenging problems.

---

# How to Use This Repository

## Step 1: Install Python

Download and install Python from the official Python website.

After installation, verify it using:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/python-programming-roadmap.git
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## Step 3: Open the Project

You can open the project using:

* Visual Studio Code
* PyCharm
* IntelliJ IDEA with Python support
* Any Python-compatible IDE or editor

---

## Step 4: Select a Topic

Start with:

```text
01_Python_Basics
```

Then continue folder by folder in numerical order.

Following the sequence will make learning easier because later topics use concepts introduced in earlier sections.

---

## Step 5: Run a Python Program

Open the terminal inside the project folder.

Run:

```bash
python filename.py
```

Example:

```bash
python 01_hello_world.py
```

---

# Learning Approach

For better learning, follow this method:

1. Read the program carefully.
2. Understand each line.
3. Run the program.
4. Change some values.
5. Observe the output.
6. Rewrite the program yourself.
7. Try solving the same problem without looking at the original solution.

Programming improves through practice, not only by reading code.

---

# Who Can Use This Repository?

This repository can be useful for:

* Python beginners
* Computer Science students
* Software Engineering students
* University students
* Programming lab preparation
* Python assignment practice
* Beginners preparing for coding interviews
* Students learning Object-Oriented Programming
* Anyone who wants structured Python practice

---

# Prerequisites

No advanced programming knowledge is required.

Basic computer usage is enough to begin.

Recommended tools:

* Python 3
* Visual Studio Code or PyCharm
* Git
* GitHub
* Command Prompt, PowerShell, or Terminal

---

# Main Learning Goals

After completing this repository, a learner should understand:

* Python syntax
* Variables and data types
* Input and output
* Operators
* Conditional statements
* Loops
* Functions
* Recursion
* Lists
* Tuples
* Sets
* Dictionaries
* Arrays
* Strings
* File handling
* Exception handling
* Object-Oriented Programming
* Classes and objects
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction
* Modules
* Packages
* pip
* Virtual environments
* Lambda functions
* List comprehensions
* Iterators
* Generators
* Decorators

---

# Development Environment

The programs in this repository are written using:

```text
Language: Python
Recommended Version: Python 3.x
```

The code is designed to be simple enough for beginners while still following proper Python programming concepts.

---

# Coding Style

The programs are written with a focus on:

* Simple logic
* Meaningful variable names
* Beginner-friendly comments
* Readable formatting
* Small and understandable examples
* Practical programming exercises

The goal is to make every program understandable instead of making the code unnecessarily complicated.

---

# Practice Recommendation

Do not simply copy and paste the programs.

For maximum benefit:

```text
Read → Understand → Run → Modify → Rewrite → Practice
```

Try creating your own variations of every program.

For example, after learning a program that checks whether a number is even or odd, try creating programs that check:

* Positive or negative numbers
* Voting eligibility
* Student grades
* Maximum of multiple numbers
* Leap years

This helps improve programming logic.

---

# Future Improvements

This repository may be extended in the future with topics such as:

* Advanced Python
* Regular Expressions
* JSON handling
* Date and Time
* Database programming
* SQLite
* MySQL with Python
* APIs
* NumPy
* Pandas
* Matplotlib
* Automation
* Web scraping
* Flask
* Django
* Data Structures and Algorithms
* Python projects

---

# Contribution

This repository is mainly created for learning and programming practice.

Suggestions and improvements are welcome.

If you find an issue or have an idea for improving an example, you can open an issue or suggest an improvement through GitHub.

---

# Author

**Ahmad Akhtar**

Computer Science Student
Python Learner & Developer

This repository represents my Python learning, programming practice, and continuous improvement in software development.

---

# Repository Purpose

The main purpose of this repository is education and personal skill development.

It serves as a structured record of Python programming concepts and practice exercises, progressing from beginner-level concepts toward intermediate Python programming.

---

# Final Note

Learning programming takes time and consistent practice.

This repository is organized so that learners can progress step by step instead of trying to learn everything at once.

Start with the basics, understand the logic behind each program, practice regularly, and gradually move toward more advanced Python concepts.

> **Learn the concept. Understand the logic. Write the code. Practice again.**

---

**Created by Ahmad Akhtar**
