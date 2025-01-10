#Kaylie Yuen
#November 11
#AP CSP

import random


#functions
def game_medium():
    x = int(input("Guess a number between 0 and 10! "))
    y = random.randint(0,10)
    lives = 2
    for i in range(2):
        if x > y:
            lives == lives - 1
            print("Too high! Try lower. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 10! "))
        if x < y:
            lives == lives - 1
            print("Too low! Try higher. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 10! "))
        elif x == y:
            print("Congratulations! You have guessed the nunber! :)")
            break
        elif x != y or lives == 0:
            print("WRONG! The correct number is " + str(y) + ". You're out of lives! GAME OVER")

def game_easy():
    x = int(input("Guess a number between 0 and 5! "))
    y = random.randint(0,5)
    lives = 2
    for i in range(2):
        if x > y:
            lives == lives - 1
            print("Too high! Try lower. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 5! "))
        if x < y:
            lives == lives - 1
            print("Too low! Try higher. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 5! "))
        elif x == y:
            print("Congratulations! You have guessed the nunber! :)")
            break
        elif x != y or lives == 0:
            print("WRONG! The correct number is " + str(y) + ". You're out of lives! GAME OVER")

def game_hard():
    x = int(input("Guess a number between 0 and 15! "))
    y = random.randint(0,15)
    lives = 2
    for i in range(2):
        if x > y:
            lives == lives - 1
            print("Too high! Try lower. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 15! "))
        if x < y:
            lives == lives - 1
            print("Too low! Try higher. You have " + str(lives) + " lives left.")
            x = int(input("Guess a number between 0 and 15! "))
        elif x == y:
            print("Congratulations! You have guessed the nunber! :)")
            break
        elif x != y or lives == 0:
            print("WRONG! The correct number is " + str(y) + ". You're out of lives! GAME OVER")

#main

print("Welcome to the Random Number Guessing Game! Guess a number, test your chances! You'll have 3 lives to guess correctly.")

difficulty = input("First, pick a difficulty level: easy (e), medium (m), or hard (h)? ")
if difficulty == "e":
    game_easy()
elif difficulty == "m":
    game_medium()
elif difficulty == "h":
    game_hard()
