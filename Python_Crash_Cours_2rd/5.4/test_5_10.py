current_users = ['tom','tim','ted','brian','carl']
new_users = ['bob','lee','jack','Carl','Tom']
for new_user in new_users :
    if new_user.lower() in current_users :
        print(f"{new_user} is current user, please uses anthor one.")
    else :
        print(f"{new_user} ia avaible.")
