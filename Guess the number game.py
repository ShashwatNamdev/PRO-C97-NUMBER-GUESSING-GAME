import random

realNumber = int(random.randint(1,9))
chances = int(0)

while chances <= 4:

    userNumber = int(input("Guess the number:- "))

    if userNumber < realNumber:
        print("Your guess was too low. Guess the number higher than ",userNumber)
        chances = chances + 1

    elif userNumber > realNumber:
        print("Your guess was too high. Guess the number lower than ",userNumber)
        chances = chances + 1

    elif userNumber == realNumber:
        print("Congratulations YOU WON!!!")
        chances = 6

if(chances == 5):
    print("You LOSE! The number was ",realNumber)
