import copy

class Rotation():
	def __init__(self):
		pass

	def rotation_matrix_clockwise(self, axe, item):
		copy_item = copy.deepcopy(item)
		if (axe == 'z'):
			item['x'] = copy_item['y']
			item['y'] = copy_item['x'] * -1
		if (axe == 'y'):
			item['x'] = copy_item['z'] * -1
			item['z'] = copy_item['x']
		if (axe == 'x'):
			item['y'] = copy_item['z']
			item['z'] = copy_item['y'] * -1

	def rotation_matrix_counterclockwise(self, axe, item):
		copy_item = copy.deepcopy(item)
		if (axe == 'z'):
			item['x'] = copy_item['y'] * -1
			item['y'] = copy_item['x']
		if (axe == 'y'):
			item['x'] = copy_item['z']
			item['z'] = copy_item['x'] * -1
		if (axe == 'x'):
			item['y'] = copy_item['z'] * -1
			item['z'] = copy_item['y']
	
	def rotation_matrix_180(self, axe, item):
		copy_item = copy.deepcopy(item)
		if (axe == 'z'):
			item['x'] = copy_item['x'] * -1
			item['y'] = copy_item['y'] * -1
		if (axe == 'y'):
			item['x'] = copy_item['x'] * -1
			item['z'] = copy_item['z'] * -1
		if (axe == 'x'):
			item['y'] = copy_item['y'] * -1
			item['z'] = copy_item['z'] * -1

	def rotation(self, rot_side, cube):
		for block in cube:
			if (rot_side == 'U'):
				if (block['z'] == 1):
					self.rotation_matrix_clockwise('z', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('z', face)
			if (rot_side == 'D'):
				if (block['z'] == -1):
					self.rotation_matrix_counterclockwise('z', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('z', face)
			if (rot_side == 'R'):
				if (block['y'] == 1):
					self.rotation_matrix_clockwise('y', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('y', face)
			if (rot_side == 'L'):
				if (block['y'] == -1):
					self.rotation_matrix_counterclockwise('y', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('y', face)
			if (rot_side == 'F'):
				if (block['x'] == 1):
					self.rotation_matrix_clockwise('x', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('x', face)
			if (rot_side == 'B'):
				if (block['x'] == -1):
					self.rotation_matrix_counterclockwise('x', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('x', face)
	# sens inverse
			if (rot_side == "U'"):
				if (block['z'] == 1):
					self.rotation_matrix_counterclockwise('z', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('z', face)
			if (rot_side == "D'"):
				if (block['z'] == -1):
					self.rotation_matrix_clockwise('z', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('z', face)
			if (rot_side == "R'"):
				if (block['y'] == 1):
					self.rotation_matrix_counterclockwise('y', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('y', face)
			if (rot_side == "L'"):
				if (block['y'] == -1):
					self.rotation_matrix_clockwise('y', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('y', face)
			if (rot_side == "F'"):
				if (block['x'] == 1):
					self.rotation_matrix_counterclockwise('x', block)
					for face in block['faces']:
						self.rotation_matrix_counterclockwise('x', face)
			if (rot_side == "B'"):
				if (block['x'] == -1):
					self.rotation_matrix_clockwise('x', block)
					for face in block['faces']:
						self.rotation_matrix_clockwise('x', face)

	# 180 degres
			if (rot_side == "U2"):
				if (block['z'] == 1):
					self.rotation_matrix_180('z', block)
					for face in block['faces']:
						self.rotation_matrix_180('z', face)
			if (rot_side == "D2"):
				if (block['z'] == -1):
					self.rotation_matrix_180('z', block)
					for face in block['faces']:
						self.rotation_matrix_180('z', face)
			if (rot_side == "R2"):
				if (block['y'] == 1):
					self.rotation_matrix_180('y', block)
					for face in block['faces']:
						self.rotation_matrix_180('y', face)
			if (rot_side == "L2"):
				if (block['y'] == -1):
					self.rotation_matrix_180('y', block)
					for face in block['faces']:
						self.rotation_matrix_180('y', face)
			if (rot_side == "F2"):
				if (block['x'] == 1):
					self.rotation_matrix_180('x', block)
					for face in block['faces']:
						self.rotation_matrix_180('x', face)
			if (rot_side == "B2"):
				if (block['x'] == -1):
					self.rotation_matrix_180('x', block)
					for face in block['faces']:
						self.rotation_matrix_180('x', face)
