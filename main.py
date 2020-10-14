# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *

scale = 1 
""" no cambiar la escala de 1 """
width, height = scale * 1000, scale * 600

def bomba(xc, yc):
	for k in range(1,17):
		Circle8v(xc, yc, k, 100/255, 100/255, 100/255, 1)
	DDA(xc+8, yc+8, xc+14, yc+14, 255/255, 200/255, 0/255, 3)
	set_pixel( xc+14,yc+14,255/255, 0/255, 0/255, 4)
	
	
def explocion(xc, yc):
	posx=xc%100
	posy=yc%100
	if(posx == 50 or posx == -50):
		DDA(xc,250,xc,-250, 255/255, 100/255, 0/255, 40)
	
	if(posy == 50 or posy == -50):
		DDA(-450,yc,450,yc, 255/255, 100/255, 0/255, 40)

	set_pixel( xc,yc,255/255, 0/255, 0/255, 4)

def main():

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)


	#bordes
	x=487.5
	y=287.5

	vertices = [(-x, -y), (-x, y), (x, y), (x, -y)]
	DrawPolygon(vertices, 175/255, 175/255, 175/255, 25)
	x = -400
	for k in range(0,9):
		y = 200
		for l in range(0,5):
			set_pixel(-400+(k*100),200-(l*100),175/255, 175/255, 175/255, 50)
	bomba(-450,250)
	bomba(450,150)
	bomba(-200,50)
	bomba(150,-100)
	explocion(350,150)
	explocion(-200,-50)
	explocion(50,-200)
	print("Finish...")
	glFlush()
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()
