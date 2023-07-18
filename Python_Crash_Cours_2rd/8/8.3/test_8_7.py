def make_album(artist_name,album_name,album_num=None):
    '''make album'''
    if album_num == None:
        return {'a_title':album_name, 'artists':artist_name}
    else:
        return {'a_title':album_name, 'artists':artist_name,'num':album_num}

a_album = make_album('lee','test',12)
b_album = make_album('ll','tx')
c_album = make_album('ted','pp')

print(f"{a_album}\n{b_album}\n{c_album}")