import numpy as np
import cv2 as cv
import img64
import base64

def base64_to_cvImage():
    original = base64.b64decode(img64.img64)
    npimg = np.frombuffer(original, dtype=np.uint8)
    cv_image = cv.imdecode(npimg, 1)
    cv.imshow('test', cv_image)
    #cv.imwrite('test.jpg',cv_image)

base64_to_cvImage()
cv.waitKey(0)
cv.destroyAllWindows()
