def get_formatted_name(first_name, last_name):
    """返回整洁名字"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is a loop

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name.lower() == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name.lower() == 'q':
        break
    
    formatted_name = get_formatted_name(f_name.lower(), l_name.lower())
    print (f"\nHello, {formatted_name}")