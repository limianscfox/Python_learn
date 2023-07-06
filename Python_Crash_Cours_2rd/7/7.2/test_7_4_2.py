prompt = "\nPlease enter Pizzas's filling:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    ingredient = input(prompt).lower()
    if ingredient != 'quit':
        print(ingredient)
    else:
        break