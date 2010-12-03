# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.newui import Ui_MainWindow
from string import find

class MainWindow(QtGui.QMainWindow):

	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl&)"), self.tryLogin)
	
	def tryLogin(self, url):
		urlstr = str(url.toString())
		print "Redirecting to %s" % urlstr
		
		if urlstr.startswith("http://www.facebook.com/connect/login_success.html#access_token="):
			startIndex = len("http://www.facebook.com/connect/login_success.html#access_token=")
			finishIndex = find(urlstr, "&")
			self.oauthToken = urlstr[startIndex:finishIndex]
			print self.oauthToken
		
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setup()

import sys

app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QWindowsVistaStyle())
#app.setStyle("windowsvista")
main = MainWindow()
main.show()
sys.exit(app.exec_())