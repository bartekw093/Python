import random
import getpass as hide


print('choose game mode!')
print('1. VS computer')
print('2. Vs player')
game = int(input("Enter number of game mode: "))
if game == 1: #Player versus Computer
    number = random.randint(1,10)
    guess = 0
    counter = 0
    while number != guess:
        guess = int(input('have a try: '))
        if guess==number:
            print(f'Congratulations, you won! it only took you {counter} tries')
            break
        else:
            counter = counter + 1
            print(f'I\'m Sorry you failed again... for the {counter} time')
elif game == 2: #Player versus player
    print('Player 1 please enter number between 1 and 10 in pasword field')
    hiden = hide.getpass()
    hiden = int(hiden)
    guess = 0
    counter = 0
    while hiden != guess:
        guess = int(input('have a try: '))
        if guess==hiden:
            print(f'Congratulations, you won! it only took you {counter} tries')
            break
        else:
            counter = counter + 1
            print(f'I\'m Sorry you failed again... for the {counter} time')