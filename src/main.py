import cv2
import numpy as np
import shape_lib as sl

"""
width, height = 255, 255

white_bg = np.full((width, height, 3), 1.0)

cv2.imshow('bg', white_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

center_pt = (white_bg.shape[0] / 2, white_bg.shape[1] / 2)
print("center pt: {}".format(center_pt))

for i in range(1, 256):
	white_bg[:, i - 1] = (i / float(width), (float(height) - i) / float(height), 0.0)

cv2.imshow('bg gradient', white_bg)
cv2.waitKey(0)
"""
#square = sl.gradient_square(150, (100, 100, 100), (255, 0, 255), direction = 'v')
"""
while True:
	try:
		square = sl.create_sqaures_background(500, 20, (255, 255, 255), (255, 255, 0), random_directions = True, percentage = 0.85)
	except:
		continue
	break
"""
square = sl.create_sqaures_background(500, 50, (180, 105, 255), (255, 255, 255), random_directions = True)

cv2.imshow('bg gradient', square)
cv2.waitKey(0)