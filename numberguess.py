import random
import time


x = 1,2,3,4,5,6,7,8,9,10
y = random.choice(x)
def givequestion():
    print("hello welcome to a number guessing game!")
    time.sleep(3)
    consent = input("Do you want to play the game (respond with Y/N):")
    if consent != "Y":
        quit()

    guess = input("Guess the number between 1-10! :")
    if guess != y:
        print("you got the wrong answer! , the correct answer is " + str(y))
