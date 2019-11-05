from skimage import color
from skimage.filters import threshold_sauvola
import numpy as np
import matplotlib.pyplot as plt

def image_preprocess(img):
    # convert image to gray space
    img_gray = color.rgb2gray(img)
    # filter by sauvola
    window_size = 25
    thresh_sauvola = threshold_sauvola(img_gray, window_size=window_size)
    binary_sauvola = img_gray > thresh_sauvola
    return binary_sauvola

def image_split(img):

    split_sign = np.sum(img, axis=1)
    split_list = []
    label = 0
    for i in range(len(split_sign)):
        #print(split_sign[i])
        if label == 0:
            if split_sign[i] != img.shape[1]:
                split_list.append(i)
                label = 1
                continue
        elif label == 1:
            if split_sign[i] == img.shape[1]:
                split_list.append(i)
                label = 0
                continue
    # print(split_list)
    assert (len(split_list) % 2) == 0
    split_imgs = []
    for i in range(0, len(split_list), 2):
        split_imgs.append(img[split_list[i]:split_list[i+1], :].astype(int))

    return split_imgs

def image_discard_blank(img):
    blank = []
    for i in range(len(img)):
        if img[i].shape[0] <= 5:
            blank.append(i)

    while blank:
        i = blank.pop()
        img.pop(i)

    return img

def image_discard_side(img):
    i = 0
    for strip in img:
        strip_neg = (strip.astype(bool) == False)[:, :-3]
        strip_projection = np.sum(strip_neg, axis=0)
        strip_projection = strip_projection.astype(bool)

        if i == 0:
            total_projection = strip_projection
        else:
            total_projection = strip_projection

        strip_density = np.sum(strip_projection) / strip_projection.shape[0]
        strip_above_density = (strip_projection > strip_density)

        if i == 0:
            total_above_density = strip_above_density
        else:
            total_above_density += strip_above_density

        i += 1

    strip_width = total_projection.shape[0]
    raw_left_side = list(total_projection).index(True)
    raw_right_side = strip_width - (list(total_projection)[::-1]).index(True) - 1
    ripe_left_side = list(total_above_density).index(True)
    ripe_right_side = strip_width - (list(total_above_density)[::-1]).index(True) - 1

    new_img = []
    for strip in img:
        strip = strip[:, ripe_left_side:ripe_right_side]
        new_img.append(strip)

    return new_img


def image_classify(img):
    labels = ['formula'] * len(img)
    # img_dens = []
    # quarter_dens = []
    i = 0
    for strip in img:
        strip_neg = (strip.astype(bool) == False)
        strip_projection = np.sum(strip_neg, axis=0)
        # plt.plot(strip_projection)
        # plt.show()
        width = strip_projection.shape[0]
        percent = width // 100
        if np.sum(strip_projection[:percent]):
            labels[i] = 'text'
            i += 1
            continue

        deci = width // 10
        twentieth = deci // 2
        total_density = np.sum(strip_projection) / width
        twentieth_density = np.sum(strip_projection[:twentieth]) / \
                            (strip_projection[:twentieth]).shape[0]
        twentieth_deci_density = np.sum(strip_projection[twentieth:deci]) / \
                                 (strip_projection[twentieth:deci]).shape[0]
        if twentieth_density < total_density and twentieth_deci_density > total_density:
            labels[i] = 'text'
        i += 1

    return img, labels

