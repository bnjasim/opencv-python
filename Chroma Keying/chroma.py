from __future__ import division
import cv2
import numpy as np 

 
gk = 255
bk = 0
k = gk - bk 
# im_foreground = cv2.imread('snap.png')
video = cv2.VideoCapture('zebra-chroma-key.mp4')

retval, im_foreground = video.read()
count = 1
while(retval):
	im_background = cv2.imread('london.jpg')
	out_name = 'composite/' + str(count) + '.jpg'

	for i in range(438, 774):
		for j in range(212, 808):
			foreground_pixel = im_foreground[i-438, j-212]
			background_pixel = im_background[i,j]
			# check if the pixel is the constant background green. 
			# Allow some tolerance in the green [3, 255, 15]
			b = foreground_pixel[0]
			g = foreground_pixel[1]
			r = foreground_pixel[2]

			# Simple thresholding
			#if (b < 30 and g > 200 and r < 70):
			#	pass
			#else:
			#	im_background[i, j] = foreground_pixel

			# Using SOLUTION 2: GRAY OR FLESH in the paper Blue Screen Matting by Alvy Ray
			# Find alpha
			
			alpha = (k + b - g) / k

			if (alpha > 1):
				alpha = 1

			if (alpha < 0):
				alpha = 0

			# Blended image C = Co + (1-alpha) Cb
			# where Cb is the background image
			bo = b - (1-alpha)*bk
			go = g - (1-alpha)*gk
			# bo is approx equal to go

			Co = [bo, go, r]

			C_temp = Co + (1-alpha)*background_pixel
			C = np.array([int(pix) for pix in C_temp])

			im_background[i,j] = C


	# The height of image is 775. we make it 774 as ffmpeg requires even dimensions
	cv2.imwrite(out_name, im_background[0:774, :])

	count += 1
	
	retval, im_foreground = video.read()



video.release()
cv2.destroyAllWindows()
