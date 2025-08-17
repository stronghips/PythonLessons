# Python Introduction 1
2023-11-05

## Python
Python is an interpreted programming language, i.e. it is executed line by line
by the Python interpreter. Languages like C or C++ are compiled languages, i.e. the
source code is compiled into machine code before it is executed (usually much faster).

## Packages
Packages contain functions and other things that we can use in our
program. They have been written by someone and we can use the functionality
of those packages.

To use a package we have to install it first using the package manager `pip`.
- `pip install turtle`
And then we have to import the functions that we need from the package in
our program:
- `from turtle import *`

## Control structures
## Conditional statements: if, else, elif

A condition is true or false. Branching allows us to execute different code paths based on conditions.
The program can have many execution paths

## Loops

A loop has a body, that is all the code that is executed
in one loop iteration.

### while
We usually don't know how often the loop is executed.
How many loop iterations are executed.

A while loop has a condition and it will execute as long
as the condition is true.

### for
We know before we enter the loop how often it will
be executed.

It doesn't have a boolean condition, but it usually has a loop
counter or a loop variable.

## Operators
### Boolean Operators not, ==, !=, and, or
A && B, A and B are both true.

They evaluate to true or false.

### Comparison Operators <, >, >=
They evaluate to true or false.

### Arithmetic Operators +, -, *, /
The evaluate to a number.

## Note:
- A boolean condition is a condition like `2 == 3`, and it evaluates to true or false.
- `.md` files contain markdown language.


## Debugger
A debugger is a tool that helps us find and fix errors in our code. It allows us to:
- Set breakpoints: Pause the execution of the program at a specific line.
- Step through the code: Execute the code line by line to see how it behaves.
- Inspect variables: Check the values of variables at different points in the program.
- Modify variables: Change the values of variables while debugging.

Using a debugger can make it much easier to understand what is happening in our code and to identify the root cause of issues.