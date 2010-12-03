# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.newui import Ui_MainWindow
from string import find
from facebook_interface import Facebook_Interface

class MainWindow(QtGui.QMainWindow):

	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		# SIGNALS ################################################
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl&)"), self.tryLogin)
		QtCore.QObject.connect(self.ui.btnShare, QtCore.SIGNAL("clicked()"), self.post)
		QtCore.QObject.connect(self.ui.btnNewsFeed, QtCore.SIGNAL("clicked()"), self.displayNewsFeed)
	
	def tryLogin(self, url):
		urlstr = str(url.toString())
		print "Redirecting to %s" % urlstr
		
		if urlstr.startswith("http://www.facebook.com/connect/login_success.html#access_token="):
			startIndex = len("http://www.facebook.com/connect/login_success.html#access_token=")
			finishIndex = find(urlstr, "&")
			oauthToken = urlstr[startIndex:finishIndex]
			self.facebook = Facebook_Interface(oauthToken)
			self.ui.stackedWidget.setCurrentIndex(1)
	
	def post(self):
		text = self.ui.txtInput.toPlainText()
		if text:
			self.facebook.updateStatus(text)
			self.ui.txtInput.setText("")
			
	def displayNewsFeed(self):
		newsFeed = self.facebook.getNewsFeed()
		self.ui.listWidget.clear()
		for post in newsFeed['data']:
			# nombre de usuario
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
			
			if post['type'] == "status":
				outputString = '%s\n%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText)
			elif post['type'] == "link":
				if "link" in post:
					link = "\nLink: %s" % post['link']
				else:
					raise "This shouldn't happen!"
				outputString = '%s\n%s%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText, link)
			elif post['type'] == "video":
				if "source" in post:
					source = "\nVideo: %s" % post['source']
				else:
					raise "This shouldn't happen!"
				outputString = '%s\n%s%s%s%s' % (unicode(userName), unicode(message), likesText, commentsText, source)
			# si el mensaje tiene target, lo muestro
			# if "to" in post:
				# userName += " >> %s" % post['to']['data'][0]['name']
			
			QtGui.QListWidgetItem(QtGui.QIcon(userImage), outputString, self.ui.listWidget)
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setup()

import sys

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())