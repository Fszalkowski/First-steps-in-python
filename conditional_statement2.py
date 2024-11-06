price = int(input("What's your price? ")) 
value = input("The price you provided was in EUR or PLN?")

if value == "EUR":
    converted = price * 4,35
    print("Price in PLN: " + str(converted))
if value == "PLN":
    converted = price // 4,35
    print("Price in EUR: " + str(converted))

elif value != "EUR" and  value != "PLN":
    print("Invalid value")
