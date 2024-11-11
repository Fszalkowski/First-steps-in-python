count = 0

while count <= 5:
    count = count + 1
    if count % 2 == 1:
        continue
    print(count)
    if count > 5:
        break
