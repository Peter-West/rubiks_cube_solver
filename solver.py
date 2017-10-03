import copy
import math
import pprint as pp

import pyglet
from graph_3d import Graph_3D

class Solver():

	def __init__(self, cube3d_root, cube3d_goal, rotation_func):
		self.cube3d_root = cube3d_root
		self.cube3d_goal = cube3d_goal
		
		self.rot = rotation_func
		ret_corners = self.corners_positions()
		# pp.pprint(len(ret_corners['path']))
		# pp.pprint(self.corners_goal[0])
		# self.breadth_first_search(self.corners_goal)
		# patterns = self.pattern_database(ret_corners, [])

		WIDTH = 800
		HEIGHT = 800
		# Graph_3D(WIDTH, HEIGHT, 'Cube 3D !', ret_corners['path'][-1])
		# pyglet.app.run()


	def breadth_first_search(self, s):
		available_rotation = ['U', 'F', 'R', 'B', 'L', 'D', "U'", "F'", "R'", "B'", "L'", "D'", 'U2', 'F2', 'R2', 'B2', 'L2', 'D2']
		f = []
		f.append(s)
		data = []
		while f:
			s = f.pop()
			# print(s)
			# print("********")
			for rot in available_rotation:
				t = copy.deepcopy(s)
				# pp.pprint(t)
				self.rot(rot, t)
				# if t not in f:
				data.append(t)
				print('len file : ', len(data))
				f.append(t)



	# def pattern_database(ret_corners, patterns):
	# 	count = 0
	# 	while True:
			
	# 		if (count = 88 179 840)
	# 			break
	# 		count += 1


	# 	return patterns

	def corners_positions(self):
		corners_root = []
		for block in self.cube3d_root:
			if (block['block_type'] == 'corner'):
				corners_root.append(block)
		self.corners_goal = []	
		for block in self.cube3d_goal:
			if (block['block_type'] == 'corner'):
				self.corners_goal.append(block)
				# self.corners_goal.append({'branded':False , 'block': Block})
		# return
		return self.ida_star(corners_root)

	def	h(self, node):
		# Md3d
		md3d = 0
		for corner_goal in self.corners_goal:
			for block in node:
				if (block['value'] == corner_goal['value']):
					md3d += abs(corner_goal['x'] - block['x']) + abs(corner_goal['y'] - block['y']) + abs(corner_goal['z'] - block['z'])
		# print(md3d)
		return (md3d)
		# return (1)

	def cost(self, node, succ):
		md3d = 0
		for block_succ in succ:
			if (block_succ['block_type'] == 'corner'):
				for block in node:
					if (block['value'] == block_succ['value']):
						md3d += abs(block_succ['x'] - block['x']) + abs(block_succ['y'] - block['y']) + abs(block_succ['z'] - block['z'])
		return (md3d)
		# return (1)

	def is_goal(self, node):
		return True if (self.corners_goal == node) else False

	def successors_ordered(self, node):
		available_rotation = ['U', 'F', 'R', 'B', 'L', 'D', "U'", "F'", "R'", "B'", "L'", "D'", 'U2', 'F2', 'R2', 'B2', 'L2', 'D2']
		succ = []
		for rot in available_rotation:
			n_cpy_h = {'node': copy.deepcopy(node), 'h':0}
			self.rot(rot, n_cpy_h['node'])
			# pp.pprint(node_copy)
			n_cpy_h['h'] = self.h(n_cpy_h['node'])
			succ.append(n_cpy_h)
		for s in succ:
			pp.pprint(s['h'])
		print('*********')
		succ_2 = sorted(succ, key=lambda k: k['h'])
		for s in succ_2:
			pp.pprint(s['h'])
		print('00000000000')

		return (succ)

	def successors(self, node):
		available_rotation = ['U', 'F', 'R', 'B', 'L', 'D', "U'", "F'", "R'", "B'", "L'", "D'", 'U2', 'F2', 'R2', 'B2', 'L2', 'D2']
		succ = []
		for rot in available_rotation:
			node_copy = copy.deepcopy(node)
			self.rot(rot, node_copy)
			succ.append(node_copy)
		return (succ)

	def ida_star(self, root):
		bound = self.h(root)
		path = [root]
		# print('path:', path)
		while 1:
			t = self.search(path, 0, bound)
			if (t == 'FOUND'):
				# print('heyyyy ')
				# print('path : ', path)
				# print('bound : ', bound)
				return {'path':path, 'bound':bound}
			if (t == math.inf):return ('NOT_FOUND')
			bound = t

	def search(self, path, g, bound):
		node = path[-1]
		f = g + self.h(node)
		# print('f: ', f)
		if (f > bound):return f
		if (self.is_goal(node)): return ('FOUND')
		minimum = math.inf
		for succ in self.successors(node):
			if (succ not in path):
				path.append(succ)
				t = self.search(path, g + self.cost(node, succ), bound)
				if (t == 'FOUND'):return ('FOUND')
				if (t < minimum):
					minimum = t
					# print('minimum : ', minimum)
				path.pop()
		return minimum