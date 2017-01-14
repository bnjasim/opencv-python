import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/Autumn.jpg')
print img.shape
print img.dtype


# Plotting in matplotlib. R and B are interchanged in OpenCV and matplotlib
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

cv2.imshow('Autumn', img)
print 'Press Esc to continue'
cv2.waitKey(0) # Press Esc to close the image
cv2.destroyAllWindows()