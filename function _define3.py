while True:
    try:
        count_1=int(input("Enter first count: "))
        count_2=int(input("Enter second count: "))
        count_3=int(input("Enter third count: "))
    except ValueError:
        print("Invalid value")
        continue
    def multiply(*numbers):
        total = 1
        for number in numbers:
            total = total * number
        return total
    break
print(multiply(count_1,count_2,count_3))
