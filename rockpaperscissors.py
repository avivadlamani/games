import random

while True:

    #input

    rishab = input("rock, paper, or scissors?\n").lower()

    #output

    choices = ["rock", "paper", "scissors"]

    sri = random.choice(choices)

    if rishab == "fuck you":

        print("please do")

        break

    if not rishab in choices:

        print("bro...")

        continue

    print("I play " + sri)
    
    if sri == "rock":

        if rishab == "rock":
            print("tie!")
        elif rishab == "paper":
            print("you win")
        elif rishab == "scissors":
            print("you lose")
   
    elif sri == "paper":

        if rishab == "rock":
            print("you lose!")
        elif rishab == "paper":
            print("tie!")
        elif rishab == "scissors":
            print("you win")
  
    elif sri == "scissors":

        if rishab == "rock":
            print("you win")
        elif rishab == "paper":
            print("you win")
        elif rishab == "scissors":
            print("tie")

    print()
