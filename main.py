import numpy as np
import cv2 as cv
import img64
import base64

imagesPath = 'images'

def base64_to_cvImage():
    original = base64.b64decode(img64.img64)
    npimg = np.frombuffer(original, dtype=np.uint8)
    cv_image = cv.imdecode(npimg, 1)
    resize(cv_image, 200)
    #cv.imwrite('test.jpg',cv_image)

def resize(image,scale):
    width, height = image.shape[:2]
    dim = (int(height*scale/100), int(width*scale/100))
    image_resize = cv.resize(image, dim);
    return image_resize

def save_image(image, imageName):
    cv.imwrite(imagesPath+'/'+imageName)

image = base64_to_cvImage()
cv.imshow('Resize image', image)

cv.waitKey(0)
cv.destroyAllWindows()
