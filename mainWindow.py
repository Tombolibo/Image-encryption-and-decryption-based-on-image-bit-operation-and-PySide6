# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayoutTop = QHBoxLayout()
        self.horizontalLayoutTop.setObjectName(u"horizontalLayoutTop")
        self.verticalLayoutTopLeft = QVBoxLayout()
        self.verticalLayoutTopLeft.setObjectName(u"verticalLayoutTopLeft")
        self.pushButtonChoseImg = QPushButton(self.centralwidget)
        self.pushButtonChoseImg.setObjectName(u"pushButtonChoseImg")

        self.verticalLayoutTopLeft.addWidget(self.pushButtonChoseImg)

        self.labelChoseImg = QLabel(self.centralwidget)
        self.labelChoseImg.setObjectName(u"labelChoseImg")
        self.labelChoseImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutTopLeft.addWidget(self.labelChoseImg)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutTopLeft.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonDeleteImg = QPushButton(self.centralwidget)
        self.pushButtonDeleteImg.setObjectName(u"pushButtonDeleteImg")

        self.horizontalLayout.addWidget(self.pushButtonDeleteImg)

        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout.addWidget(self.pushButtonSave)


        self.verticalLayoutTopLeft.addLayout(self.horizontalLayout)


        self.horizontalLayoutTop.addLayout(self.verticalLayoutTopLeft)

        self.verticalLayoutTopRight = QVBoxLayout()
        self.verticalLayoutTopRight.setObjectName(u"verticalLayoutTopRight")
        self.horizontalLayoutTopRight = QHBoxLayout()
        self.horizontalLayoutTopRight.setObjectName(u"horizontalLayoutTopRight")
        self.pushButtonChoseKey = QPushButton(self.centralwidget)
        self.pushButtonChoseKey.setObjectName(u"pushButtonChoseKey")

        self.horizontalLayoutTopRight.addWidget(self.pushButtonChoseKey)

        self.pushButtonRandomKey = QPushButton(self.centralwidget)
        self.pushButtonRandomKey.setObjectName(u"pushButtonRandomKey")

        self.horizontalLayoutTopRight.addWidget(self.pushButtonRandomKey)


        self.verticalLayoutTopRight.addLayout(self.horizontalLayoutTopRight)

        self.labelChoseKey = QLabel(self.centralwidget)
        self.labelChoseKey.setObjectName(u"labelChoseKey")
        self.labelChoseKey.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutTopRight.addWidget(self.labelChoseKey)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutTopRight.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonDeleteKey = QPushButton(self.centralwidget)
        self.pushButtonDeleteKey.setObjectName(u"pushButtonDeleteKey")

        self.horizontalLayout_2.addWidget(self.pushButtonDeleteKey)

        self.pushButtonSaveKey = QPushButton(self.centralwidget)
        self.pushButtonSaveKey.setObjectName(u"pushButtonSaveKey")

        self.horizontalLayout_2.addWidget(self.pushButtonSaveKey)


        self.verticalLayoutTopRight.addLayout(self.horizontalLayout_2)


        self.horizontalLayoutTop.addLayout(self.verticalLayoutTopRight)


        self.verticalLayout_3.addLayout(self.horizontalLayoutTop)

        self.horizontalLayoutBelow = QHBoxLayout()
        self.horizontalLayoutBelow.setObjectName(u"horizontalLayoutBelow")
        self.pushButtonEncrypt = QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setObjectName(u"pushButtonEncrypt")

        self.horizontalLayoutBelow.addWidget(self.pushButtonEncrypt)

        self.pushButtonDecrypt = QPushButton(self.centralwidget)
        self.pushButtonDecrypt.setObjectName(u"pushButtonDecrypt")

        self.horizontalLayoutBelow.addWidget(self.pushButtonDecrypt)

        self.pushButtonROI = QPushButton(self.centralwidget)
        self.pushButtonROI.setObjectName(u"pushButtonROI")

        self.horizontalLayoutBelow.addWidget(self.pushButtonROI)


        self.verticalLayout_3.addLayout(self.horizontalLayoutBelow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonChoseImg.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247...", None))
        self.labelChoseImg.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.pushButtonDeleteImg.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u56fe\u7247", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.pushButtonChoseKey.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5bc6\u94a5...", None))
        self.pushButtonRandomKey.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a\u751f\u6210\u5bc6\u94a5", None))
        self.labelChoseKey.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5bc6\u94a5", None))
        self.pushButtonDeleteKey.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5bc6\u94a5", None))
        self.pushButtonSaveKey.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5bc6\u94a5", None))
        self.pushButtonEncrypt.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u52a0\u5bc6", None))
        self.pushButtonDecrypt.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u89e3\u5bc6", None))
        self.pushButtonROI.setText(QCoreApplication.translate("MainWindow", u"\u6846\u9009\u533a\u57df", None))
    # retranslateUi

