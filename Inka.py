# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# Python 3.8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import random
import numpy as np
### Algorithm ###
def set_pixel(x, y, r, g, b, size):
    glColor3f(r, g, b)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
    pygame.display.flip()

def color_pixel(width, height, x, y, size):
    rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size,GL_RGB,GL_UNSIGNED_BYTE, None)
    return list(rgb)
def DDA(x0, y0, x1, y1, r, g, b, size):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    if abs(dx) > abs(dy):
        steps = abs(dx)
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
        steps = abs(dy)
        xi = dx / steps
        yi = dy / steps
        set_pixel(round(x), round(y), r, g, b, size)
        points.append((round(x), round(y)))
        for k in range(steps):
            x += xi
            y += yi
            set_pixel(round(x), round(y), r, g, b, size)
            points.append((round(x), round(y)))
            
def DrawPolygon(vertices, r, g, b, size):
    vertices.append(vertices[0])
    for k in range(len(vertices) - 1):
        x0, y0,z0 = vertices[k]
        x1, y1,z0 = vertices[k + 1]
        DDA(x0, y0, x1, y1, r, g, b, size)
        
def SimpleSeedFill(width, height, size, vertices, xi, yi, r, g, b):
    r, g, b = 255 * r, 255 * g, 255 * b
    stack = []
    stack.append((xi, yi))
    while len(stack) > 0:
        x, y = stack.pop()
        if color_pixel(width, height, x, y, size) != [r, g,b]:
            set_pixel(x, y, r, g, b, size)
        if color_pixel(width, height, x + 1, y, size) != [r,g, b]:
            stack.append((x + 1, y))
        if color_pixel(width, height, x, y + 1, size) != [r,g, b]:
            stack.append((x, y + 1))
        if color_pixel(width, height, x - 1, y, size) != [r,g, b]:
            stack.append((x - 1, y))
        if color_pixel(width, height, x, y - 1, size) != [r,g, b]:
            stack.append((x, y - 1))
            
def Traslacion(vertices,tx,ty):
    T=[[1,0,tx],[0,1,ty],[0,0,1]]
    result=[]
    for i in range (len(vertices)-1):
        point=np.dot(T,vertices[i])
        result.append(point)
    return result

def display_openGL(width, height, scale):
    pygame.display.set_mode((width, height), pygame.OPENGL)
    #da el color al canvas
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height/ 2) 

scale = 1
width, height = scale * 500, scale * 500
pygame.init()
pygame.display.set_caption('C.G. I')
display_openGL(width, height, scale)
	
x = 0
y = 0
set_pixel(x, y, 1, 1, 1, scale)

vertices =[(10,-30,1),(10,0,1),(13,-10,1),(15,-10,1),(15,5,1),(10,5,1),(10,15,1),
           (15,15,1),(15,20,1),(20,20,1),(20,30,1),(15,30,1),(15,35,1),
           (10,35,1),(0,40,1),(-10,35,1),(-15,35,1),(-15,30,1),
           (-20,30,1),(-20,20,1),(-15,20,1),(-15,15,1),(-10,15,1),(-10,5,1),
           (-15,5,1),(-15,-10,1),(-13,-10,1),
           (-10,0,1),(-10,-30,1),(-2,-30,1),(-2,-15,1),
           (2,-15,1),(2,-30,1)
           ]
DrawPolygon(vertices, 250/250, 0/250, 0/250, scale)

V2=[(-8,15,1),(-8,18,1),(-2,18,1),(-2,15,1)]
DrawPolygon(V2, 250/250, 0/250, 0/250, scale)

V3=[(2,15,1),(2,18,1),(8,18,1),(8,15,1)]
DrawPolygon(V3, 250/250, 0/250, 0/250, scale)

V4=[(-4,7,1),(-4,10,1),(4,10,1),(4,7,1)]
DrawPolygon(V4, 250/250, 0/250, 0/250, scale)

xi = 15
yi = 25
SimpleSeedFill(width, height, scale, vertices, xi, yi, 255/255, 0/255, 0/255)

DrawPolygon(Traslacion(vertices,50,0), 0/250, 0/250, 250/250, scale)
SimpleSeedFill(width, height, scale, vertices, 51, 1, 0/255, 0/255, 255/255)

DrawPolygon(Traslacion(vertices,100,0), 0/250, 0/250, 250/250, scale)
SimpleSeedFill(width, height, scale, vertices, 100, 1, 0/255, 0/255, 255/255)

DrawPolygon(Traslacion(vertices,-50,0), 0/250, 0/250, 250/250, scale)
SimpleSeedFill(width, height, scale, vertices, -49, 1, 0/255, 0/255, 255/255)

DrawPolygon(Traslacion(vertices,-100,0), 0/250, 0/250, 250/250, scale)
SimpleSeedFill(width, height, scale, vertices, -99, 1, 0/255, 0/255, 255/255)

glFlush()
pygame.display.flip()
	 
