def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello,{username.title()}!")

user = input("Please input you name:")
greet_user(user)