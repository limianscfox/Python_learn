def show_messages(msg_list):
    """print list element"""
    print("Showing all messages")
    for msg in msg_list:
        print(msg)


def send_messages(msg_list,sent_list):
    """print & move list element"""
    print("\nSending all messages:")
    while msg_list:
        current_msg = msg_list.pop()
        print(current_msg)
        sent_list.append(current_msg)
    


msg_lists = ['mail','slienge','zhengse']
show_messages(msg_lists)

sent_list = []
send_messages(msg_lists[:],sent_list)

print("\nFinal list")
print(msg_lists)
print(sent_list)

