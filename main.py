# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.newui import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):

	def setup(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl &url)"), self.login)
	
	def login(self, url):
		print "print"

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