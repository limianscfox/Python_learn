# 创建一个用于存储外星人的空列表。 
aliens = []
# 创建30个绿色的外星人。
# 每个外星人独立字典，方便单独修改和引用。创建列表后修改字典，并不影响列表内容，所以以下内容代码没有意思，修改列表中指定字典，可以通过列表索引操作。
'''
for alien_number in range(30):
    locals()[f'alien_{alien_number}']= {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(locals()[f'alien_{alien_number}'])
'''
for alien_number in range(30):
    new_alien= {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# 显示穿件的30个外星人的
#for alien_number in range(30):
#    print(locals()[f'alien_{alien_number}'])
#修改第二个外星人颜色为红色，速度为高，分数为20
aliens[1] = {'color': 'red', 'points': 20, 'speed': 'high'}
# 如果前4个外星人的颜色是绿色，则改完黄色,速度中，分值10
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

# 显示前5个外星人。
for alien in aliens[:5]: 
    print(alien)
print("...")

# 显示创建了多少个外星人。
print(f"Total number of aliens: {len(aliens)}")