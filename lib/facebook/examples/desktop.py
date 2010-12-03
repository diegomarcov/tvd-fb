# -*- coding: utf-8 -*-
from facebook import Facebook

# Get api_key and secret_key from a file
api_key = '6698e61a09d52d0e98502fb0721672c5'
secret_key = 'f2a50e87ab08eb4ea8a9c37428bb9926'
# fbs = open(FB_SETTINGS).readlines()
facebook = Facebook(api_key, secret_key)
print 'creacion re ok'
facebook.auth.createToken()
# Show login window
print 'auth re ok'
facebook.login()
print 'login re ok'
# Login to the window, then press enter
print 'After logging in, press enter...'
raw_input()

facebook.auth.getSession()
info = facebook.users.getInfo([facebook.uid], ['name', 'birthday', 'affiliations', 'sex'])[0]

for attr in info:
    print '%s: %s' % (attr, info[attr])

friends = facebook.friends.get()
friends = facebook.users.getInfo(friends[0:5], ['name', 'birthday', 'relationship_status'])

for friend in friends:
    if 'birthday' in friend:
	print friend['name'], 'has a birthday on', friend['birthday'], 'and is', friend['relationship_status']
    else:
	print friend['name'], 'has no birthday and is', friend['relationship_status']

arefriends = facebook.friends.areFriends([friends[0]['uid']], [friends[1]['uid']])

photos = facebook.photos.getAlbums(friends[1]['uid'])
print photos