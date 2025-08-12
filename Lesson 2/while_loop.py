number1 = input("Enter a number1: ")
number2 = input("Enter a number2: ")

while (number1 != number2) or True:
    # loop body
    print("while 1 loop is running")
    if number1 > number2:
        print(number1, "is greater than", number2)
    elif number1 < number2:
        print(number1, "is less than", number2)

    number1 = input("Enter a number: ")
    number2 = input("Enter a number: ")

print("while loop has stopped, the condition is false: number1 != number2")

# endless loop: it goes on forever
# you can stop the program by pressing CTRL+C
# "2 == 2" is always true, it evaluates to the same value a "True"
# "3 == 2" is always false, it evaluates to the same value a "False"
# not 3 == 2 is the same as "True".
while not 2 == 2: # True
    print("while 2 loop is running")
    number1 = input("Enter a number: ")
    number2 = input("Enter a number: ")

    if number1 > number2:
        print(number1, "is greater than", number2)
    elif number1 < number2:
        print(number1, "is less than", number2)
    else:
        print(number1, "is equal to", number2)

# this statement is not part of the while loop
print("Done")
