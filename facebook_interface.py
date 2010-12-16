import facebook
import urllib2
from PyQt4 import QtGui

class Facebook_Interface():
	def __init__(self, authToken):
		self.graph = facebook.GraphAPI(authToken)
		self.profilePictures = {}
	
	def updateStatus(self, message):
		self.graph.put_object("me", "feed", message=message)
	
	def getNewsFeed(self):
		return self.graph.get_connections("me", "home")
		
	def getProfilePicture(self, user):
		if user in self.profilePictures:
			return self.profilePictures[user]
			print "Cached picture: %s" % self.profilePictures[user]
		else:
			print "Requesting pic from user %s" % user
			# self.profilePictures[user] = self.graph.get_connections(user, "picture")
			photo = "http://graph.facebook.com/%s/picture?type=square" % user
			imageurl = urllib2.urlopen(photo)
			self.imagedata = imageurl.read()
			imageurl.close()
			self.image = QtGui.QPixmap()
			self.image.loadFromData(self.imagedata)
			self.profilePictures[user] = self.image
			return self.image
			
	def getWallPosts(self, target):
		return self.graph.get_connections(target, "feed")
	
	def postToWall(self, target, message):
		self.graph.put_wall_post(message=message, attachment={}, profile_id=target)
		
	def getComments(self, postID):
		return self.graph.get_connections(postID, "comments")