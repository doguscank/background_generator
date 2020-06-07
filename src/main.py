import cv2
import numpy as np
import shape_lib as sl

square = sl.create_sqaures_background(500, 50, (180, 105, 255), (255, 255, 255), random_directions = True)

cv2.imshow('bg gradient', square)
cv2.waitKey(0)