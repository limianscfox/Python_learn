favorite_places = {
    'tom':['beijing'],
    'bob':['shanghai','sichuan'],
    'ted':['china','us','japan']
    }
for name,places in favorite_places.items():
    print(f"{name.title()} love ",end='')
    for place in places:
        print(f" {place.title()}",end='')
    print(f"!\n")
    
            
           