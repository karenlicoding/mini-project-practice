import random

#computer's number
#enter number
hight = "Too hight, try again!"
low = "Too low, try again!"
goodbye = "Thanks for playing. Bye"
cpnumber = random.randint(1, 10)

while True: #可以直接進行迴圈
    #check number
    guessnumber = int(input("guess a number between 1 and 10:"))
    if cpnumber < guessnumber:
        print(hight)
        
    elif cpnumber > guessnumber: 
        print(low)

    else:    
        print("You guessed it! You won")
        print(cpnumber)
        answer = input("Do you want to keep playing? (y/n)").lower()
        if answer == "y":
            cpnumber = random.randint(1, 10)
        #ask try again
        else:
            print(goodbye)
            break    #最內迴圈中斷往上延續中斷全部迴圈


    

