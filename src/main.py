import cv2
import numpy as np
import shape_lib as sl

sc = sl.Square(500, (255, 0, 0), (255, 255, 255), random_directions = True, debug = True)
square = sc.create_square()

bg_creator = sl.Creator()
bg = bg_creator.create_squares_background(500, 100, (255, 255, 255), (200, 200, 255), random_directions = True)

cv2.imshow('bg gradient', bg)
cv2.waitKey(0)