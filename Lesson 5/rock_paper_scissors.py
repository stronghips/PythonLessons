import random

def rock_paper_scissors():
    # Define the options
    options = ['rock', 'paper', 'scissors']

    # Computer makes a choice
    computer_choice = random.choice(options)

    # User makes a choice
    user_choice = input('Enter your choice (rock, paper, scissors): ')

    # Check if user's input is valid
    if user_choice not in options:
        print('Invalid choice. Please choose rock, paper or scissors.')
        return

    # Determine the winner
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win!')
    else:
        print('You lose!')

    print('Computer chose: ', computer_choice)

# Run the game
rock_paper_scissors()