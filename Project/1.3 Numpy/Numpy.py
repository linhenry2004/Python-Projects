import numpy
import cv2
im_g = cv2.imread("smallgray.png", 0)
im_g = cv2.imwrite("newsmallgray.png", im_g)

for i in im_g:
    for j in im_g[i]:
        print(j)

imh = numpy.hstack((im_g, im_g))
imv = numpy.vstack((im_g, im_g))

print(numpy.hsplit(imh, 5))
print(numpy.vsplit(imv, 3))
#Run on jupyter
