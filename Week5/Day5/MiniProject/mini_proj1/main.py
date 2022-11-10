import random

r_p_s = ["Rock", "Paper", "Scissors"]

my_points = 0
computer_points = 0
shared_points = 0

def play():
    play = input("Do you want to play?")

    if play == "yes":
        actual_game()

    else:
        print("See you next time")

def actual_game():
    user = input("Rock, Paper, Scissors:")
    computer = random.choice(r_p_s) 

    if user == "Rock" and computer == "Paper":
        print(f"you chose {user} the computer chose {computer} you lose")
        computer_points + 1
        play_again()
    elif user == "Rock" and computer == "Scissors":
        print(f"you chose {user} the computer chose {computer} you win!")
        my_points + 1
        play_again()
    elif user == "Paper" and computer == "Rock":
        print(f"you chose {user} the computer chose {computer} you win!")
        my_points + 1
        play_again()
    elif user == "Paper" and computer == "Scissors":
        print(f"you chose {user} the computer chose {computer} you lose")
        computer_points + 1
        play_again()
    elif user == "Scissors" and computer == "Rock":
        print(f"you chose {user} the computer chose {computer} you lose")
        computer_points + 1
        play_again()
    elif user == "Scissors" and computer == "Paper":
        print(f"you chose {user} the computer chose {computer} you win!")
        my_points + 1
        play_again()
    elif user == "Rock" and computer == "Rock":
        print(f"you chose {user} the computer chose {computer} its a tie!")
        shared_points + 1
        play_again()
    elif user == "Paper" and computer == "Paper":
        print(f"you chose {user} the computer chose {computer} its a tie!")
        shared_points + 1
        play_again()
    elif user == "Scissors" and computer == "Scissors":
        print(f"you chose {user} the computer chose {computer} its a tie!")
        shared_points + 1
        play_again()

def play_again():
    play_again = input("Do you want to play again?")

    if play_again == "yes":
        actual_game()

    else:
        print(f"your points:{my_points} computers points:{computer_points} shared points:{shared_points}")

play()

