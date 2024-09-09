#rock paper scissor game
import random

def our_choice():
    user_choice = input("enter your choice (rock or paper or scissor) =")
    while(user_choice not in ["rock","paper","scissor"]):
        user_choice = input("enter your choice (rock or paper or scissor) =")
    return user_choice

def machine_choice():
    return random.choice(["rock","paper","scissor"])

def win(user_choice, computer_choice ):
    if(user_choice == computer_choice ):
        return "tie"
    elif((user_choice == "rock" and computer_choice == "paper") or 
         (user_choice == "paper" and computer_choice == "scissor") or 
         (user_choice == "scissors" and computer_choice == "rock")):
        return "computer"
    else:
        return "user"

def result(user_choice, computer_choice ,winner):
    print("our choice =", user_choice)
    print("machine choice =", computer_choice )
    if(winner == "tie"):
        print("tie")
    elif(winner == "computer"):
        print("you loss")
    else:
        print("you win")

def main():
    user = 0
    computer = 0

    while True:
        user_choice = our_choice()
        computer_choice = machine_choice()
        winner = win(user_choice,computer_choice)
        result(user_choice,computer_choice,winner)

        if(winner == "computer"):
            computer += 1
        elif(winner == "user"):
            user += 1

        print("user score =",user)
        print("computer score =",computer)

        once_again=input("do you what play once more?(yes/no) = ")
        if(once_again == "no"):
           break

    print("thanks for playing")

if __name__=="__main__":
    main()