#Kaylie Yuen
#AP CSP, P1
#Multiplication Quiz Project
#January 8, 2025

#initialize
import random
import time

#functions

global score
score = 0

def quiz():
    difficulty = int(input("Please choose a difficulty: (1) Easy, (2) Normal, or 3 (Hard). "))
    question_number = int(input("How many questions do you want to answer? "))

    if difficulty == 1:
        score = 0
        start_time = time.time()
        for i in range(question_number):
            factor_1 = random.randint(0, 10)
            factor_2 = random.randint(0, 10)
            answer = factor_1 * factor_2
            student_answer = int(input("What is " + str(factor_1) + " times " + str(factor_2) + "? "))
            if student_answer == answer:
                print("Congratulations! That's correct.")
                score = score + 1
            else:
                print("Not quite...")
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_round = round(elapsed_time, 2)
        print("Your final score is " + str(score) + " out of " + str(question_number) + " correct on EASY difficulty!")
        print("It took you " + str(elapsed_time_round) + " seconds to finish the quiz!")

    elif difficulty == 2:
        score = 0
        start_time = time.time()
        for i in range(question_number):
            factor_1 = random.randint(-12, 12)
            factor_2 = random.randint(-12, 12)
            answer = factor_1 * factor_2
            student_answer = int(input("What is " + str(factor_1) + " times " + str(factor_2) + "? "))
            if student_answer == answer:
                print("Congratulations! That's correct.")
                score = score + 1
            else:
                print("Not quite...")
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_round = round(elapsed_time, 2)
        print("Your final score is " + str(score) + " out of " + str(question_number) + " correct on NORMAL difficulty!")
        print("It took you " + str(elapsed_time_round) + " seconds to finish the quiz!")

    else:
        score = 0
        start_time = time.time()
        for i in range(question_number):
            factor_1 = random.randint(-50, 50)
            factor_2 = random.randint(-50, 50)
            answer = factor_1 * factor_2
            student_answer = int(input("What is " + str(factor_1) + " times " + str(factor_2) + "? "))
            if student_answer == answer:
                print("Congratulations! That's correct.")
                score = score + 1
            else:
                print("Not quite...")
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_round = round(elapsed_time, 2)
        print("Your final score is " + str(score) + " out of " + str(question_number) + " correct on HARD difficulty!")
        print("It took you " + str(elapsed_time_round) + " seconds to finish the quiz!")

def final_quiz():
    print("\nWelcome to the multiplication quiz, where you test your abilities in multiplication!\n")
    quiz()
    while True:
            play_again = input("Quiz again? (Y/N) ")
            if play_again.upper() == "Y":
                quiz()
            else:
                print("This quiz has ended! Thanks for testing your math skilL!")
                break

#main

final_quiz()


