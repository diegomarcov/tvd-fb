# -*- coding: utf-8 -*-
from facebook import Facebook
import datetime
import simplejson as json
import codecs

class Facebook_Interface:
	def connect(self, api_key, secret_key):
		facebook = Facebook(api_key, secret_key)
		facebook.auth.createToken()
		facebook.login()
		print "After logging in, press enter..."
		raw_input()
		facebook.auth.getSession()
		
	def getUserName(self, userid):
		self.namequery = "SELECT name FROM user WHERE uid=%s" % userid
		try:
			self.name = facebook.fql.query(namequery)[0]
			return self.name
		catch:
			return ""
			
	def getNewsFeed(self, userid):
		self.query = "SELECT post_id, actor_id, message FROM stream WHERE filter_key in (SELECT filter_key FROM stream_filter WHERE uid=%s AND type='newsfeed') AND is_hidden = 0" % userid
		self.results = facebook.fql.query(query)
# Get api_key and secret_key from a file
api_key = "6698e61a09d52d0e98502fb0721672c5"
secret_key = "f2a50e87ab08eb4ea8a9c37428bb9926"
# fbs = open(FB_SETTINGS).readlines()

connect(api_key, secret_key)
# Show login window
# Login to the window, then press enter

#estas dos lineas son viejas, no tiene mas sentido usarlas... en su lugar, uso FQL
#userName = facebook.users.getInfo([facebook.uid], ["name"])[0]
#info = facebook.users.getInfo([facebook.uid], ["birthday", "affiliations", "sex"])[0]

#FQL

#query = "SELECT uid, first_name, last_name FROM user WHERE uid=%s" % facebook.uid
#results = facebook.fql.query(query)[0]
#userName = "%s %s" % (results[u'first_name'], results[u'last_name'])


query = "SELECT post_id, actor_id, message FROM stream WHERE filter_key in (SELECT filter_key FROM stream_filter WHERE uid=%s AND type='newsfeed') AND is_hidden = 0" % facebook.uid
#query = "SELECT first_name, last_name FROM user WHERE uid = 837208710"
print query
results = facebook.fql.query(query)

for p in results:
	try:
		#namequery = "SELECT first_name, middle_name, last_name FROM user WHERE uid=%s" % p[u'actor_id']
		namequery = "SELECT name FROM user WHERE uid=%s" % p[u'actor_id']
		print namequery
		#firstName = ""
		#middleName = ""
		#lastName = " "
		name = facebook.fql.query(namequery)[0]
		'''
		if 'first_name' in name and name[u'first_name']:
			firstName = name[u'first_name']
		if 'middle_name' in name and name[u'middle_name']:
			middleName = name[u'middle_name']
		if 'last_name' in name and name[u'last_name']:
			lastName+=name[u'last_name']
		'''
		print "%s\n%s\n\n" % (name[u'name'], p[u'message'])
		#print "%s%s%s\n%s\n\n" % (firstName, middleName, lastName, p[u'message'])
	except:
		pass

#print "El nombre del usuario es: %s. Su perfil indica:" % (userName)
#for attr in info:
 #   print "%s: %s" % (attr, info[attr])


#require_permissions("status_update")

#facebook.request_extended_permission("status_update")
#facebook.request_extended_permission("read_stream")
#facebook.request_extended_permission("publish_stream")

#print("Once you got it, press enter...")

#raw_input()

#att =  {'name': u"Juan Domingo Peron\n", 'href': 'http://es.wikipedia.org/wiki/Juan_Domingo_Per%C3%B3n', 'description': 'PERON PERON QUE GRANDE SOS, MI GENERAL CUANTO VALES!', 'media': [{'type': 'image', 'src': 'http://www.lagazeta.com.ar/peron1.jpg', 'href': 'http://www.lagazeta.com.ar/peron1.jpg'}] }
#action_link = [{'text':'Ir a la pagina oficial del General', 'href':'http://es.wikipedia.org/wiki/Juan_Domingo_Per%C3%B3n'}]
#facebook.stream.publish(message='Probando mensajes con media attachments.', attachment=att, action_links=action_link, target_id='1113442416')

#facebook.users.setStatus(status="Actualizando el status desde un plasma 42 mientras veo la NBA",clear=False, status_includes_verb=True)

#streams = facebook.stream.get()

#print "These are da streams, dawg"
#print streams

#get devuelve el arreglo de user id"s
#friends = facebook.friends.get()
'''
data = facebook.stream.get(facebook.uid)
profiles = dict((p["id"], p) for p in data["profiles"])

for post in data["posts"]:
	print "Hello\n"
	if "message" in post and post["message"]:
		sender_name = (profiles[post["actor_id"]]["name"]).encode("utf-8")
		text = (post["message"]).encode("utf-8")
		time = datetime.datetime.fromtimestamp(post["created_time"])
		comments = post["comments"]["count"]

		print "(%s) %s: %s (%s comments)" % (time, sender_name, text, comments)

for f in friends:
	friendName = facebook.users.getInfo(f, ["name"])
	if cmp(friendName, "Jorge Marcovecchio")==0:
		friendData = facebook.users.getInfo(f, ["birthday", "relationship_status"])
		print "%s cumple el %s y esta %s" % (friendName, friendData["birthday"], friendData["relationship_status"])


friends = facebook.users.getInfo(friends[7], ["name", "birthday", "relationship_status"])

for friend in friends:
	if cmp(friend["name"],"Robert Battle") == 0:
		print "Come on dawg, come play for peniarol!"
		print "Fecha de nacimiento: %s" % (friend["birthday"])
    
	if "birthday" in friend:
		print friend["name"], "has a birthday on", friend["birthday"], "and is", friend["relationship_status"]
	else:
		print friend["name"], "has no birthday and is", friend["relationship_status"]

#arefriends = facebook.friends.areFriends([friends[0]["uid"]], [friends[1]["uid"]])

#photos = facebook.photos.getAlbums(friends[1]["uid"])
#print photos
'''
