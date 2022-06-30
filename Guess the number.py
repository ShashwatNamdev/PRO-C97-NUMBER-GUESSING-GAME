import random

actualNumber = random.randrange(0,9)
userNumber = int(input("Enter your guess:- "))
chances = 0
if userNumber < actualNumber:
    print("Your guess was too low: Guess a number higher than " + userNumber)
    chances += 1
elif userNumber > actualNumber:
    print("Your guess was too high: Guess a number lower than " + userNumber)
    chances += 1
else:
    print("Congratulation YOU WON!!!")

for i in chances:
    if not chances < 5:
        print("YOU LOSE!!! The number is:- " + actualNumber)

