#Kaylie Yuen
#January 6, 2025
#Period 1
#AP CSP

#initialize
import random

#functions

def FINAL_GAME():
    print("\nLet's play rock, paper, scissors! Test your chances -- play against the computer! \n")
    rock_paper_scissors()
    while True:
        play_again = input("Play again? (Y/N) ")
        if play_again == "Y":
            rock_paper_scissors()
        else:
            print("This game has ended! The final scores are: ")
            print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE " + str(computer_win))
            break


player_win = 0
computer_win = 0

def rock_paper_scissors():
    global computer_win
    global player_win
    player_move = int(input("Do you want to play rock (1), paper (2), or scissors (3)? "))
    if player_move == 1:
        print(""" You have played ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif player_move == 2:
        print(""" You have played PAPER!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        print(""" You have played SCISSORS!)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    computer_move = random.randint(1, 3)
    if computer_move == 1:
        print(""" Computer has played ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif computer_move == 2:
        print(""" Computer has played PAPER!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        print(""" Computer has played SCISSORS!)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    if player_move == 1 and computer_move == 2:
        print("You have played rock, and the computer has played paper! Paper covers rock, you LOSE! TRY AGAIN")
        computer_win = computer_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    elif player_move == 1 and computer_move == 3:
        print("You have played rock, and the computer has played scissors. Rock smashes scissors, YOU WIN!")
        player_win = player_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    elif player_move == 2 and computer_move == 1:
        print("You have played paper, and the computer has played rock! Paper covers rock, YOU WIN!")
        player_win = player_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    elif player_move == 2 and computer_move == 3:
        print("You have played paper, and the computer has played scissors! Scissors cuts paper, you LOSE! TRY AGAIN")
        computer_win = computer_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    elif player_move == 3 and computer_move == 1:
        print("You have played scissors, and the computer has played rock! Rock smashes scissors, you LOSE! TRY AGAIN")
        computer_win = computer_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    elif player_move == 3 and computer_move == 2:
        print("You have played scissors, and the computer has played paper. Scissors cuts paper, YOU WIN!")
        player_win = player_win + 1
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))
    else:
        print("You and the computer played the same move -- TIE! PLAY AGAIN")
        print("\nPLAYER SCORE: " + str(player_win) + " COMPUTER SCORE: " + str(computer_win))

#main

FINAL_GAME()

