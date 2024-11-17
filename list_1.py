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
while True:
    question_3 = input("What do you want to do with your counts?(add/remove/clear/exit): ")
    if question_3 == "add":
        try:
            value = int(input("Enter count which you wanna add: "))
            numbers.append(value)
            print(numbers)
        except ValueError:
            print("Invalid value, please try one more.")
    elif question_3 == "remove":
        try:
            value_2 = int(input("Which count you wanna remove? "))
            if value_2 in numbers:
                numbers.remove(value_2)
                print(numbers)
            else: 
                print("Count not found on the list, enter count one more time.")    
        except ValueError:
            print("Invalid value, please try one more.")
    elif question_3 == "clear":
            numbers.clear()
            print(numbers)
    elif question_3 == "exit":
        print("Exiting...")
        break        
    else:
        print("Invalid option. Please choose add/remove/clear")
