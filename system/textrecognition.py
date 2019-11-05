from skimage import io
import pytesseractcp
import os

print("tesseract version: ", pytesseractcp.get_tesseract_version())

# for i in range(14):
#     img_path = './imagedata/IMG_6_{}.jpg'.format(str(i))
#     img = io.imread(img_path)
#     # io.imshow(img)
#     # io.show()
#
#     # print("recognizing image " + str(i) + " ......", img.shape)
#     img_string = pytesseractcp.image_to_string((img), lang='chi_sim', path='/home/wangsen/Desktop/')
#     print(img_string)

def text_recognition(img):
    text = pytesseractcp.image_to_string((img), lang='chi_sim', path=os.getcwd())
    return text