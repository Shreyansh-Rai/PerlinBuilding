
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import perlinnoise

ns = perlinnoise.perlin2d(40,120)
class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = 'white_cube',
			color = color.white,
			highlight_color = color.lime)
	
	def input(self, key):
		if self.hovered :
			if key == "left mouse down" :
				voxel = Voxel(
					position=(self.position + mouse.normal)
				)
			
			if key == "right mouse down" :
				destroy(self)
	

def gen():
	l= perlinnoise.perlin2d(40,120)
	l2=perlinnoise.perlin2d(40,120)
	l3 =perlinnoise.perlin2d(40,120)
	for i in range(40) :
		for j in range(40):
			# x = floor(i/40)
			# z = floor(i%40)
			x=i
			z=j
			y = floor((l[x][z]+l2[z][x]+l3[z][x])*7)
			voxel = Voxel(position=(x,y,z))
			voxel = Voxel(position=(x,y-1,z))



app = Ursina()
player = FirstPersonController()
player.y=20

window.color = color.azure


gen()

def update() :
	if held_keys['g'] :
		player.jump_height = 10
		player.gravity = -0.4
	if not held_keys['g'] :
		player.gravity = 1
		player.jump_height = 2
app.run()