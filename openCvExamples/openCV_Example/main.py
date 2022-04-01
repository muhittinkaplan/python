#first --  conda install -c conda-forge opencv=4.1.0

import cv2
print(cv2.__version__)
img=cv2.imread('images.jpeg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
