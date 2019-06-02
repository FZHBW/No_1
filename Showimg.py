import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import cv2

#打开图像文件
img = mpimg.imread('/Users/huangyh/Documents/PythonLearning/Model/No_1/IMG_0579.jpg')
print(img.shape)
#必要变量声明与初始化
PT=[]
linedata=[]

data=np.array(img)


rdata=(data[:,:,0].flatten())
gdata=(data[:,:,1].flatten())
bdata=(data[:,:,2].flatten())
covx=[rdata.tolist(),gdata.tolist(),bdata.tolist()]
covx=np.array(covx)
print (np.cov(covx)/len(rdata))


#必要函数声明
def on_press(event):
    global PT
    if event.button==1 and len(PT)<2: #鼠标左键点击
        PT.append([int(event.xdata),int(event.ydata)])
        print(PT)
    elif event.button==3: #鼠标右键点击
        PT=[]
        print("clear positions")
    elif len(PT)==2:
        figline=plt.figure("line")
        x=PT[0][0]
        k=(PT[0][1]-PT[1][1])/(PT[1][0]-PT[0][0])
        b=-PT[0][1]-k*PT[0][0]
        while x<=PT[1][0]:
            global linedata
            y=-int(k*x+b)
            linedata.append(img[y][x])
            x+=1
        linedata=np.array(linedata)
        
        n=0
        name=['red', 'green', 'blue']
        while n<3:
            plt.subplot(1,3,n+1)
            
            plt.bar(range(len(linedata)),height=linedata[:,n],width=0.4,color=name[n])
            n+=1
        plt.show()


#显示正常RGB图像
fig1=plt.figure("Image")
plt.subplot(2,3,1)
plt.imshow(img)
plt.title('RGB')
plt.axis('off')
fig1.canvas.mpl_connect('button_press_event', on_press)

#矩阵乘法生成灰度值图像
plt.subplot(2,3,2)
wheight=np.array([0.299,0.587,0.114])
imggray=np.dot(data,wheight)
plt.title('Gray')
plt.imshow(imggray,cmap='gray')
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(img[:,:,0],cmap='gray')
plt.axis('off')
plt.title('R')
plt.subplot(2,3,4)
plt.imshow(img[:,:,1],cmap='gray')
plt.axis('off')
plt.title('G')
plt.subplot(2,3,5)
plt.imshow(img[:,:,2],cmap='gray')
plt.axis('off')
plt.title('B')
plt.axis('off')

#直方图可视化
i=1
fig2=plt.figure("Historigram",figsize=(12,4))
name=['red', 'green', 'blue']
while i<=3: 
    plt.subplot(1,3,i)
    n,bins,patches = plt.hist(x=img[:,:,i-1].flatten()*255, bins=16, density = 1,color=name[i-1], alpha=0.7, rwidth=0.85)
    plt.grid(axis='y')
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.xlabel(..., fontsize=6)
    plt.ylabel(..., fontsize=6)
    plt.subplots_adjust(wspace =0.5, hspace =0)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(name[i-1])
    maxfreq = n.max()
    i+=1


#计算协方差

#图像显示
plt.show()



