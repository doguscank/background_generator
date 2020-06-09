import cv2
import numpy as np
import shape_lib as sl

sc = sl.Square(800, (255, 0, 0), (255, 255, 255), random_directions = True, debug = False)
square = sc.create_square()
bg = sc.triangulate(10, gradient = True)

#print(bg)

"""
bg_creator = sl.Creator()
bg = bg_creator.create_squares_background(500, 100, (255, 255, 255), (200, 200, 255), random_directions = True)
"""
cv2.imshow('bg gradient', bg)
"""
to_write = np.float32(bg)
to_write = 255 * to_write
to_write = np.clip(to_write, 0, 255)
to_write = np.uint8(to_write)
cv2.imwrite('result.png', to_write)
"""
cv2.waitKey(0)