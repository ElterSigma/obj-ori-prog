class Calculator:
    
    def fAddition(lst):
        print(sum(lst))
    
    def fSubtraction(lst):
        a = lst.pop(0)
        if not lst == False:
            b = lst.pop(0)
            a -= b
        
        print(a)
    
    def fMultiplication(lst):
        a = lst.pop(0)
        if not lst == False:
            b = lst.pop(0)
            a *= b
        
        print(a)
    
    def fDivision(lst):
        a = lst.pop(0)
        if not lst == False:
            b = lst.pop(0)
            a /= b
        
        print(a)
    
    while True:
        numList = []
        
        y = int(input("How many numbers would you like to use?: "))
        while y >= 1:
            x = float(input("Type a number: "))
            numList.append(x)
            y -= 1
        
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
        choice = input("Choose a function: ")
            
        if choice == '1':
            fAddition(numList)
        
        elif choice == '2':
            fSubtraction(numList)
        
        elif choice == '3':
            fMultiplication(numList)
        
        elif choice == '4':
            fDivision(numList)
        
        else:
            print("Error! Please choose a valid option!")


