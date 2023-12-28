import random #imported random module
content="  Rock Paper Scissor"#Heading
width=len(content)+4#Width for outline structure
horizontal_line="*"*width#outline border with star
print(horizontal_line)#printing top horizontal line
print(f'*{content}  *')# content between two horizontal line to show box structure
print(horizontal_line)#bottom horizontal line
count = 0#for user score count
ComputerCount = 0#for computer play count
store1 = []#for storing user choice 
store2 = []#for storing computer choice

def UserPlay():# user play def
    for i in range(10):#each 10 trail for user and computer 
        UserInput = input("Enter your choice /R/r/P/p/S/s:")#user input
        if UserInput in ["R", "r", "P", "p", "S", "s"]:# using condition to find input is right or wrong
            store1.append(UserInput)#storing values in user array store1
            ComputerPlay()# after 1 trail , computerplay start with this respective call function in condition
        else:
            print("Wrong Input")# if input is wrong
            break# breaking the function to avoid continue to next trail

def ComputerPlay():#computer def
    array = ["R", "P", "S"]#array to generate random value
    choice = random.choice(array)# using random function , generating random choice from array
    print("Computer choice:",choice)# printing computer choice
    store2.append(choice)# storing computer choice in store2
    WinnerCheck()# after 1 trail of computerplay , The Winnercheck function call to count the value

def WinnerCheck():#winner check def
    global count, ComputerCount  # Use the global variables 'count' and 'ComputerCount'
    user_choice = store1[-1]# getting last value from store1 
    computer_choice = store2[-1]#getting last value from store2
    #checking store1 and store2 choices of computer and user with condition (if and elif)
    if user_choice in ["R", "r"] and computer_choice in ["S"]:
        count += 1#adding value to user
        print("You win!")
    elif computer_choice in ["R"] and user_choice in ["S", "s"]:
        ComputerCount += 1#adding value to computer
        print("Computer wins!")
    elif user_choice in ["P", "p"] and computer_choice in ["S"]:
        ComputerCount += 1
        print("Computer wins!")
    elif computer_choice in ["P"] and user_choice in ["S", "s"]:
        count += 1
        print("You win!")
    elif computer_choice in ["S"] and user_choice in ["S", "s"]:
        print("Tie")
    elif user_choice in ["R", "r"] and computer_choice in ["P"]:
        ComputerCount += 1
        print("Computer win!")
    elif computer_choice in ["R"] and user_choice in ["P", "p"]:
        count += 1
        print("You win!")
    elif user_choice in ["P", "p"] and computer_choice in ["P"]:
        print("Tie")
    elif user_choice in ["R", "r"] and computer_choice in ["R"]:
        print("Tie")

UserPlay()#calling userPlay function

if ComputerCount > count:# checking, If computer score is high or not
    #if it's high this get implemeted
    print("Computer:", ComputerCount)
    print("User:", count)
    print("You Lost")
else:# if computer value is low than user
    #code get implemented
    print("Computer:", ComputerCount)
    print("User:", count)
    arr = ["You Win", "Bravo", "Congratulations", "Your Hero", "Good luck"]# creating array to generate random wishes
    wishes = random.choice(arr)#random choice
    print(wishes)#printing the wishes
    


