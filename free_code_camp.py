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
# # to run this code copy and paste to your terminal =>> python free_code_camp.py

# tc_mc_task 1
# # Q7
# name, age, height = "Azeez", 28, 5.10

# print(name)
# print(age)
# print(height)

# # Q8
# num_str = "123"
# num_int = int(num_str)

# sum = num_int + 50
# print(sum)
# print(type(sum))

# num_str = str(sum)
# print(num_str)
# print(type(num_str))

# # Q9
# product, price, quantity = "laptops", 999.99, 3
# total_cost = price * quantity
# total_cost = round(total_cost, 2)

# print(f"Buying {quantity} {product} will cost me {total_cost}")

# # Q10
# score =100
# print(type(score))

# score = "High Score"
# print(type(score))

# score = True
# print(type(score))
