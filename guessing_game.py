secret_number = 9
i=0
isWin = False
while i<3:
    guess_number = int(input("Guess: "))
    if guess_number==9:
        print("You Win!")
        isWin = True
        break
    else:
        i+=1

if not isWin:
    print("You Failed!")
        
