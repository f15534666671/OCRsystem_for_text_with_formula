# -*- coding: utf-8 -*-
# course assignments ------ image process system
#     a OCR system for printed text with formulas

from skimage import io
from preprocess import image_preprocess, image_split
from preprocess import image_discard_blank, image_discard_side
from preprocess import image_classify
# from textrecognition import text_recognition
# from formularecognition import formula_recognition
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

img_name = 'IMG_6'
img_format = '.jpg'

# load the raw image
img_path = './raw_img/'
img = io.imread(img_path + img_name + img_format)
io.imshow(img)
io.show()


# preprocess image
img_preprocessed = image_preprocess(img)
img_preprocessed_path = './preprocessed_img/'
io.imsave(img_preprocessed_path + img_name + img_format,
          img_preprocessed.astype(int))

# split image by line
img_split = image_split(img_preprocessed)
img_split = image_discard_blank(img_split)
img_split = image_discard_side(img_split)
img_split_path = './split_img/'
for i in range(len(img_split)):
    # print(img_split[i].shape)
    img_split_name = img_split_path + img_name + '_' + str(i) + img_format
    io.imsave(img_split_name, img_split[i])



# classify and analysis
labels = ['formula'] * len(img_split)
print(labels)
i = 0


print(labels)

real_labels = ['text', 'formula', 'formula', 'text', 'formula',
          'text', 'formula', 'text', 'formula', 'text', 'text',
          'formula']
print(real_labels)