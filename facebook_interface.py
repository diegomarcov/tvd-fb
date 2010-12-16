import facebook
import urllib2
from PyQt4 import QtGui
from threading import Thread, Lock
from time import sleep
import thread

profilePictures = {}
threadLock = Lock()

class Facebook_Interface():
	def __init__(self, authToken):
		self.graph = facebook.GraphAPI(authToken)
		self.prefetch = PrefetcherThread(self.graph)
		self.prefetch.start()
	
	def updateStatus(self, message):
		self.graph.put_object("me", "feed", message=message)
	
	def getNewsFeed(self):
		return self.graph.get_connections("me", "home")
		
	def getProfilePicture(self, user):
		threadLock.acquire()
		if user in profilePictures:
			print "Cached picture @ main thread for user %s" % user
			threadLock.release()
			return profilePictures[user]
		else:
			print "Requesting pic @ main thread from user %s" % user
			# self.profilePictures[user] = self.graph.get_connections(user, "picture")
			photo = "http://graph.facebook.com/%s/picture?type=square" % user
			imageurl = urllib2.urlopen(photo)
			self.imagedata = imageurl.read()
			imageurl.close()
			self.image = QtGui.QPixmap()
			self.image.loadFromData(self.imagedata)
			profilePictures[user] = self.image
			threadLock.release()
			return self.image
		
	def getWallPosts(self, target):
		return self.graph.get_connections(target, "feed")
	
	def postToWall(self, target, message):
		self.graph.put_wall_post(message=message, attachment={}, profile_id=target)
		
	def getComments(self, postID):
		return self.graph.get_connections(postID, "comments")
		
	def getFriends(self, target):
		return self.graph.get_connections(target, "friends")
		

		
		
		
		
		
		
# esta es la clase de prefetching de profile pictures! ########################################
		
class PrefetcherThread(Thread):
	
	def __init__ (self, facebookConnection):
		Thread.__init__ (self)
		self.facebook = facebookConnection
		
	def run (self):
		profilePictures
		self.results = self.facebook.get_connections("me", "home")
		# primero cacheamos todas las profile picture que aparecen en el NewsFeed; esto es para
		# ahorrar tiempo, y que no se espere a cargar todo cuando el usuario hace click
		for post in self.results['data']:
			userid = post['from']['id']
			threadLock.acquire()
			try:
				if userid in profilePictures:
					print "Cached profile pic from newsfeed @ prefetching thread"
				else:
					print "Acquiring profile pic from newsfeed @ prefetching thread"
					#como la api de facebook es una mierda, accedo directamente por la url a la profile picture
					photo = "http://graph.facebook.com/%s/picture?type=square" % userid
					imageurl = urllib2.urlopen(photo)
					self.imagedata = imageurl.read()
					imageurl.close()
					self.image = QtGui.QPixmap()
					self.image.loadFromData(self.imagedata)
					profilePictures[userid] = self.image
			finally:
				threadLock.release()
			sleep(0.01)
			
		# despues cargamos TODAS Y CADA UNA de las profile picture de nuestros amigos;
		# lo lamento, Facebook; no seria necesario robarte tanto ancho de banda si
		# tuvieras una api como la gente
		self.friendList = self.facebook.get_connections("me","friends")
		for friend in self.friendList['data']:
			userid = friend['id']
			threadLock.acquire()
			try:
				if userid in profilePictures:
					print "Cached profile pic from friends @ prefetching thread"
				else:
					print "Acquiring profile pic from friends @ prefetching thread"
					#como la api de facebook es una mierda, accedo directamente por la url a la profile picture
					photo = "http://graph.facebook.com/%s/picture?type=square" % userid
					imageurl = urllib2.urlopen(photo)
					self.imagedata = imageurl.read()
					imageurl.close()
					self.image = QtGui.QPixmap()
					self.image.loadFromData(self.imagedata)
					profilePictures[userid] = self.image
			finally:
				threadLock.release()
			sleep(0.01)