import random

computer = random.choice([-1,0,1])
your = input("Enter any letter")
yourdic = {"s":1 ,"p":0,"r":-1}
reversedic = {1:"snack", 0:"paper" ,"rock":-1}
 
you = yourdic[your]

print(f"You chose {reversedic[you]}\n computer chose {reversedic[computer]}")

if(computer == you):
    print("tie")

else:
    if(computer ==1  and you == 0):
        print("You win !")

    elif(computer == 1 and you == -1):
        print("You lose !")

    elif(computer ==  0 and you ==  1):
        print("You  lose !")

    elif(computer ==  0 and you ==  -1):
        print("You won !")
    
    elif(computer ==  -1 and you == 1 ):
        print("You lose !")

    elif(computer ==  -1 and you == 0 ):
        print("You win !")
