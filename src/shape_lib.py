import cv2
import numpy as np
import random

def random_direction():
	directions = ['v', 'h', 'vr', 'hr']
	return directions[random.randint(0, 3)]

class Square():
	def __init__(self, l, start_color = (255, 255, 255), end_color = None, direction = 'h', random_directions = False, debug = False):
		self.l = l
		self.start_color = start_color
		self.debug = debug
		self.random_directions = random_directions

		if end_color:
			self.end_color = end_color
		else:
			self.end_color = start_color

		if self.random_directions:
			self.direction = random_direction()
		else:
			self.direction = direction

	#Create square based on given parameters
	def create_square(self, l = None):
		#If a new length parameter is given, update current parameter
		if l:
			self.update_length(l)

		#If random directions are enabled, select a random direction
		if self.random_directions:
			new_direction = random_direction()

			if 'r' in new_direction:
				self.update_colors(self.end_color, self.start_color)

			self.direction = new_direction[0]

		#If no color gradient is required, return flat colored square
		if self.start_color == self.end_color:
			b, g, r = self.start_color
			self.square = np.full((self.l, self.l, 3), (b / 255.0, g / 255.0, r / 255.0))

			return self.s

		#Create white colored main square
		self.square = np.full((self.l, self.l, 3), (1.0, 1.0, 1.0))

		#Get start and end values of BGR values
		[SB, SG, SR] = [i / float(255.0) for i in self.start_color]
		[EB, EG, ER] = [i / float(255.0) for i in self.end_color]

		if self.debug:
			print("{} {} {} {} {} {}".format(SB, EB, SG, EG, SR, ER))
		
		#Create gradient based on current direction
		if self.direction.lower() == 'h':
			for i in range(self.l):
				self.square[:, i] = (SB + (EB - SB) * i / float(self.l), SG + (EG - SG) * i  / float(self.l), SR + (ER - SR) * i  / float(self.l))

				if self.debug: 
					print((SB + (EB - SB) * i / float(self.l), SG + (EG - SG) * i  / float(self.l), SR + (ER - SR) * i  / float(self.l)))

		elif self.direction.lower() == 'v':
			for i in range(self.l):
				self.square[i] = (SB + (EB - SB) * i / float(self.l), SG + (EG - SG) * i  / float(self.l), SR + (ER - SR) * i  / float(self.l))

				if self.debug: 
					print((SB + (EB - SB) * i / float(self.l), SG + (EG - SG) * i  / float(self.l), SR + (ER - SR) * i  / float(self.l)))

		return self.square

	#Update color parameters of square creator
	def update_colors(self, start_color, end_color = None):
		self.start_color = start_color

		if end_color:
			self.end_color = end_color
		else:
			self.end_color = start_color

	def update_length(self, l):
		if l > 0:
			self.l = l
		else:
			self.l = 1
			print("Invalid length value given! New value is 1px.")

		return self.l

class Creator():
	def __init__(self, debug = False):
		self.debug = debug

	#Main square edge length, number of squares to be drawn, gradient start, gradient end, direction of gradient,
	#random gradient directions, max square edge multiplier, put squares from bigger to smaller into the frame
	def create_squares_background(self, max_l, num_squares, first_color, second_color, direction = 'h', random_directions = False,
	percentage = 0.9, sort_squares = True):
		square_creator = Square(max_l, first_color, second_color, direction, random_directions)

		percentage = min(0.9, percentage)

		main_square = square_creator.create_square(max_l)
		squares = list()

		for i in range(num_squares - 1):
			l = int(max_l * random.uniform(0, percentage))
			new_square = square_creator.create_square(l)

			rx = int((max_l - l) * random.uniform(0, percentage)) #Random X point of center of the new square
			ry = int((max_l - l) * random.uniform(0, percentage)) #Random Y point of center of the new square
			
			if self.debug:		
				print(l, rx, ry, rx + l, ry + l)

			squares.append([l, rx, ry, new_square])

		if sort_squares:
			squares = sorted(squares, key = lambda square: square[0], reverse = True)

		for s in squares:
			main_square[s[1]: s[1] + s[0], s[2]: s[2] + s[0]] = s[3]

		return main_square