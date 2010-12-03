# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newui.ui'
#
# Created: Fri Dec 03 08:11:40 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 681, 511))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.webView = QtWebKit.QWebView(self.page)
        self.webView.setGeometry(QtCore.QRect(30, 40, 631, 301))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://graph.facebook.com/oauth/authorize?client_id=121815414497011&redirect_uri=http://www.facebook.com/connect/login_success.html&type=user_agent&scope=user_photos,friends_photos,publish_stream,user_status,friends_status&display=popup")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.txtInput = QtGui.QTextEdit(self.page_2)
        self.txtInput.setGeometry(QtCore.QRect(10, 20, 511, 41))
        self.txtInput.setObjectName(_fromUtf8("txtInput"))
        self.btnShare = QtGui.QPushButton(self.page_2)
        self.btnShare.setGeometry(QtCore.QRect(540, 20, 101, 41))
        self.btnShare.setObjectName(_fromUtf8("btnShare"))
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 301, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setIconSize(QtCore.QSize(50, 50))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidgetForInfo = QtGui.QListWidget(self.page_2)
        self.listWidgetForInfo.setGeometry(QtCore.QRect(360, 70, 281, 311))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidgetForInfo.setFont(font)
        self.listWidgetForInfo.setIconSize(QtCore.QSize(50, 50))
        self.listWidgetForInfo.setObjectName(_fromUtf8("listWidgetForInfo"))
        self.btnDisplayProfile = QtGui.QPushButton(self.page_2)
        self.btnDisplayProfile.setGeometry(QtCore.QRect(240, 450, 81, 21))
        self.btnDisplayProfile.setObjectName(_fromUtf8("btnDisplayProfile"))
        self.btnShowFriends = QtGui.QPushButton(self.page_2)
        self.btnShowFriends.setGeometry(QtCore.QRect(130, 450, 75, 23))
        self.btnShowFriends.setObjectName(_fromUtf8("btnShowFriends"))
        self.txtComment = QtGui.QTextEdit(self.page_2)
        self.txtComment.setGeometry(QtCore.QRect(360, 390, 281, 51))
        self.txtComment.setObjectName(_fromUtf8("txtComment"))
        self.btnComment = QtGui.QPushButton(self.page_2)
        self.btnComment.setGeometry(QtCore.QRect(460, 450, 101, 23))
        self.btnComment.setObjectName(_fromUtf8("btnComment"))
        self.btnNewsFeed = QtGui.QPushButton(self.page_2)
        self.btnNewsFeed.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.btnNewsFeed.setObjectName(_fromUtf8("btnNewsFeed"))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShare.setText(QtGui.QApplication.translate("MainWindow", "Share", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDisplayProfile.setText(QtGui.QApplication.translate("MainWindow", "Ver Perfil", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShowFriends.setText(QtGui.QApplication.translate("MainWindow", "Ver Amigos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnComment.setText(QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNewsFeed.setText(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
