while True:
    try:
        fruit_1 = input("Enter first fruit: ")
        fruit_2 = input("Enter second fruit: ")
        fruit_3 = input("Enter third fruit: ")
    
        fruits = [fruit_1, fruit_2, fruit_3]
        if "banana" in fruits:
            for n, fruit in enumerate(fruits):
                if fruit == "banana":
                    print(f"Banana was very sweet!")
                    
        exit_button = input("You wanna exit?(yes/no)")
        if exit_button == "yes":
            break
        elif exit_button == "no":
            continue
        else:
            print("Invalid value")
            break
    except ValueError:
        print("Invalid value")
        continue
    #in_progress
