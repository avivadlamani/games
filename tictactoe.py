#functions

import random

def printgrid (grid):
     for x in range(3):
        

        for y in range(3):

            print(grid[x][y] + "|", end = "")

        print()

def checkwin (grid):

    for rows in range (3):

        if grid[rows][0] == "x" and grid[rows][1] == "x" and grid[rows][2] == "x":

            print("you win!")

            return True

        if grid[rows][0] == "o" and grid[rows][1] == "o" and grid[rows][2] == "o":

            print("computer wins!")

            return True

    for columns in range (3):

        if grid[0][columns] == "x" and grid[1][columns] == "x" and grid[2][columns] == "x":

            print("you win!")

            return True

        if grid[0][columns] == "o" and grid[1][columns] == "o" and grid[2][columns] == "o":

            print("computer wins!")

            return True

    if grid[0][0] == "x" and grid[1][1] == "x" and grid[2][2] == "x":

        print ("you win!")

        return True

    elif grid[0][2] == "x" and grid[1][1] == "x" and grid[2][0] == "x":

        print ("you win!")

        return True
    
    elif grid[0][0] == "o" and grid[1][1] == "o" and grid[2][2] == "o":

        print ("computer wins!")

        return True

    elif grid[0][2] == "o" and grid[1][1] == "o" and grid[2][0] == "o":

        print ("computer wins!")

        return True
    
    else:

        return False


#game

print("Welcome to tic tac toe! You are x.")

grid = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]

while True:

    #input

    rows = 0
    columns = 0
    try:

        while True:

            rows = int(input("x coord? "))

            if not rows in (0,1,2):
                print("Please use 0, 1, or 2")
                continue

            else:
                break

        while True:
    
            columns = int(input("y coord? "))

            if not columns in (0,1,2):
                print("Please use 0, 1, or 2")
                continue

            else: 
                break

        if not grid[rows][columns] == " ":
            print("That space is already used")
            continue

        grid[rows][columns] = "x"

    except:

        print("Are you stupid?")

        continue

    #computer's turn

    while True:

        comprows = random.randint(0,2)
        compcolumns = random.randint(0,2)

        if grid[comprows][compcolumns] == " ":

            grid[comprows][compcolumns] = "o"

            break

    printgrid(grid)

    #output
    
    print()

    #checkwin
        
    if checkwin (grid):

        break