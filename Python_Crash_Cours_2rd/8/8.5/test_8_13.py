def build_profile(first_name,last_name,**user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

my_user_profile = build_profile('mian', 'li', age=18, hobbies='eat', gender_based='man')
print(my_user_profile)