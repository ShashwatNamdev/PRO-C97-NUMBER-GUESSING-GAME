import random
from urllib.parse import uses_fragment

realNumber = int(random.randint(1,7))
userNumber = int(input("Guess the number:- "))
chances = 0

if userNumber < realNumber:
    print("Your guess was too low. Guess the number higher than ",userNumber)
    chances += 1
    userNumber

if userNumber > realNumber:
    print("Your guess was too high. Guess the number lower than ",userNumber)
    chances += 1
    userNumber

if userNumber == realNumber:
    print("Congratulations YOU WON!!!")

if chances == 5:
    print("YOU LOSE!!! The number was ",realNumber)