sandwich_orders = ['ll','ls','lk']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print(f"all sandwich {finished_sandwiches}")    
