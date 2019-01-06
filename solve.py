# 参考 https://www.cnblogs.com/k7k8k91/p/7989630.html
import caffe
import surgery, score

import numpy as np
import os
import sys

try:
    import setproctitle
    setproctitle.setproctitle(os.path.basename(os.getcwd()))
except:
    pass

weights = 'snapshot/train_iter_12000.caffemodel'
deploy_proto = 'deploy.prototxt'

# init
#caffe.set_device(int(sys.argv[1]))
#caffe.set_mode_gpu()
caffe.set_mode_cpu()

solver = caffe.SGDSolver('solver.prototxt')
#solver.net.copy_from(weights)
vgg_net=caffe.Net(deploy_proto,weights,caffe.TRAIN) 
surgery.transplant(solver.net,vgg_net) 
del vgg_net  

# surgeries
interp_layers = [k for k in solver.net.params.keys() if 'up' in k]
surgery.interp(solver.net, interp_layers)

# scoring
val = np.loadtxt('data/_val.txt', dtype=str)

for _ in range(25):
    solver.step(4000)
    score.seg_tests(solver, False, val, layer='score')
