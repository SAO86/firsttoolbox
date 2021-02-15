
import random

def get_random_number():
     number = random.randrange(0, 9, 1)
     return number


def guess_number():
    number=get_random_number()
    guess = input('Please enter an integer between 0 and 9 :')

    if number == guess:
        print('YOU WIN!')
    else:
        print('GAME OVER')



