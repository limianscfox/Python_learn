def make_sandwich(*toppings):
    print(f"\nThe sandwich including ")
    for topping in toppings:
        print(f"- {topping}")
        
make_sandwich('slan')
make_sandwich('lts', 'temp', 'qq')
make_sandwich('lts')