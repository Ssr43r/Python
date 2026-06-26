while True:
    print("Calculater")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. ÷")
    print("5.exit")

    choice = input("Choose menu ").strip()
#Plus
    if choice in ("1" , "+"):
        while True:
            print("Plus")
            try:
                num1 = float(input("First Num "))
                num2 = float(input("Second Num "))
                w = input("if you want to stop type (yes) but you don't stop press Enter ").lower()
                if w == "yes":
                    break
                print(f"{num1} + {num2} = {num1 + num2}")
            except ValueError:
                print("Number only!!!")
#Negative
    elif choice in ("2" , "-"):
        while True:
                print("Nagative")
                try:
                    num1 = float(input("First Num "))
                    num2 = float(input("Second Num "))
                    w = input("if you want to stop type (yes) but you don't stop press Enter ").lower()
                    if w == "yes":
                        break
                    print(f"{num1} - {num2} = {num1 - num2}")
                except ValueError:
                    print("Number only!!!")
#Times
    elif choice in ("3" , "x"):
        while True:
                print("Times")
                try:
                    num1 = float(input("First Num "))
                    num2 = float(input("Second Num "))
                    w = input("if you want to stop type (yes) but you don't stop press Enter ").lower()
                    if w == "yes":
                        break
                    print(f"{num1} x {num2} = {num1 * num2}")
                except ValueError:
                    print("Number only!!!")
#divide by
    elif choice in ("4" , "÷"):
        while True:
                print("Divide by")
                try:
                    num1 = float(input("First Num "))
                    num2 = float(input("Second Num "))
                    w = input("if you want to stop type (yes) but you don't stop press Enter ").lower()
                    if w == "yes":
                        break
                    print(f"{num1} ÷ {num2} = {num1 / num2}")
                except ValueError:
                    print("Number only!!!")
#exit                    
    elif choice in ("5" , "exit"):
         print("End Program")
         break
    else:
         print("Read menu again!!!")
         continue
    