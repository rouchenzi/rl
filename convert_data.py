import scipy.io
import numpy as np
import os
import scipy.ndimage as spm

for i in range(0, 15):
    if i == 12:
        continue
    mat = scipy.io.loadmat('new_data/outAll'+str(i)+'.mat')
    data = np.array(mat['out'])
    dir = 'new_data/output'+str(i)+'/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    dims = data.shape
    x0 = dims[0]
    y0 = dims[1]
    z0 = dims[2]
    time = dims[3]
    data_new = []
    for t in range(time):
        data_new.append(data[:, :, :, t])

    #print(data_new[0].shape)
    for j in range(len(data_new)):
        data = data_new[j]
        data = data.swapaxes(0, 1)
        data = spm.zoom(data, [1, 208.0 / 224, 1])
        np.save(os.path.join(dir, 'outAll'+str(i)+'_'+str(j)), data)

# te = np.load('outAll0.npy')
# te = te[1]
# print(te.shape)'
