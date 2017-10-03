import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

class Graph_3D(pyglet.window.Window):

	xRotation = yRotation = 30  
	increment = 5

	def __init__(self, width, height, title, cube_3d):
		super(Graph_3D, self).__init__(width, height, title)
		self.cube_3d = cube_3d

		glClearColor(0, 0, 0, 1)
		glEnable(GL_DEPTH_TEST)

	def color_by_name(self, name):
		if (name == 'Front'):glColor3ub(255,0,0)
		if (name == 'Back'):glColor3ub(255,160,0)
		if (name == 'Right'):glColor3ub(0,255,0)
		if (name == 'Left'):glColor3ub(0,0,255)
		if (name == 'Up'):glColor3ub(255,255,0)
		if (name == 'Down'):glColor3ub(255,255,255)

		# glColorPointer(3, GL_UNSIGNED_BYTE, 0)

	def on_draw(self):
		self.clear()
		glPushMatrix()
		glRotatef(self.xRotation, 1, 0, 0)
		glRotatef(self.yRotation, 0, 1, 0)

		glPointSize(5);

		glBegin(GL_QUADS)

		for block in self.cube_3d:
			# glVertex3f(block['x'] * 50, block['y'] * 50, block['z'] * 50)
			if (block['x'] == 1):
				for face in block['faces']:
					if (face['x'] == 1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
			if (block['x'] == -1):
				for face in block['faces']:
					if (face['x'] == -1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
			if (block['y'] == 1):
				for face in block['faces']:
					if (face['y'] == 1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
			if (block['y'] == -1):
				for face in block['faces']:
					if (face['y'] == -1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
			if (block['z'] == 1):
				for face in block['faces']:
					if (face['z'] == 1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) + 20)
			if (block['z'] == -1):
				for face in block['faces']:
					if (face['z'] == -1):
						self.color_by_name(face['name'])
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) + 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) + 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
						glVertex3f((block['x'] * 50) - 20, (block['y'] * 50) - 20, (block['z'] * 50) - 20)
		glEnd()

		glPopMatrix()


	def on_resize(self, width, height):
		# set the Viewport
		glViewport(0, 0, width, height)

		# using Projection mode
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		aspectRatio = width / height
		gluPerspective(35, aspectRatio, 1, 1000)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef(0, 0, -400)

	def on_text_motion(self, motion):
		if motion == key.UP:
			self.xRotation -= self.increment
		elif motion == key.DOWN:
			self.xRotation += self.increment
		elif motion == key.LEFT:
			self.yRotation -= self.increment
		elif motion == key.RIGHT:
			self.yRotation += self.increment