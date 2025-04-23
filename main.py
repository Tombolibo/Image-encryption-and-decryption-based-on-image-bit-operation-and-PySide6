import sys

import cv2
import numpy as np
from PySide6 import QtWidgets, QtGui, QtCore

from mainWindow import Ui_MainWindow
from endecrypt import EnDecrypter


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._crypter = EnDecrypter()
        self._fileDialog = QtWidgets.QFileDialog()
        self._imgReaded = False
        self._imgKeySetted = False
        self._encrypted = False
        self._decrypted = True

        #信号槽绑定
        self.pushButtonChoseImg.clicked.connect(self.getImgPath)
        self.pushButtonChoseKey.clicked.connect(self.getImgKey)
        self.pushButtonRandomKey.clicked.connect(self.getRandomKey)
        self.pushButtonEncrypt.clicked.connect(self.encryptStart)
        self.pushButtonDecrypt.clicked.connect(self.decryptStart)
        self.pushButtonSave.clicked.connect(self.saveImg)
        self.pushButtonSaveKey.clicked.connect(self.saveKey)
        self.pushButtonDeleteImg.clicked.connect(self.deleteImg)
        self.pushButtonDeleteKey.clicked.connect(self.deleteKey)

        print('初始化完成')

    #选择图片
    def getImgPath(self):
        filename = self._fileDialog.getOpenFileName(self, "选择图片文件")
        self._crypter.readImgSrc(filename[0])
        #展示在label
        self.setLabelPixmap(self.labelChoseImg, self._crypter._imgSrcShow)
        self._imgReaded = True
        print('图片选择完成')

    #选择密钥
    def getImgKey(self):
        filename,_ = self._fileDialog.getOpenFileName(self, "选择文件")
        self._crypter.readImgKey(filename)
        self.setLabelPixmap(self.labelChoseKey, self._crypter._imgKeyShow)
        self._imgKeySetted = True
        print('密钥选择完成')
    #随机产生密钥
    def getRandomKey(self):
        self._crypter.randomKey()
        self.setLabelPixmap(self.labelChoseKey, self._crypter._imgKeyShow)
        self._imgKeySetted = True
    #开始加密
    def encryptStart(self):
        print('开始加密')
        if self._imgReaded and self._imgKeySetted:
            self._crypter.encrypt()
            self.setLabelPixmap(self.labelChoseImg, self._crypter._imgSrcShow)
            print('加密完成')
        else:
            print('不存在')
    #开始解密
    def decryptStart(self):
        print('开始解密')
        if self._imgKeySetted and self._imgReaded:
            self._crypter.decrypt()
            self.setLabelPixmap(self.labelChoseImg, self._crypter._imgSrcShow)
            print('解密完成')
        else:
            print('不存在')
    #保存
    def saveImg(self):
        if self._imgReaded:
            self._fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
            self._fileDialog.setDefaultSuffix('png')  #使用无损压缩，不能用jpg有损压缩，否则无法解密
            self._fileDialog.exec()
            path = self._fileDialog.selectedFiles()[0]
            imgSave = cv2.cvtColor(self._crypter._imgSrc, cv2.COLOR_RGB2BGR)
            imgSave = cv2.imencode('.png', imgSave)[1]
            imgSave.tofile(path)
            print('保存图片于：', path)
        else:
            print('无图片')

    #保存密钥
    def saveKey(self):
        if self._imgKeySetted:
            self._fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
            self._fileDialog.setDefaultSuffix('png')
            self._fileDialog.exec()
            path = self._fileDialog.selectedFiles()[0]
            imgSave = cv2.cvtColor(self._crypter._imgKey, cv2.COLOR_RGB2BGR)
            imgSave = cv2.imencode('.png', imgSave)[1]
            imgSave.tofile(path)


    #某个标签显示图像
    def setLabelPixmap(self, label, img):
        Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1]*img.shape[2], QtGui.QImage.Format.Format_RGB888)
        label.setPixmap(QtGui.QPixmap(Qimg))

    #删除某个标签图片
    def deleteImg(self):
        print('删除图片')
        if self._imgReaded:
            self.labelChoseImg.setText('请选择图片')
            self._crypter.deleteImg()
    def deleteKey(self):
        print('删除密钥')
        if self._imgKeySetted:
            self.labelChoseKey.setText('请选择密钥')
            self._crypter.deleteKey()

if __name__ == '__main__':
    mainApp = QtWidgets.QApplication(sys.argv)
    myApp =MyMainWindow()
    myApp.show()
    mainApp.exec()