###guess_number.py
##This program guesses the number that the user is thinking. It is a way to test the bisection algorithms

print('Please think of a number between 0 and 100!')
high=100
low=0
user_answer = 'c'
guess=int(low+(high-low)/2)


while True:
    print('Is your secret number ', guess,'?')
    user_answer=input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly ')
    
    if user_answer == 'c':
        break
    elif user_answer == 'h':
        high=guess
    elif user_answer == 'l':
        low=guess
    else:
        print('Sorry, I did not understand your input')
    guess=int(low+(high-low)/2)
print('Game over. Your secret number was: ', guess)