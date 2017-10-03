import sys
import copy
import pprint as pp
import pyglet
import time
from graph_3d import Graph_3D
from rotation import Rotation
from solver import Solver


cube_3d = []

def select_block_type(x, y, z):
	ret = {'type':'', 'faces':[]}
	num_type = abs(x) + abs(y) + abs(z)
	if (num_type == 3):ret['type'] = 'corner'
	if (num_type == 2):ret['type'] = 'edge'
	if (num_type == 1):ret['type'] = 'middle'
	if (x == 1):ret['faces'].append({'name':'Front', 'x':1, 'y':0, 'z':0})
	if (x == -1):ret['faces'].append({'name':'Back', 'x':-1, 'y':0, 'z':0})
	if (y == 1):ret['faces'].append({'name':'Right', 'x':0, 'y':1, 'z':0})
	if (y == -1):ret['faces'].append({'name':'Left', 'x':0, 'y':-1, 'z':0})
	if (z == 1):ret['faces'].append({'name':'Up', 'x':0, 'y':0, 'z':1})
	if (z == -1):ret['faces'].append({'name':'Down', 'x':0, 'y':0, 'z':-1})
	return(ret)

def create_cube():
	x = [-1,0,1]
	y = [-1,0,1]
	z = [-1,0,1]
	value = 0
	for c_z in z:
		for c_y in y:
			for c_x in x:
				block_type = select_block_type(c_x, c_y, c_z)
				value += 1
				cube_3d.append({'x':c_x, 'y':c_y, 'z':c_z, 'block_type':block_type['type'], 'value':value, 'faces':block_type['faces']})



def main():
	start_time = time.time()
	create_cube()
	cube_3d_goal = copy.deepcopy(cube_3d)
	# pp.pprint(cube_3d)
	r = Rotation()
	# r.rotation('U2', cube_3d)
	r.rotation('F', cube_3d)
	r.rotation('U', cube_3d)
	r.rotation("B'", cube_3d)
	r.rotation("F'", cube_3d)
	r.rotation("D'", cube_3d)
	# r.rotation("F'", cube_3d)
	# r.rotation("D'", cube_3d)
	# r.rotation('F', cube_3d)
	# r.rotation('B', cube_3d)
	# r.rotation("L'", cube_3d)

	Solver(cube_3d, cube_3d_goal, r.rotation)
	pp.pprint(time.time() - start_time)
	WIDTH = 800
	HEIGHT = 800
	Graph_3D(WIDTH, HEIGHT, 'Cube 3D !', cube_3d)
	pyglet.app.run()
	
if __name__ == '__main__':
	main()
