def greet_users(names):
    """遍历列表中元素，并按指定格式输出"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'try', 'margot']
greet_users(usernames)