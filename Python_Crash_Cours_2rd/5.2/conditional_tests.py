test_1 = 'high'
test_2 = 'higH'

if test_1.lower() == test_2.lower() :
    print(f"{test_1} {test_2} is same !")
else:
    print(f"{test_1} {test_2} is diffrent !")
    
names = ['tom','tim','ted','bob','gray']
name = 'tom'
if name in names:
    print(f"{name.title()} in list !")
else:
    print(f"{name.title()} not in list !")