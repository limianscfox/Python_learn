def show_messages(msg_list):
    """print list element"""
    for msg in msg_list:
        print(msg)


def send_messages(msg_list):
    """print & move list element"""
    sended_msg = []
    while msg_list:
        current_msg = msg_list.pop()
        print(current_msg)
        sended_msg.append(current_msg)
    print(f"need to send msg list:{msg_list}")
    print(f"complete send msg list:{sended_msg}")
    


msg_lists = ['mail','slienge','zhengse']
send_messages(msg_lists)