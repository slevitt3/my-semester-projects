#sadielevitt

#january 13 2025
#Rock Paper Scissors
import random

def game():
    print("Welcome to Rock Paper Scissors!")
    human_choice=input("Please choose Rock, Paper, or Scissors")
    computer_choice=random.randint(1, 3)
    if computer_choice==1:
        result="RocK"
    if computer_choice==2:
        result="Paper"
    if computer_choice==3:
        result="Scissors"
    if human_choice == computer_choice:
        print("It's a... TIE!")
    if human_choice =="Rock" and computer_choice == "Paper":
        print("Computer WINS!")
    if human_choice =="Rock" and computer_choice == "Scissors":
        print("human WINS!")
    if human_choice =="Paper" and computer_choice == "Rock":
            print("human WINS!")
    if human_choice =="Paper" and computer_choice == "Scissors":
            print("Computer WINS!")
    if human_choice =="Scissors" and computer_choice == "Rock":
            print("computer WINS!")
    if human_choice =="Scissors" and computer_choice == "Paper":
            print("human WINS!")
game()
