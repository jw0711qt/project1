import random

counter=0

Input =  int(input(" I am thinking of a number between 1 and 10 " #this is the input where we need to put 
"\n (including both). Can you guess what it is\n"                   #any number
"Guess the number am thinking about"))
print("your guess is",Input)
dice=random.randint(1,10) # this is where the peogram generats numbers from 1 upto 10


while counter <3 : #this is tells us the program runs 3 times
    if dice == Input:# this is if the input is equal to randfom number then you win
        print("you win")
        break
    else:
        if dice > Input:
            result=dice - Input
            print("you are low by", result,"numbers")
            print("Game numberis ",dice)
        elif Input>dice:
            result=Input-dice
            print("you are high by", result,"numbers")
            print("Game numberis ",dice)
    counter+=1 #this is a counter counts how many times you run the program
    print("you have played", counter ," time")

         
    Input =  int(input(" I am thinking of a number between 1 and 10 "# this is the input if you don't win at 1st, and 2nd time
"\n (including both). Can you guess what it is\n"
"Guess the number am thinking about  "))
    print("your guessis",Input)
    dice=random.randint(1,10)

if Input==dice:
    print("congratulations your guess ",Input, "is equal to the  random number",dice)

if counter==3:
    print("you have reached the limit")

    

   
        
    

