import random

def greeting(player):
    print(f"H3ll0 {player} Welcome to the G4M3")

def get_choice():
    player_choice = input("Enter Your Choice(rock, paper, scissors)")
    game_list =["rock" , "paper" , "scissors"]
    computer_choice = random.choice(game_list)
    choices = {"player" : player_choice , "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Your choice {player}, while Computer choice {computer}")
    if player == computer:
        return "its a tie!!"
    






greeting(input("What is Your G4M3R T4G "))
check_win("rock", "rock")
# to run this code copy and paste to your terminal =>> python free_code_camp.py