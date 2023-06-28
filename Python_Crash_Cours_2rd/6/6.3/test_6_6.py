favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', 
    }
survey = ['jen','edward','tom','ted']
for name in survey:
    if name in favorite_languages.keys():
        print (f"Thank you {name.title()}")
    else:
        print(f"Please {name.title()} complate the survey as quick")
    
