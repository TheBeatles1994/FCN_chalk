import numpy as np
from PIL import Image
import caffe
import vis
import os  
import time
# 模型版本
model_number = 100000
# 保存图片的文件夹
save_img_dir = './demo/result_visual/'
# 原图文件夹
img_dir = './demo/demo_img/'

# 计数图片数量
count = 0
total_time = 0
# 加载网络
print('The FCN is initializing...')
net = caffe.Net('deploy.prototxt', 'snapshot/train_iter_' +  str(model_number) + '.caffemodel', caffe.TEST)
# 对原图文件夹下的所有图片进行处理并保存
if os.path.isdir(img_dir):
    
    for x in os.listdir(img_dir):
        lists = x.split('.') # 分割出文件与文件扩展名  
        file_ext = lists[-1] # 后缀名
        file_name = lists[0] # 文件名
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']  
        # 判断是否为图片
        if file_ext in img_ext:  
            print(x + ' is in process.')
            start = time.time()
            # 加载读取的图片，并转化为BGR格式，同时减去mean值，并将数据维度变成Caffe框架支持的维度，即C x H x W
            im = Image.open(img_dir + x)
            in_ = np.array(im, dtype=np.float32)
            in_ = in_[:,:,::-1]
            in_ -= np.array((55.06, 55.06, 55.06))
            in_ = in_.transpose((2,0,1))
            # shape for input (data blob is N x C x H x W), set data
            net.blobs['data'].reshape(1, *in_.shape)
            net.blobs['data'].data[...] = in_
            # run net and take argmax for prediction
            net.forward()
            out = net.blobs['score'].data[0].argmax(axis=0)
            end = time.time()
            total_time = total_time + (end-start)
            # 保存处理后的文件
            im.save(save_img_dir + x)
            voc_palette = vis.make_palette(21)
            out_im = Image.fromarray(vis.color_seg(out, voc_palette))
            out_im.save(save_img_dir + file_name + '_FCN_' + str(model_number) + '.png')
            masked_im = Image.fromarray(vis.vis_seg(im, out, voc_palette))
            masked_im.save(save_img_dir + file_name + '_Visual_' + str(model_number) + '.jpg')
        else:
            print('Notice: ' + x + ' is not a pic!')
        count = count + 1
    

print('Done!')
print('Total time: %0.2f.'%total_time)  
print('Average time: %0.2f.'%(total_time/count))  
print('Count: %s images.'%(count)) 


