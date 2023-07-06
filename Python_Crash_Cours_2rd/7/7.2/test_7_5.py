prompt = "\nPlease enter age:"
prompt += "\n(Enter 'quit' when you are finished.)"
age = ''
while age != 'quit':
    age = input(prompt).lower()
    if age != 'quit':
        if int(age) < 3:
            print(f"age:{age} is free")
        elif int(age) > 3 and int(age) <=12:
            print(f"age:{age} is 10$")
        else:
            print(f"age:{age} is 15$")
        
    

