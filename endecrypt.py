import cv2
import numpy as np

class EnDecrypter(object):
    def __init__(self):
        self._imgSrcPath = None  #原始图片路径
        self._imgKeyPath = None  #密钥图片路径
        self._savePath = None  #图片保存路径
        self._imgSrc = None  #原始图片
        self._imgSrcShow = None  #展示的原始图片
        self._imgKey = None  #密钥图片（读取或随机值）
        self._imgKeyShow = None  #展示的密钥
        self._expand = 400  #从1：x的比例扩展系数（长：宽，width：height）
        self._ROI = None  #框选区域
        self._imgSrcExisted = False  #原始图片是否存在
        self._imgKeyExisted = False  #密钥是否存在
        self._ROIExisted = False  #框选区域是否存在
        self._encrypted = False  #是否已经加密

    #读取原始图片
    def readImgSrc(self, imgPath):
        if imgPath is not None:
            try:
                self._imgSrcPath = imgPath
                self._imgSrc = cv2.imdecode(np.fromfile(self._imgSrcPath, dtype = np.uint8), -1)  #读入进来是BGR
            except:
                print('读取失败')
            else:
                self._imgSrcExisted = True
                self._imgSrc = cv2.cvtColor(self._imgSrc, cv2.COLOR_BGR2RGB)
                self._imgSrcShow = self.scaleImg(self._imgSrc)
                if self._imgKeyExisted:
                    self.scaleKey()
                print('原始图片读取完成')
    #密钥对齐
    def scaleKey(self):
        if self._imgSrcExisted and self._imgKeyExisted:
            self._imgKey = cv2.resize(self._imgKey, (self._imgSrc.shape[1], self._imgSrc.shape[0])) #resize不需要通道
            self._imgKeyShow = self.scaleImg(self._imgKey)
            print('密钥已对齐')
        else:
            print('图片不完整，无法对齐密钥')
    #读取密钥图片
    def readImgKey(self,imgPath):
        if imgPath is not None:
            try:
                self._imgKeyPath = imgPath
                self._imgKey = cv2.imdecode(np.fromfile(self._imgKeyPath, dtype = np.uint8), -1)  #中文路径
            except:
                print('密钥图片读取失败')
            else:
                self._imgKeyExisted = True
                self._imgKey = cv2.cvtColor(self._imgKey, cv2.COLOR_BGR2RGB)
                self.scaleKey()
                self._imgKeyShow = self.scaleImg(self._imgKey)
                print('密钥读取完成')
    #随机生成密钥
    def randomKey(self):
        if self._imgSrcExisted:
            self._imgKey = np.random.randint(0,255,self._imgSrc.shape, dtype = np.uint8)
            self._imgKey = cv2.cvtColor(self._imgKey,cv2.COLOR_BGR2RGB)
            self._imgKeyShow = self.scaleImg(self._imgKey)
            self._imgKeyExisted = True
        else:
            self._imgKey = np.random.randint(0,255,(200,200,3), dtype = np.uint8)
            self._imgKey = cv2.cvtColor(self._imgKey,cv2.COLOR_BGR2RGB)
            self._imgKeyShow = self.scaleImg(self._imgKey)
            self._imgKeyExisted = True
            self.scaleKey()
        print('随机密钥生成完成')
    #加密
    def encrypt(self):
        if self._imgSrcExisted and self._imgKeyExisted:
            self._imgSrc = cv2.bitwise_xor(self._imgSrc, self._imgKey)
            self._imgSrcShow = self.scaleImg(self._imgSrc)
            print('加密完成')
        else:
            print('不存在')
    #解密
    def decrypt(self):
        if self._imgSrcExisted and self._imgKeyExisted:
            self._imgSrc = cv2.bitwise_xor(self._imgSrc, self._imgKey)
            self._imgSrcShow = self.scaleImg(self._imgSrc)
            print('解密完成')
        else:
            print('不存在')
    #缩放图片
    def scaleImg(self, img):
        h,w,ch = img.shape
        img = cv2.resize(img, (1*self._expand, int(h/w*self._expand)))
        return img

    #删除图片
    def deleteImg(self):
        if self._imgSrcExisted:
            self._imgSrc = None
            self._imgSrcShow = None
            self._imgSrcPath = None
            self._imgSrcExisted = False

    #删除密钥
    def deleteKey(self):
        if self._imgKeyExisted:
            self._imgKey = None
            self._imgKeyPath = None
            self._imgKeyShow = None
            self._imgKeyExisted = False

if __name__ == '__main__':
    print('调试')



