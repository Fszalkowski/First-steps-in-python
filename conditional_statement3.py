name = input("Hi, what's your name? ")
print("Hello "+ name)

question = input("You wanna equal your counts? ")
if question == 'Yes':
    print("Nice!")
else:
    print("Sad :(")
    
count = int(input("Enter first count: "))
count_2 = int(input("Enter second count: "))
if count == count_2:
    print("Your first count was equal second count")
elif count > count_2:
    print("Your first count was bigger than second count")
elif count < count_2:
    print("Your second count was bigger than first count")    
else:
    print("Invalid value")
