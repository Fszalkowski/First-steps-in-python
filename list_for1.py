while True:
    try:
        fruit_1 = input("Enter first fruit: ")
        fruit_2 = input("Enter second fruit: ")
        fruit_3 = input("Enter third fruit: ")
    except ValueError:
        print("Invalid value")
        continue
    fruits = [fruit_1, fruit_2, fruit_3]
    for fruit in fruits:
        print(fruit)
    break
    #in_progress
