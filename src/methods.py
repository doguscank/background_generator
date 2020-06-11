import numpy as np
import random
import math

class Voronoi():
	def __init__(self, pts = None):
		self.pts = pts

	def init_centers(self, random = True, centers = None, num_pts = 10, l = 500, w = 500):
		if not random:
			if centers:
				pts = centers
			elif self.pts:
				pts = self.pts
			else:
				pts = list()

				for i in range(num_pts):
					pts.append(self.random_pt((1, w - 1), (1, l - 1)))
		else:
			pts = list()

			for i in range(num_pts):
				pts.append(self.random_pt((1, w - 1), (1, l - 1)))

		return pts

	def random_pt(self, range_x, range_y):
		return (random.randint(range_x[0], range_x[1]), random.randint(range_y[0], range_y[1]))

	def random_color_list(self, n):
		colors = list()

		for i in range(n):
			b = random.randint(0, 255)
			g = random.randint(0, 255)
			r = random.randint(0, 255)

			colors.append((b, g, r))

		return colors

	def init_img(self, w, l):
		self.img = np.full((w, l, 3), (0.0, 0.0, 0.0), dtype = np.uint8)

		return self.img

	def get_dist(self, coord1, coord2):
		return math.sqrt(math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1], 2))

	def find_closest_pt(self, centers, px_coords):
		min_dist = 9999999999999999999
		min_coords = None

		for c in centers:
			d = self.get_dist(px_coords, c)

			if d < min_dist:
				min_coords = c
				min_dist = d

		return min_coords

	def voronoi(self, w, l, random = True, centers = None, num_pts = 10):
		img = self.init_img(w, l)
		pts = self.init_centers(random, centers, num_pts, l = l, w = w)
		colors = self.random_color_list(num_pts)

		for i in range(l):
			for j in range(w):
				closest_center = self.find_closest_pt(pts, (i, j))
				index = pts.index(closest_center)
				img[i][j] = colors[index]

		return img