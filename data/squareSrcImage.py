# 参考链接：https://stackoverflow.com/questions/7733364/python-pil-create-indexed-color-image-with-transparent-background
# 将src的大小调整为正方形
from PIL import Image
import numpy as np
import re  
import os  
import time  

squareLength = 110

def func(picDir):  
    global i  
    # 判断是否为文件夹
    if os.path.isdir(picDir):  
        #列举srcImage文件夹下面的所有文件
        for x in os.listdir(picDir + '/srcImage'):
            lists = x.split('.') #分割出文件与文件扩展名  
            file_ext = lists[-1] #后缀名
            file_name = lists[0] #文件名
            img_ext = ['bmp','jpeg','gif','psd','png','jpg']  
            #判断是否为图片
            if file_ext in img_ext:  
                # 读取一张8bit png标签图
                Img = Image.open(picDir + '/srcImage/' + x)
                testnp = np.array(Img)
                #np.savetxt('array.txt',testnp)
                newImg = Image.new('RGB', [squareLength, squareLength], (0,0,0))
                pixels = newImg.load()
                pos_start_x = (squareLength - Img.width)/2
                pos_start_y = (squareLength - Img.height)/2
                for width in range(Img.width):
                    for height in range(Img.height):
                        arr = testnp[height][width]
                        pixels[pos_start_x+width, pos_start_y+height] = (arr[0],arr[1],arr[2])
                newImg.save(picDir + '/srcImage_square/' + x)
                
                i = i+1
                print('Image %s ok!'%(i))

present_dir = os.getcwd()
start = time.time()  
i = 0  
func(present_dir)  
c = time.time() - start  
print('time: %0.2f'%(c))  
print('count: %s images'%(i)) 