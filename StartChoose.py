#inicio del juego
#personaje
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import random as rdn
import numpy as np

#algoritmo para traslacion
def reflexion(vertices,x,y):
    
    r=[[1,-1*(-y),0],[0,-1*(-x),0],[0,0,1]]
    result=[]
    for j in range(len(vertices)-1):
        point=np.dot(r,vertices[j])
        result.append(point)
    return result
    
def deformacion(vertices,shx,shy):
    D=[[1,shx,0],[0,1,0],[shy,0,1]]
    result=[]
    for i in range(len(vertices)-1):
        point=np.dot(D,vertices[i])
        result.append(point)
    return result
    
    
def escalamiento(vertices,sx,sy):
    E=[[sx,0,0],[0,sy,0],[0,0,1]]
    result=[]
    for i in range(len(vertices)-1):
        point=np.dot(E,vertices[i])
        result.append(point)
    return result
    
def traslate(vertices,tx,ty):
    T=[[1,0,tx],[0,1,ty],[0,0,1]]
    result=[]
    for i in range (len(vertices)):
        point=np.dot(T,vertices[i])
        result.append(point)
    return result

def set_pixel(x, y, r, g, b, size):
    glColor3f(r, g, b)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
    pygame.display.flip()
    #print("{}\t{}".format(x, y))
    #pygame.time.wait(1)

def set_point(x, y, r, g, b, size):
    glColor3f(r, g, b)
    glPointSize(size)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
    pygame.display.flip()
    print("{}\t{}".format(x, y))
    #pygame.time.wait(0)

#circulos



def DDA(x0, y0, x1, y1, r, g, b, size):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    if abs(dx) > abs(dy):
        steps = abs(dx)
        if steps!=0:
            xi = dx / steps
            yi = dy / steps
            set_pixel(round(x), round(y), r, g, b, size)
            points.append((round(x), round(y)))
            for k in range(steps):
                x += xi
                y += yi
                set_pixel(round(x), round(y), r, g, b, size)
                points.append((round(x), round(y)))
        else:
            xi = 0
            yi = 0
            set_pixel(round(x), round(y), r, g, b, size)
            points.append((round(x), round(y)))
            for k in range(steps):
                x += xi
                y += yi
                set_pixel(round(x), round(y), r, g, b, size)
                points.append((round(x), round(y)))
    else:
        steps = abs(dy)

        if steps!=0:
            xi = dx / steps
            yi = dy / steps
            set_pixel(round(x), round(y), r, g, b, size)
            points.append((round(x), round(y)))
            for k in range(steps):
                x += xi
                y += yi
                set_pixel(round(x), round(y), r, g, b, size)
                points.append((round(x), round(y)))
        else:
            xi = 0
            yi = 0
            set_pixel(round(x), round(y), r, g, b, size)
            points.append((round(x), round(y)))
            for k in range(steps):
                x += xi
                y += yi
                set_pixel(round(x), round(y), r, g, b, size)
                points.append((round(x), round(y)))

def DrawPolygon(vertices, r, g, b, size):
    # vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
    vertices.append(vertices[0])
    for k in range(len(vertices) - 1):
        x0, y0,z0 = vertices[k]
        x1, y1,z1 = vertices[k + 1]
        DDA(x0, y0, x1, y1, r, g, b, size)

def display_openGL(width, height, scale):
    pygame.display.set_mode((width, height), pygame.OPENGL)
    glClearColor(0.0, 0.0, 0.0, scale)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # glScalef(scale, scale, 0)
    #gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height/ 2)  #aqui define un espacio 2D para las cordenadas
    gluOrtho2D(-50, 50, -50, 50)

def color_pixel(width, height, x, y, size):
    rgb = glReadPixels( width/2+x,height/2+y , size ,size,GL_RGB,GL_UNSIGNED_BYTE, None)
    print(list(rgb))
    return list(rgb)

def L_G(x,y,size):
    G=[[0,1,1,1,0,0],
       [1,0,0,0,0,0],
       [1,0,1,1,0,0],
       [1,0,0,1,0,0],
       [1,0,0,1,0,0],
       [0,1,1,0,0,0]]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
        
def L_R(x,y,size):
    R=[[0,1,1,1,0,0],
       [1,0,0,0,1,0],
       [1,1,1,1,0,0],
       [1,0,1,0,0,0],
       [1,0,0,1,0,0],
       [0,0,0,0,1,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_A(x,y,size):
    R=[[0,1,1,0,0,0],
       [1,0,0,1,0,0],
       [1,0,0,1,0,0],
       [1,1,1,1,0,0],
       [1,0,0,1,0,0],
       [0,0,0,1,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_M(x,y,size):
    R=[[0,1,0,1,0,0],
       [1,0,1,0,1,0],
       [1,0,1,0,1,0],
       [1,0,1,0,1,0],
       [1,0,0,0,1,0],
       [0,0,0,0,1,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_E(x,y,size):
    R=[[0,1,1,1,0,0],
       [1,0,0,0,0,0],
       [1,1,1,1,0,0],
       [1,0,0,0,0,0],
       [1,1,1,1,0,0],
       [0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_S(x,y,size):
    R=[[0,1,1,1,0,0],
       [1,0,0,0,0,0],
       [0,1,1,0,0,0],
       [0,0,0,1,0,0],
       [1,1,1,0,0,0],
       [0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_T(x,y,size):
    R=[[1,1,1,1,1,0],
       [0,0,1,0,0,0],
       [0,0,1,0,0,0],
       [0,0,1,0,0,0],
       [0,0,1,0,0,0],
       [0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_X(x,y,size):
    R=[[1,1,0,0,1,1],
       [0,1,0,0,1,0],
       [0,0,1,1,0,0],
       [0,0,1,1,0,0],
       [1,1,0,0,1,1],
       [0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def L_I(x,y,size):
    R=[[0,1,1,1,1,0],
       [1,0,1,0,0,0],
       [0,0,1,0,0,0],
       [0,0,1,0,0,0],
       [0,1,1,1,1,0],
       [0,0,0,0,0,0]]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]==1: 
                set_pixel(x+j,y-i, 85, 85, 85, size)
def Presentacion():
    width=-40
    height=30

    L_S(width,height,5)
    L_T(width+5,height,5)
    L_A(width+15,height,5)
    L_R(width+25,height,5)
    L_T(width+35,height,5)
    
    L_G(-width-30,height,5)
    L_A(-width-20,height,5)
    L_M(-width-10,height,5)
    L_E(-width,height,5)

    salida()
def salida():
    b1=0
    b2=-40
    L_E(b1-10,b2,5)
    L_X(b1-5,b2,5)
    L_I(b1,b2,5)
    L_T(b1+5,b2,5)

def puntero(x,y):
    P=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,2,2,0,0,0,0],
       [0,0,2,0,2,0,2,0,0],
       [0,0,2,2,2,0,2,0,0],
       [0,0,2,0,0,0,2,0,0],
       [0,0,2,0,0,0,0,0,0],
       [0,3,0,0,0,0,0,3,0],
       [0,0,3,3,3,3,3,0,0]]
    size=5
    for i in range(len(P)):
        for j in range(len(P)):
            if P[i][j]==2:
                set_pixel(x+j,y-i, 85, 85, 85, size)
            if P[i][j]==3:
                set_pixel(x+j,y-i, 255, 233, 0, size)
def marco(vertices):
    size=5
    r,g,b=1, 0.7, 1
    DrawPolygon(vertices, r, g, b, size)
        
def personajeVerde(xc, yc):
	#cabeza
	set_pixel( xc,yc+8,255/255, 179/255, 133/255, 10)
	DDA(xc-2, yc+9, xc+2, yc+9, 0/255, 110/255, 10/255, 2)
	set_pixel( xc-3,yc+22, 0/255, 0/255, 0/255, 2)
	set_pixel( xc+2,yc+22, 0/255, 0/255, 0/255, 2)
	DDA(xc-1, yc+8, xc+1, yc+8, 0/255, 0/255, 0/255, 2)
	#manos
	DDA(xc-5, yc+6, xc-6, yc-1, 255/255, 179/255, 133/255, 5)
	DDA(xc+5, yc+6, xc+6, yc-1, 255/255, 179/255, 133/255, 5)
	#tronco
	DDA(xc, yc+2, xc, yc-8, 0/255, 110/255, 10/255, 15)
	DDA(xc, yc-1, xc, yc-10, 0/255, 0/255, 0/255, 1)
	glFlush()
def personajeRojo(xc, yc):
	#cabeza
	set_pixel( xc,yc+8,255/255, 179/255, 133/255, 10)
	DDA(xc-2, yc+9, xc+2, yc+9, 255/255, 0/255, 0/255, 2)
	set_pixel( xc-3,yc+22, 0/255, 0/255, 0/255, 2)
	set_pixel( xc+2,yc+22, 0/255, 0/255, 0/255, 2)
	DDA(xc-1, yc+8, xc+1, yc+8, 0/255, 0/255, 0/255, 2)
	#manos
	DDA(xc-5, yc+6, xc-6, yc-1, 255/255, 179/255, 133/255, 5)
	DDA(xc+5, yc+6, xc+6, yc-1, 255/255, 179/255, 133/255, 5)
	#tronco
	DDA(xc, yc+2, xc, yc-8, 255/255, 0/255, 0/255, 15)
	DDA(xc, yc-1, xc, yc-10, 0/255, 0/255, 0/255, 1)
	glFlush()

'''         
    size=5
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==1:
                set_pixel(x-j,y-i, 1, 0.7, 1, size)
            if matriz[i][j]==2:
                set_pixel(x-j,y-i, 0, 0, 255, size)
            if matriz[i][j]==3:
                set_pixel(x-j,y-i, 128, 0, 0, size)
            if matriz[i][j]==4:
                set_pixel(x-j,y-i, 1, 1, 1, size)
            if matriz[i][j]==5:
                set_pixel(x-j,y-i, 0, 0, 254, size)
            if matriz[i][j]==6:
                set_pixel(x-j,y-i, 255, 233, 0, size)
            if matriz[i][j]==7:
                set_pixel(x-j,y-i, 255,0.5,0.5, size)'''

def clearCanvas():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
def Choose(sx,sy):
    vertices=[[-10,-20,1],[10,-20,1],[10,20,1],[-10,20,1]]
    marco(vertices)
    v=traslate(vertices,sx,sy)
    clearCanvas()
    marco(v)
    puntero(sx,sy-21)
def moveImage(x,y,sx,sy,size):
    clearCanvas()
    vertices=traslate([[x,y,1]],sx,sy)
    x=vertices[0][0]
    y=vertices[0][1]
    marco()
    pygame.display.flip()
    return x,y
            
def main():
    scale = 1
    width, height = scale * 400, scale * 400

    pygame.init()
    pygame.display.set_caption('C.G. I')

    display_openGL(width, height, scale)
    
    x,y=0,0
    
    print("Finish...")
    glFlush()
    pygame.display.flip()

    marcador=-1

    while True:
        Presentacion()
        personajeVerde(-20, 0)
        personajeRojo(20, 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    
                    print("k_a")
                elif event.key==pygame.K_LEFT:
                    sx=-20
                    sy=0
                    Choose(sx,sy)
                    marcador=0
                    print("K_Left")
            
                elif event.key==pygame.K_RIGHT:
                    sx=20
                    sy=0
                    Choose(sx,sy)
                    marcador=1
                    print("K_Right")
                elif event.key==pygame.K_DOWN:
                    sx=0
                    sy=-30
                    Choose(sx,sy)
                    marcador=2
                    print("K_Down")
        
                elif event.key==pygame.K_SPACE:
                    if marcador==0:
                        print("select VERDE")
                    elif marcador==1:
                        print("select ROJO")
                    elif marcador==2:
                        print("exit")
                

main()
