def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b  

def per(a):
    return a / 100


print("Welcome to my simple Python Calculator! Please select an option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Percentage")

while True:
    user_choice = input("Enter your option choice: 1, 2, 3, 4, or 5") 
    if user_choice == "1":
        try:
            int1 = float(input("With no punctuation, enter the first number to be calculated: "))
            int2 = float(input("With no punctuation, enter the second number to be calculated: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
    elif user_choice == "2": 
            try: 
                 int1 = float(input("With no punctuation, enter the first number to be calculated: "))
                 int2 = float(input("With no punctuation, enter the second number to be calculated: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
    elif user_choice == "3": 
            try: 
                 int1 = float(input("With no punctuation, enter the first number to be calculated: "))
                 int2 = float(input("With no punctuation, enter the second number to be calculated: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
    elif user_choice == "4": 
            try: 
                 int1 = float(input("With no punctuation, enter the first number to be calculated: "))
                 int2 = float(input("With no punctuation, enter the second number to be calculated: "))
            except ValueError:
                print("Please enter a valid number!")
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                continue
    elif user_choice == "5": 
            try: 
                 perc = float(input("With no punctuation, enter the percentage to be calculated: "))
            except ValueError:
                print("Please enter a valid number!")
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                continue
    else:
         print("Please enter a valid choice!")
         continue
            
    if user_choice == "1": 
        print(int1, "+", int2, "=", add(int1, int2))
    elif user_choice == "2":
        print(int1, "-", int2, "=", sub(int1, int2))
    elif user_choice == "3":
        print(int1, "*", int2, "=", mult(int1, int2))
    elif user_choice == "4":
        print(int1, "/", int2, "=", div(int1, int2)) 
    elif user_choice == "5":
        print(perc, "/", "100", "=", per(perc), "%")
        
    while True:
        next_calculation = input("Calculate another equation? Y/N?")
        if next_calculation == "Y" or next_calculation == "y":
             break
        elif next_calculation == "N" or next_calculation == "n":
             print("Thank you for using my simple Python calculator. :)")
             continue
             
