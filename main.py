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
	Circle8v(xc, yc, 15, 0/255, 0/255, 0/255, 1)
	for k in range(1,15):
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

def mapa():
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

def personajeRojo(xc, yc):
	#cabeza
	set_pixel( xc,yc+20,255/255, 179/255, 133/255, 10)
	DDA(xc-5, yc+24, xc+5, yc+24, 255/255, 0/255, 0/255, 2)
	set_pixel( xc-3,yc+22, 0/255, 0/255, 0/255, 2)
	set_pixel( xc+2,yc+22, 0/255, 0/255, 0/255, 2)
	DDA(xc-2, yc+17, xc+1, yc+17, 0/255, 0/255, 0/255, 2)
	#manos
	DDA(xc-10, yc+12, xc-12, yc-3, 255/255, 179/255, 133/255, 5)
	DDA(xc+10, yc+12, xc+12, yc-3, 255/255, 179/255, 133/255, 5)
	#tronco
	DDA(xc, yc+7, xc, yc-17, 255/255, 0/255, 0/255, 15)
	DDA(xc, yc-5, xc, yc-25, 0/255, 0/255, 0/255, 1)
	glFlush()

def personajeVerde(xc, yc):
	#cabeza
	set_pixel( xc,yc+20,255/255, 179/255, 133/255, 10)
	DDA(xc-5, yc+24, xc+5, yc+24, 0/255, 110/255, 10/255, 2)
	set_pixel( xc-3,yc+22, 0/255, 0/255, 0/255, 2)
	set_pixel( xc+2,yc+22, 0/255, 0/255, 0/255, 2)
	DDA(xc-2, yc+17, xc+1, yc+17, 0/255, 0/255, 0/255, 2)
	#manos
	DDA(xc-10, yc+12, xc-12, yc-3, 255/255, 179/255, 133/255, 5)
	DDA(xc+10, yc+12, xc+12, yc-3, 255/255, 179/255, 133/255, 5)
	#tronco
	DDA(xc, yc+7, xc, yc-17, 0/255, 110/255, 10/255, 15)
	DDA(xc, yc-5, xc, yc-25, 0/255, 0/255, 0/255, 1)
	glFlush()

def main():

	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)


	mapa()
	xr=-450
	yr=250
	personajeRojo(xr,yr)
	xv=450
	yv=-250
	personajeVerde(xv,yv)


	print("Finish...")
	glFlush()
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					print("K_LEFT")
					sx = -50
					sy = 0
					xv, yv = MoveDefender(xv, yv, sx, sy)
					if(xv-sx == xr and yv == yr):
						personajeRojo(xr,yr)
					personajeVerde(xv,yv)
				elif event.key == pygame.K_RIGHT:
					print("K_RIGHT")
					sx = 50
					sy = 0
					xv, yv = MoveDefender(xv, yv, sx, sy)
					if(xv-sx == xr and yv == yr):
						personajeRojo(xr,yr)
					personajeVerde(xv,yv)
				elif event.key == pygame.K_UP :
					print("K_UP")
					sx = 0
					sy = 50
					xv, yv = MoveDefender(xv, yv, sx, sy)
					if(xv == xr and yv - sy== yr):
						personajeRojo(xr,yr)
					personajeVerde(xv,yv)
				elif event.key == pygame.K_DOWN :
					print("K_DOWN")
					sx = 0
					sy = -50
					xv, yv = MoveDefender(xv, yv, sx, sy)
					if(xv == xr and yv - sy== yr):
						personajeRojo(xr,yr)
					personajeVerde(xv,yv)
				elif event.key == pygame.K_a :
					print("K_a")
					sx = -50
					sy = 0
					xr, yr = MoveDefender(xr, yr, sx, sy)
					if(xv == xr-sx and yv == yr):
						personajeVerde(xv,yv)
					personajeRojo(xr,yr)
				elif event.key == pygame.K_d:
					print("K_d")
					sx = 50
					sy = 0
					xr, yr = MoveDefender(xr, yr, sx, sy)
					if(xv == xr-sx and yv == yr):
						personajeVerde(xv,yv)
					personajeRojo(xr,yr)
				elif event.key == pygame.K_w :
					print("K_w")
					sx = 0
					sy = 50
					xr, yr = MoveDefender(xr, yr, sx, sy)
					if(xv == xr and yv == yr-sy):
						personajeVerde(xv,yv)
					personajeRojo(xr,yr)
				elif event.key == pygame.K_s :
					print("K_s")
					sx = 0
					sy = -50
					xr, yr = MoveDefender(xr, yr, sx, sy)
					if(xv == xr and yv == yr-sy):
						personajeVerde(xv,yv)
					personajeRojo(xr,yr)
				elif event.key == pygame.K_m :
					print("K_m")
					bomba(xv,yv)
					glFlush()

			
#cambio123456

if __name__ == '__main__':
	main()
