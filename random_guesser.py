#importing random module

import random

#generating a random number
random_number =random.randint(1,100)


chance = 10
flag = False
while (flag != True):
    if (chance == 0):
        print("You have exhausted all your chances.")
        break
    guess = int(input("guess the number between 1 to 100: "))

    if (guess > 100 or guess < 1):
        print(f"Your choosen number {guess} not between 1 or 100.")
    elif (random_number == guess):
        flag = True
        print(f"Congratulation! You have guessed the number.")
    elif(random_number > guess):
        chance -=1
        print(f"Your number less than actual number. You have {chance} more chances left.")
    elif(random_number < guess):
        chance -=1
        print(f"Your number greater than actual number. You have {chance} more chances left.")