import facebook

class Facebook_Interface():
	def __init__(self, authToken):
		self.graph = facebook.GraphAPI(authToken)
	
	def updateStatus(self, message):
		self.graph.put_object("me", "feed", message=message)
	
	def getNewsFeed(self):
		return self.graph.get_connections("me", "home")