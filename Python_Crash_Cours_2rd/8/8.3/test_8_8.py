def make_album(artist_name,album_name,album_num=None):
    '''make album'''
    if album_num == None:
        return {'a_title':album_name, 'artists':artist_name}
    else:
        return {'a_title':album_name, 'artists':artist_name,'num':album_num}
    
list_album = []
while True:
    print("\nPlease enter the album information")
    print("(enter 'q' at any time to quit)")

    a_name = input("Please enter album name:")
    if a_name.lower() == 'q':
        break
    
    p_name = input("Please enter artist:")
    if p_name.lower() == 'q':
        break
    
    a_num = input("Please enter songs num:")
    if a_num.lower() == 'q':
        break
    
    #引用函数返回字典值赋
    m_album = make_album(p_name.title(), a_name.title(), a_num.title())
    
    #动态用"a_name_album"格式命名变量，并将新生成的字典给其赋值
    exec('{}_album = {}'.format(a_name,m_album))
    #打印动态命名的变量，确认输入字典内容
    exec('print({}_album)'.format(a_name))
    #将输入生成的字典追加到列表中
    exec('list_album.append({}_album)'.format(a_name))

for lists in list_album:
    print(lists)










