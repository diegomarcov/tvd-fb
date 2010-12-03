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
		# for post in newsFeed['data']:
		print newsFeed
		
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setup()

import sys

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())