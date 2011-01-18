# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.newui import Ui_MainWindow
from string import find
from facebook_interface import Facebook_Interface

HOME = "home"
VISITING_PROFILE = "profile"

class MainWindow(QtGui.QMainWindow):

	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		# self.mode indica en qué modo de exploración está el usuario: si en la página principal, o visitando perfiles
		self.mode = HOME
		
		# este atributo guarda el profile ID que se está visitando en este momento; si el usuario está en modo HOME,
		# entonces es None
		self.currentDisplayedProfile = None
		
		# estas dos listas contienen los post ID y profile ID del listWidget que muestra los posts, respectivamente
		self.postIDList = []
		self.profileIDList = []
		
		
		# SIGNALS ################################################
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl&)"), self.tryLogin)
		QtCore.QObject.connect(self.ui.btnShare, QtCore.SIGNAL("clicked()"), self.post)
		QtCore.QObject.connect(self.ui.btnNewsFeed, QtCore.SIGNAL("clicked()"), self.displayNewsFeed)
		QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.displayComments)
		QtCore.QObject.connect(self.ui.btnDisplayProfile, QtCore.SIGNAL("clicked()"), self.displaySelectedProfile)
		QtCore.QObject.connect(self.ui.btnShowFriends, QtCore.SIGNAL("clicked()"), self.displayFriends)
		QtCore.QObject.connect(self.ui.btnComment, QtCore.SIGNAL("clicked()"), self.displayFriends)
		# @TODO: agregar un comentario a un post
	
	def getSelectedProfileID(self):
		return self.profileIDList[self.ui.listWidget.currentRow()]
	
	def getSelectedPostID(self):
		return self.postIDList[self.ui.listWidget.currentRow()]	
	
	def tryLogin(self, url):
		urlstr = str(url.toString())
		print "Redirecting to %s" % urlstr
		
		# @TODO: probar casos de error
		if urlstr.startswith("http://www.facebook.com/connect/login_success.html#access_token="):
			startIndex = len("http://www.facebook.com/connect/login_success.html#access_token=")
			finishIndex = find(urlstr, "&")
			oauthToken = urlstr[startIndex:finishIndex]
			self.facebook = Facebook_Interface(oauthToken)
			self.ui.stackedWidget.setCurrentIndex(1)
	
	def displayFriends(self):
		profileID = self.getSelectedProfileID()
		friends = self.facebook.getFriends(profileID)
		self.ui.listWidget.clear()
		self.profileIDList = []
		self.postIDList = []
		i = 0
		# @TODO: no se pueden pedir los amigos de cualquier ID.... fixear eso, O unicamente permitir para el usuario
		for friend in friends['data']:
			if i<35:
				self.profileIDList.append(friend['id'])
				pic = self.facebook.getProfilePicture(friend['id'])
				QtGui.QListWidgetItem(QtGui.QIcon(pic), friend['name'], self.ui.listWidget)
			else:
				print "Friend limit reached!"
				break
				
	def displayComments(self):
		postid = self.getSelectedPostID()
		comments = self.facebook.getComments(postid)
		self.ui.listWidgetForInfo.clear()
		if 'data' in comments:
			for comment in comments['data']:
				pic = self.facebook.getProfilePicture(comment['from']['id'])
				username = comment['from']['name']
				message = comment['message']
				QtGui.QListWidgetItem(QtGui.QIcon(pic), "%s\n%s" % (username,message), self.ui.listWidgetForInfo)
	
	def displaySelectedProfile(self):
		self.mode = VISITING_PROFILE
		self.currentDisplayedProfile = self.getSelectedProfileID()
		print "Showing %s profile" % self.currentDisplayedProfile
		self.profileIDList = []
		self.postIDList = []
		self.ui.listWidget.clear()
		wallPosts = self.facebook.getWallPosts(self.currentDisplayedProfile)
		self.displayPosts(wallPosts)
	
	def post(self):
		text = self.ui.txtInput.toPlainText()
		if text:
			if self.mode == HOME:
				self.facebook.updateStatus(text)
				self.ui.txtInput.setText("")
			elif self.mode == VISITING_PROFILE:
				self.facebook.postToWall(self.currentDisplayedProfile, text)
			else:
				raise "This shouldn't happen!"
	
	def displayPosts(self, posts):
		for post in posts['data']:
			if "type" in post:
				# nombre de usuario
				self.profileIDList.append(post['from']['id'])
				self.postIDList.append(post['id'])
				userName = post['from']['name']
				
				userImage = self.facebook.getProfilePicture(post['from']['id'])
				
				# LIKES que tiene el post
				if "likes" in post:
					if post['likes'] == 1:
						likesText = "\n(A 1 persona le gusta esto.)"
					else:
						likesText = "\n(A %s personas les gusta esto.)" % post['likes']
				else:
					likesText = ""
				
				# comentarios del post
				if "comments" in post:
					if post['comments']['count'] == 1:
						commentsText = "\n(1 comentario.)"
					else:
						commentsText = "\n(%s comentarios.)" % post['comments']['count']
				else:
					commentsText = ""
				
				#si el mensaje tiene cuerpo, lo muestro
				if "message" in post:
					message = "\n%s" % post['message']
				else:
					message = ""
				
				# si el mensaje tiene target, lo muestro
				if "to" in post:
					userName += " >> %s" % post['to']['data'][0]['name']
					
				# formateo según el tipo de mensaje ###############################
				
				# si es una actualización de estado, lo muestro directamente
				if post['type'] == "status":
					outputString = '%s\n%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText)
				# si es un link... por ahora obtengo el link y nada más @TODO
				elif post['type'] == "link":
					if "link" in post:
						link = "\nLink: %s" % post['link']
					else:
						raise "This shouldn't happen!"
					outputString = '%s\n%s\n%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText, link)
				# si es un video... por ahora obtengo el source y nada más @TODO ver si los links son sólo de YouTube o también de facebook; ver de asociar con el widget de Juan
				elif post['type'] == "video":
					if "source" in post:
						source = "\nVideo: %s" % post['source']
					else:
						raise "This shouldn't happen!"
					outputString = '%s\n%s%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText, source)
				# si es una imagen, por ahora pongo el source y nada más
				elif post['type'] == "picture":
					if "picture" in post:
						source = "\nPicture: %s" % post['picture']
					else:
						raise "This souldn't happen!"
					outputString = '%s\n%s%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText, source)
				
				# print "########## NEW POST ###############"
				# print outputString
				QtGui.QListWidgetItem(QtGui.QIcon(userImage), unicode(outputString), self.ui.listWidget)
			else: # este caso es OTRO fail de la api de facebook... vienen posts sin TYPE... IMPRESENTABLE
				pass

	def displayNewsFeed(self):
		newsFeed = self.facebook.getNewsFeed()
		self.ui.listWidget.clear()
		self.mode = HOME
		self.profileIDList = []
		self.postIDList = []
		self.ui.listWidgetForInfo.clear()
		self.currentDisplayedProfile = None
		self.displayPosts(newsFeed)
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setup()

import sys

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())