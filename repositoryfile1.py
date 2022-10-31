ad_infinitum = None

while ad_infinitum != 0:
    try:
        user_choice = int(input("Menu\n---------------\n1. Addition\n2. Subtraction\n\nWhich do you want to do? "))
        if user_choice != 1 and user_choice != 2:
            raise ValueError("That was neither 1 nor 2 man...")
        if user_choice == 1:
            oper_one = int(input("What is your first number? "))
            oper_two = int(input("What is your second number? "))
            result = oper_one + oper_two
            print("The sum of the two numbers you granted is", result)
        if user_choice == 2:
            oper_one = int(input("What is your first number? "))
            oper_two = int(input("What is your second number? "))
            result = oper_one - oper_two
            print("The difference of the two numbers you granted is", result)
        break
    except ValueError as error:
        print(str(error))
    except:
        print()
        print("You backed out of the prompt. Why? Why would you do that?")
        print("Is this a joke to you? Try again man... for shame!")
        print()

