print(f"The pastrami is sold out")

sandwich_orders = ['ll','ls','lk','lt','pastrami','pastrami','pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        finished_sandwiches.append(sandwich)
    else:
        print(f"The pastrami is sold out")
    

print(f"all sandwich {finished_sandwiches}")  