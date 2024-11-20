while True:
    try:
        count_1 = int(input("Enter first count: "))
        count_2 = int(input("Enter second count: "))

        def adding(first_count, second_count):
            return first_count + second_count
    except ValueError:
        print("Invalid value")
        continue

    result = adding(count_1, count_2)

    print("Your result: ", result)
    if result > 10:
        print("Your result was bigger than 10")
    elif result < 10:
        print("Your result was smaller than 10")
    elif result == 10:
        print("Your result was equal to 10")
    else:
        print("Something was wrong")     
    break
