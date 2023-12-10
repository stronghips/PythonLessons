# Python Introduction 2
2023-11-11

## Libraries
A library is code that you can use in your program without having to write it
yourself. You cannot execute it like program. But you can use the functions
that the library provides.

In order to use a lib you need to install a package. A lib is usually
put into a package.

To install a package you use package manager. In Python the package manager
is called `pip`.

Where do you find those packages?
- [https://pypi.org/](https://pypi.org/)

How do you install a package?
Use the command you find on the above website.
- `pip install sketchpy`

## Functions

The basic elements of every program are:
- control structures (loops, if conditions) + functions

simple function
`def my_function():`

- Functions have to be defined first.
- To use a function, you must call it.

### Parameter passing
- Giving a function some data, some information from outside the function.
- Information goes into a function with `parameters`.
- Information comes out of a function with `return values`.
- When we call a function with a parameter, we give it an actual parameter.

Example:
- `def my_function_with_params(name)` - Definition: (formal) parameter name
- `my_function_with_params("Emil")` - Call: actual parameter: "Emil"

## Data Types
What kinds of parameters are there?
- Strings: "Hello from a function !^"
  - They are quoted with "", '' (the same)
  - Strings are like text
- Numbers:
  - -1, 0, 1, 2, 3, ... (Integers)
  - 2.111, 0.5, 3.1413, 1343.5  , ... (Float, real numbers in math)

