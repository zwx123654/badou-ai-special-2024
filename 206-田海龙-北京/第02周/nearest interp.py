
import cv2
import numpy as np
import Util

def function(img):
    height,width,channels =img.shape
    emptyImage=np.zeros((800,800,channels),np.uint8)

    # 比例
    sh=800/height
    sw=800/width

    for i in range(800):
        for j in range(800):
            # x/y为缩放后原图的像素点位置
            x=int(i/sh + 0.5)  #int(),转为整型，使用向下取整。
            y=int(j/sw + 0.5)
            emptyImage[i,j]=img[x,y]

    return emptyImage

def function(img,w,h):
    """
    可以设置缩放后的宽高
    """
    height,width,channels =img.shape
    emptyImage=np.zeros((h,w,channels),np.uint8)

    print(height,width)

    # 比例
    sh=h/height
    sw=w/width

    for i in range(h):
        for j in range(w):
            # x/y为缩放后原图的像素点位置
            # 这里是先高后宽
            x=int(i/sh + 0.5)  #int(),转为整型，使用向下取整。
            y=int(j/sw + 0.5)
            emptyImage[i,j]=img[x,y]

    return emptyImage
    
# cv2.resize(img, (800,800,c),near/bin)

imgPath='./206-田海龙-北京/第02周/lenna.png'

# cv2不支持中文路径
# img=cv2.imread(imgPath)
img=Util.cv_imread(imgPath)

zoom=function(img,600,800)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)


