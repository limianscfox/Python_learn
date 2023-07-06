prompt = "\nPlease enter Pizzas's filling:"
prompt += "\n(Enter 'quit' when you are finished.)"
acitve = True
while acitve:
    ingredient = input(prompt).lower()
    if ingredient != 'quit':
        print(ingredient)
    else:
        acitve = False