users_places = {}
poll_status = True

while poll_status:
    name = input("What's your name ?")
    place = input("If you could visit one place in the world, where would you go?")
    users_places[name] = place
    
    end_status = input("To continue or not, enter yes or no")
    if end_status.lower() == 'no':
        poll_status = False
    else:
        continue

for name_list,place_list in users_places.items():
    print(f"{name_list} went to visit {place_list}")

    