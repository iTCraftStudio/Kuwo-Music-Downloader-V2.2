# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kuwo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_kuwo(object):
    def setupUi(self, kuwo):
        if not kuwo.objectName():
            kuwo.setObjectName(u"kuwo")
        kuwo.setEnabled(True)
        kuwo.resize(294, 141)
        self.actionAbout_Us = QAction(kuwo)
        self.actionAbout_Us.setObjectName(u"actionAbout_Us")
        self.actionAbout_Us.setCheckable(True)
        self.actionHome = QAction(kuwo)
        self.actionHome.setObjectName(u"actionHome")
        self.centralwidget = QWidget(kuwo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UrlEnit = QLineEdit(self.centralwidget)
        self.UrlEnit.setObjectName(u"UrlEnit")
        self.UrlEnit.setGeometry(QRect(10, 11, 191, 20))
        self.OkButton = QPushButton(self.centralwidget)
        self.OkButton.setObjectName(u"OkButton")
        self.OkButton.setGeometry(QRect(210, 10, 75, 23))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 271, 51))
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 20, 261, 23))
        self.progressBar.setCursor(QCursor(Qt.WaitCursor))
        self.progressBar.setValue(100)
        kuwo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(kuwo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 294, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        kuwo.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionAbout_Us)
        self.menu.addAction(self.actionHome)

        self.retranslateUi(kuwo)

        QMetaObject.connectSlotsByName(kuwo)
    # setupUi

    def retranslateUi(self, kuwo):
        kuwo.setWindowTitle(QCoreApplication.translate("kuwo", u"酷我音乐歌曲下载器", None))
        self.actionAbout_Us.setText(QCoreApplication.translate("kuwo", u"About Us", None))
        self.actionHome.setText(QCoreApplication.translate("kuwo", u"Home", None))
        self.UrlEnit.setText("")
        self.OkButton.setText(QCoreApplication.translate("kuwo", u"\u63d0\u4ea4\u97f3\u4e50URL", None))
        self.groupBox.setTitle(QCoreApplication.translate("kuwo", u"\u72b6\u6001", None))
        self.menu.setTitle(QCoreApplication.translate("kuwo", u"\u5173\u4e8e", None))
    # retranslateUi

