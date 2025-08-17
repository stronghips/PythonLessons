# Interaction with computer: command line
# Input / output system: command line

import random

# define global array of options (element 0: 'rock', element 1: 'paper', element 2: 'scissors')
# arrays have elements of the same type
options = ['rock', 'paper', 'scissors']

def GetUserChoice():
    user_choice = input('Enter your choice (rock, paper, scissors, q - quit): ')
    return user_choice

def GetComputerChoice():
    computer_choice = random.choice(options)
    return computer_choice

def CalculateWinner(user_choice, computer_choice):
    print('Computer chose: ', computer_choice)
    if user_choice == computer_choice:
        print('It\'s a tie!')
    # operand1 or operand2 or operand3
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win!')
    else:
        print('You lose!')

def StartGame():
    user_choice = GetUserChoice()
    if user_choice == 'q':
        exit()

    if user_choice not in options:
        print('Invalid choice. Please choose rock, paper or scissors.')
        return

    computer_choice = GetComputerChoice()
    CalculateWinner(user_choice, computer_choice)

# main entry point of the program
if __name__ == "__main__":
    while True:
        StartGame()