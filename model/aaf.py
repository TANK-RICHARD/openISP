#!/usr/bin/python
import numpy as np
from scipy.ndimage import correlate

class AAF:
    'Anti-aliasing Filter'

    def __init__(self, img):
        self.img = img

    def padding(self):
        img_pad = np.pad(self.img, (2, 2), 'reflect')
        return img_pad

    def execute(self):
        img_pad = self.padding()
        raw_h = self.img.shape[0]
        raw_w = self.img.shape[1]
        aaf_img = correlate(self.img, np.array([[1, 0, 1, 0, 1],
                                                [0, 0, 0, 0, 0],
                                                [1, 0, 8, 0, 1],
                                                [0, 0, 0, 0, 0],
                                                [1, 0, 1, 0, 1]])/16)
        self.img = aaf_img
        return self.img

def _load_img(raw_path, raw_h, raw_w, dtype='uint16'):
    t_b = get_tick()
    rawimg = np.fromfile(raw_path, dtype='uint16', sep='')
    rawimg = rawimg.reshape([raw_h, raw_w])
    print(50*'-' + '\nLoading RAW Image Done......')
    print('\nsec:%d'%(get_tick() - t_b))

    return rawimg

if __name__ == "__main__":
    
    img = _load_img('../test_img', 600, 800, '')
    aaf = AAF()