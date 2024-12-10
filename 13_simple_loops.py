# for Loops
for i in range(5):
    print(i)

listOfThings = ["apple", "mango", "cheese", "orange"]
for food in listOfThings:
    print(food)

listOfNumbers = [3, 1, 2, 90, 343]
for num in listOfNumbers:
    print(num)


# while Loops 
count = 0
while count < 5:
    print(count) # action before update
    count += 1 # never forget your increment else it will run forever
    # print(count) # action after update
    if(count == 3):
        continue
        # break
    # actions to do here after skip

    
# break - end the loop
# continue - skip over a part of the loop


# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 13_simple_loops.py