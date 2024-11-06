print('Welecome in grade checker!')

math_grade = input('Enter your math grade: ') #entering_grade
if int(math_grade) > 3: 
    print("Are you genius?")
elif int(math_grade) == 3:
    print("Nice!")
elif int(math_grade) < 3:
    print("Let's correct it!") #conparison
    
pe_grade = input('Enter your pe grade: ') #entering_grade
if int(pe_grade) > 4:
    print("Nice!")
elif int(pe_grade) ==4: #conparison
    print("Not bad :/")
elif int(pe_grade) < 4:
    print("You are looser?")
    
