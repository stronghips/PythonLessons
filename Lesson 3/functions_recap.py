
# function
def print_string(my_str = "lol"):   # my_str is a function parameter and a local variable inside of the function
    count = 0
    while count < 10:
        count = count + 1
        if True:
            print(str(count) + " " + my_str)


print_string("my_new_str")  # function call


def format_string(my_str):
    return "***_" + my_str + "_***"   # return value of the function

# store function return value in a variable
return_val = format_string("blabla")
return_val = "###" + return_val + "###"
print(return_val)

print(format_string("hello"))  # return value of a function is the input parameter of the next function

# this is called
# function composition
# also: nested / chained function calls
