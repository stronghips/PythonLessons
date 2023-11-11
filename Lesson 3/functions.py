from turtle import color, right, forward # * we import from the lib turtle everything

# Definition of a function
def my_function():
    print("Hello from a function")

# To use a function, you must call it.
my_function()

# Functions with parameters: info goes into the function
# Parameter passing: giving a function some data, some information from outside the function
def my_function_with_params(name):
    print(name + " called the function")

my_function_with_params("Emil")
my_function_with_params("Ermis")

def my_function_with_two_params(param1, param2):
    print(param1 + " " + param2)

my_function_with_two_params("value1", "value2")

# Functions with return values: info comes out of a function
def my_function_with_return_value():
    return "Hello from my_function_with_return_value"

# get the return value out of the function
ret_value = my_function_with_return_value()
ret_value = ret_value + " and more"
print(ret_value)

# in Python, you can return multiple values from a function
def my_function_with_multiple_return_values():
    return "Hello", "World"

ret_value1, ret_value2 = my_function_with_multiple_return_values()
print(ret_value1 + " between " + ret_value2)

# the inside of function (loop, if statement has to be indented "    " - 4 spaces)
def draw(iterations):
    for steps in range(1, iterations):
        # a nested loop: 3 iterations
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps) # length of the line: 1, 2, 3, ..., 100
            right(30) # change the direction by 30 degrees

interations = input("specify iterations: ")
draw(int(interations))

input("press enter to exit")