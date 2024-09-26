#Loop program over until all checks are positive.
x = 0
while x == 0:
    #Receives the inputs from users
    yCoffee = input("How many coffee(s) would you like: ")
    yMuffin = input("How many muffin(s) would you like: ")
    yBagel = input("How many bagel(s) would you like: ")
    yTea = input("How many tea(s) would you like: ")


    #By default we set valid to avoid future errors.
    validInt = False


    #If we can type convert from int to string valid int then becomes True which allows us to continue.
    try:
            xCoffee = int(yCoffee)
            xMuffin = int(yMuffin)
            xBagel = int(yBagel)
            xTea = int(yTea)
            validInt = True


    #Prints an error statement if we cannot type convert.
    except:
            print("Please enter values as a valid int.")


    #Checks to see if the inputs are valid.
    if validInt == False:
        "Enter a valid digit"


    #Valid input checking.
    elif validInt == True and xCoffee < 0 or xMuffin < 0 or xBagel < 0 or xTea < 0:
        print("Please enter a valid number for purchasing")


    #If inputs are valid the program begins to calculate costs
    elif validInt == True:
        #Calculating charges
        cTotal = xCoffee * 5
        mTotal = xMuffin * 4
        bTotal = xBagel * 3
        tTotal = xTea * 2
        TAX_RATE = (cTotal + mTotal + bTotal + tTotal) * 0.06
        total = cTotal + mTotal + bTotal + tTotal + TAX_RATE


        #Formatting/Printing our values in a f-string.
        receipt = ("***************\nMy Coffee and Muffin shop reciept:"
        +"\n {} Coffee(s) at $5 each:${} \n {} Muffin(s) at $4 each:${}" 
        +"\n {} Bagel(s) at $3 each: ${}\n {} Tea(s) at $2 each:{}\n 6% Tax at :${} \n Total:${}\n").format(xCoffee, cTotal, xMuffin, mTotal, xBagel, bTotal, xTea,tTotal, TAX_RATE, total)
        print(receipt)
        print("\nThank you for shopping with us!!!\n***************")
        
        
        #If all checks are valid then we set x to 1 which breaks the looping mechanism.
        x = 1
        
