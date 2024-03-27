
import Util
import matplotlib.pyplot as plt
import cv2

import numpy as np

def img_test():
    img=Util.cv_imread(r"./206-田海龙-北京/第02周/lenna.png")
    print(img.shape)

    # 直接matplotlib显示图片，是正常的
    # import matplotlib.image as mpimg
    # img = mpimg.imread(r"D:\Desktop\maomi.jpg")

    # import cv2
    # # cv2加载的图片颜色显示不正确
    # img=cv2.imread(r"D:\Desktop\maomi.jpg")

    # 需要把通道顺序转下
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.show()

    # 调整颜色设置
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    h,w = img.shape[:2]                               #获取图片的high和wide
    img_gray = np.zeros([h,w],img.dtype)                   #创建一张和当前图片大小一样的单通道图片
    # 自己写方法，实现灰度
    for i in range(h):
        for j in range(w):
            #取出当前high和wide中的BGR坐标
            m = img[i,j]                             
            #将BGR坐标转化为gray坐标并赋值给新图像
            # img_gray[i,j] = int(m[0]*0.1 + m[1]*0.4 + m[2]*0.5)   
            # 平均值法，效果不好
            # img_gray[i,j] = int((m[0] + m[1] + m[2])/3)
            # 直接取G颜色，效果还可以
            img_gray[i,j] = m[1]
            # 取其他颜色也还可以，保持相关对比度吧
            img_gray[i,j] = m[2]

    cv2.imshow("image show gray",img_gray)
    cv2.waitKey(0)

img_test()

# 向量乘法练习
A=np.arange(6)
A=A.reshape(3,2)

B=A.reshape(2,3)

print(A)
print(B)

print(A.dot(B))
