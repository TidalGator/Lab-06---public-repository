ad_infinitum = None

while ad_infinitum != 0:
    try:
        oper_one = int(input("What is your first number? "))
        oper_two = int(input("What is your second number? "))
        result = oper_one + oper_two
        print("The sum of the two numbers you granted is", result)
        break
    except:
        print("You backed out of the prompt. Why? Why would you do that?")
        print("Is this a joke to you? Try again man... for shame!")

