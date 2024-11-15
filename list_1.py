question_1 = input("You wanna see how works list in python?(yes/no): ")
if question_1 == "yes":
    print("Nice! Lets start")
elif question_1 == "no":
    print("That was so sad :()")
    exit()
else:
    print("Invalid value")
    exit() 
while True:
    try:
        count_1 = int(input("Enter first count: "))
        count_2 = int(input("Enter second count: "))
        count_3 = int(input("Enter third count: "))
        count_4 = int(input("Enter fourth count: "))
        count_5 = int(input("Enter fifth count: "))
        user_decision = input("You wanna correct your counts?(yes/no): ")
        if user_decision == "yes":
            continue
        elif user_decision == "no":
            break
    except ValueError:
        print("Invalid value! Please enter numbers only")
        continue
question_2 = input("Are you ready for avtivities on your counts?")
if question_2 == "yes":
    print("Let's start!")
elif question_2 == "no":
    print("Ok...")
    exit()
else:
    print("Invalid value")
    exit()    
numbers = [count_1, count_2, count_3, count_4, count_5]    
question_3 = ("What do you want to do with your counts?")
#in progress