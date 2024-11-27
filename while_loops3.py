name = input("Enter your name: ")
while True:
    count_1 = int(input("Enter first count: "))
    count_2 = int(input("Enter second count: "))
    
    if count_1 == count_2:
        print("First count equal second count " + name)
        continue
    elif count_1 > count_2:
        print("First count was bigger than second count " + name)
        continue
    elif count_1 < count_2 :
        print("Second count was bigger than first count " + name)
        continue
    else:
        print("Invalid value") #Invalid value doesn't show up
        break
