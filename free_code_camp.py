import random


def greeting(player):
    print(f"H3ll0 {player} Welcome to the G4M3")

def get_choice():
    player_choice = input("Enter Your Choice(rock, paper, scissors)")
    game_option =["rock" , "paper" , "scissors"]
    computer_choice = random.choice(game_option)
    choices = {"player" : player_choice , "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Your chose {player}, while Computer choose {computer}")
    if player == computer:
        return "its a tie!!"
    elif player == "rock":  # writing comparisons of player palying rock
        if computer == "paper":
            return "Paper covers rock Computer WINS :("
        elif  computer == "scissors":
            return "Rock breaks scissors Player WINS!!"
    elif player == "paper":  # writing comparisons of player palying paper
        if computer == "rock":
            return "Paper covers rock Player WINS!!"
        elif computer == "scissors":
            return "Scissors cuts Paper Computer WINS:("
    elif player == "scissors":   # writing comparisons of player palying scissors
        if computer == "rock":
            return "Rock breaks scissors Computer WINS:("
        elif computer == "paper": 
            return "Scissors cuts Paper Player WINS!!"
    else : print("Go again")

greeting(input("What is Your G4M3R T4G "))
choices = get_choice()
result = check_win(choices["player"], choices["computer"])

print(result)





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

# Tc_Mc Task 2 
# Q7
# a = input("Enter first Number: ")
# a = int(a.strip())
# b = input("Enter second number: ")
# b = int(b.strip())

# def addition():
#     print(a + b)
# def subtraction():
#     print(a - b)
# def multiply():
#     print(a * b)
# def divide():
#     print(a / b)

# addition()
# subtraction()
# multiply()
# divide()

# # Q8
# user_score = input("Enter student score: ")
# user_score = int(user_score.strip())

# if user_score > 100 or user_score < 0:
#     print(f"Enter Valid Score: {user_score} is Invalid")

# if user_score >= 90 and user_score <=100:
#     print("A")
# elif user_score < 90 and user_score >= 80:
#     print("B")
# elif user_score < 80 and user_score >= 70:
#     print("C")
# elif user_score < 70 and user_score >= 60:
#     print("D")
# else:
#     print ("F")
# # Q9
# sentence = input("Enter your sentence")
# sentence = sentence.strip()

# vowels = "aeiou"
# for vowel in vowels:
#     print(f"{vowel} : {sentence.count(vowel)}")
# if len(sentence) > 20:
#     print(f"True the sentence is {len(sentence)} and is longer than 20")
# else:
#     print("False")

# print(sentence.title())



