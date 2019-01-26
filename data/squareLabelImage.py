# 参考链接：https://stackoverflow.com/questions/7733364/python-pil-create-indexed-color-image-with-transparent-background
# 将label的大小调整为正方形
from PIL import Image
import numpy as np
import re  
import os  
import time  

squareLength = 110

def func(picDir):  
    global i  
    # 读取一张正确的8bit indexed图 获取其中的palette
    img = Image.open("palette.png")
    # Get the colour palette
    palette = img.getpalette()
    # Determine the total number of colours
    # num_colours = len(palette)/3
    # Create a colour map matrix
    # map = np.array(palette).reshape(num_colours, 3)
    # 判断是否为文件夹
    if os.path.isdir(picDir):  
        #列举labelImage文件夹下面的所有文件
        for x in os.listdir(picDir + '/labelImage'):
            lists = x.split('.') #分割出文件与文件扩展名  
            file_ext = lists[-1] #后缀名
            file_name = lists[0] #文件名
            img_ext = ['bmp','jpeg','gif','psd','png','jpg']  
            #判断是否为图片
            if file_ext in img_ext:  
                # 读取一张8bit png标签图
                Img_8bit = Image.open(picDir + '/labelImage/' + x)
                testnp = np.array(Img_8bit)
                #np.savetxt('array.txt',testnp)
                newImg = Image.new('P', [squareLength, squareLength], 0)
                newImg.putpalette(palette)
                pixels = newImg.load()
                pos_start_x = (squareLength - Img_8bit.width)/2
                pos_start_y = (squareLength - Img_8bit.height)/2
                for width in range(Img_8bit.width):
                    for height in range(Img_8bit.height):
                        arr = testnp[height][width]
                        if (arr == 0):
                            pixels[pos_start_x+width, pos_start_y+height] = 0 # 背景
                        elif (arr == 1):
                            pixels[pos_start_x+width, pos_start_y+height] = 1 # 种子
                        elif (arr == 2):
                            pixels[pos_start_x+width, pos_start_y+height] = 2 # 胚
                        else:
                            pixels[pos_start_x+width, pos_start_y+height] = 3 # 其他为垩白
                newImg.save(picDir + '/labelImage_square/' + x)
                
                i = i+1
                print('Image %s ok!'%(i))

present_dir = os.getcwd()
start = time.time()  
i = 0  
func(present_dir)  
c = time.time() - start  
print('time: %0.2f'%(c))  
print('count: %s images'%(i)) 