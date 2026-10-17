# Calculator :
    
while True :
    print("Python Calculator : \n")
    print("1. Addition \n")
    print("2. Subtraction \n")
    print("3. Multiplication \n")
    print("4.Division \n")
    print("5. Exit \n")
    
    choice = input("Enter your choice(1-5) :")
    
    if choice==5:
        print("Exiting calculator, Goodbye !")
        break
    
    if choice in ['1', '2', '3', '4']:
        x = input("Enter first number :")
        y = input("Enter second number :")
        
        num1 = int(x)
        num2 = int(y)
    if choice == '1':
        print("result :", num1 + num2)
        
    elif choice == '2':
        print("result :", num1 - num2)
        
    elif choice == '3':
        print("result :", num1 * num2)
        
    elif choice == '4':
        print("result :", num1 / num2)
        
    else:
        print("Invalid choice")
        
