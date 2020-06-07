import cv2
import numpy as np
import random

def random_direction():
	directions = ['v', 'h', 'vr', 'hr']
	return directions[random.randint(0, 3)]

#Edge length, color
def square(l, color = (255, 255, 255)):
	s = np.full((l, l, 3), (color[0] / 255.0, color[1] / 255.0, color[2] / 255.0))

	return s

#Edge length, start color, end color, direction => 'v'ertical, 'h'orizontal
def gradient_square(l, start_color, end_color, direction = 'h'):
	s = square(l)
	[SB, SG, SR] = [i / float(255.0) for i in start_color]
	[EB, EG, ER] = [i / float(255.0) for i in end_color]

	B_sign = 1
	G_sign = 1
	R_sign = 1

	print("{} {} {} {} {} {}".format(SB, EB, SG, EG, SR, ER))
	#print("{} {} {}".format(B_sign, G_sign, R_sign))
	
	if direction.lower() == 'h':
		for i in range(l):
			s[:, i] = (SB + (EB - SB) * i / float(l), SG + (EG - SG) * i  / float(l), SR + (ER - SR) * i  / float(l))
			#print((SB + (EB - SB) * i / float(l), SG + (EG - SG) * i  / float(l), SR + (ER - SR) * i  / float(l)))
	elif direction.lower() == 'v':
		for i in range(l):
			s[i] = (SB + (EB - SB) * i / float(l), SG + (EG - SG) * i  / float(l), SR + (ER - SR) * i  / float(l))
			#print((SB + (EB - SB) * i / float(l), SG + (EG - SG) * i  / float(l), SR + (ER - SR) * i  / float(l)))
	return s
"""
def create_sqaures_background(max_l, num_squares, first_color, second_color, direction = 'h', random_directions = False, percentage = 0.9):
	if random_directions:
		direction = random_direction()

	percentage = min(0.99, percentage)

	if 'r' in direction:
		print("before: {} {}".format(first_color, second_color))
		temp = first_color
		first_color = second_color
		second_color = temp
		direction = direction[0]
		print("after: {} {}".format(first_color, second_color))

	main_square = gradient_square(max_l, first_color, second_color, direction)
	squares = list()

	for i in range(num_squares - 1):
		if random_directions:
			direction = random_direction()

		if 'r' in direction:
			print("before: {} {}".format(first_color, second_color))
			temp = first_color
			first_color = second_color
			second_color = temp
			direction = direction[0]
			print("after: {} {}".format(first_color, second_color))

		l = int(max_l * random.uniform(0, percentage))
		new_square = gradient_square(l, first_color, second_color, direction)

		rx = min(int(max_l * random.uniform(0, percentage)), max_l - l - 5)
		ry = min(int(max_l * random.uniform(0, percentage)), max_l - l - 5)
		print(rx, ry, l)
		print(int(max_l / 2) - rx, int(max_l / 2) - rx + l, int(max_l / 2) - ry, int(max_l / 2) - ry + l)
		_ = input()

		squares.append([l, new_square, int(max_l / 2) - rx, int(max_l / 2) - rx + l, int(max_l / 2) - ry, int(max_l / 2) - ry + l])

	squares = sorted(squares, key = lambda item: item[0], reverse = True)
	
	for s in squares:
		main_square[s[2]: s[3], s[4]: s[5]] = s[1]

	return main_square
"""