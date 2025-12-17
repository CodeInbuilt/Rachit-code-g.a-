import pygame
from pygame.locals import*
from OpenGL.OpenGL import*
from OpenGL.GLU import*

x1=int(input("Enter x1:"))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
x3=int(input("Enter x3: "))
y3=int(input("Enter y3: "))
x4=int(input("Enter x4: "))
y4=int(input("Enter y4: "))

pygame int()

screen_width = 1000
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Drawing rectangle with user input")

def init_ortho():
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0, screen_width, 0, screen_height)
# Function to draw primitives
def draw_primitives():
glPointSize(5)
glBegin(GL_QUADS)
glColor3f(1.0, 1.0, 0.0) # Yellow
glVertex2i(x1, y1)
glVertex2i(x2, y2)
glVertex2i(x3, y3)
glVertex2i(x4, y4)
glEnd()
done = False
init_ortho()
while not done:
for event in pygame.event.get():
if event.type == pygame.QUIT:
done = True
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_MODELVIEW)
glPointSize(5)
draw_primitives()
pygame.display.flip()
pygame.time.wait(100)
pygame.quit()



