import random
secret_number=random.randint(0,10)
game=input('Enter a Number:')
if game==secret_number:
    print('Congratulations! You guessed right')
else:
    print('ohhoo!Try again')