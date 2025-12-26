#import pygame
#from pygame.locals import *
#from OpenGL.GL import *
#from OpenGL.GLU import *
#import math

# Initialize pygame
#pygame.init()

# Set up display
#screen_width = 1000
#screen_height = 900
#screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
#pygame.display.set_caption("OpenGL in Python")

# Initialize orthographic projection
#def init_ortho():
 #   glMatrixMode(GL_PROJECTION)
 #   glLoadIdentity()
 #   gluOrtho2D(0, screen_width, 0, screen_height)
 #   glMatrixMode(GL_MODELVIEW)
 #   glLoadIdentity()

#def draw_circle(center_x, center_y, radius, color):
#    glColor3f(*color)
#    glBegin(GL_TRIANGLE_FAN)
#    glVertex2f(center_x, center_y)  # Center of circle
#    for angle in range(361):
#        x = center_x + math.cos(math.radians(angle)) * radius
#        y = center_y + math.sin(math.radians(angle)) * radius
#        glVertex2f(x, y)
#    glEnd()

#def draw_ellipse(center_x, center_y, radius_x, radius_y, color):
#    glColor3f(*color)
#    glBegin(GL_TRIANGLE_FAN)
#    glVertex2f(center_x, center_y)  # Center of ellipse
#    for angle in range(361):
#        x = center_x + math.cos(math.radians(angle)) * radius_x
#        y = center_y + math.sin(math.radians(angle)) * radius_y
#       glVertex2f(x, y)
#    glEnd()

# Main loop
#done = False
#init_ortho()
#while not done:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            done = True
#
 #   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 #   glLoadIdentity()
    
    # Draw shapes
 #   draw_circle(400, 500, 50, (1, 0, 0))  # Red circle
 #   draw_circle(375, 525, 10, (0, 0, 0))  # Left eye
  #  draw_circle(425, 525, 10, (0, 0, 0))  # Right eye
  #  draw_ellipse(400, 500, 5, 10, (0, 1, 0))  # Small green ellipse
  #  draw_ellipse(400, 475, 20, 5, (0, 1, 0))  # Wide green ellipse
  #  draw_ellipse(400, 350, 200, 75, (1, 0, 1))  # Large purple ellipse
#    draw_ellipse(400, 350, 50, 100, (0, 0, 1))  # Tall blue ellipse
    
 #   pygame.display.flip()
 #   pygame.time.wait(100)

#pygame.quit()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Animated Bouncing OpenGL Character")

# Set up orthographic projection
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)

# Draw a filled circle
def draw_circle(center_x, center_y, radius, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center_x, center_y)
    for angle in range(361):
        x = center_x + math.cos(math.radians(angle)) * radius
        y = center_y + math.sin(math.radians(angle)) * radius
        glVertex2f(x, y)
    glEnd()

# Draw a filled ellipse
def draw_ellipse(center_x, center_y, radius_x, radius_y, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center_x, center_y)
    for angle in range(361):
        x = center_x + math.cos(math.radians(angle)) * radius_x
        y = center_y + math.sin(math.radians(angle)) * radius_y
        glVertex2f(x, y)
    glEnd()

# Generate random color
def random_color():
    return (random.random(), random.random(), random.random())

# Initialize
init_ortho()
face_color = (1, 0, 0)
x, y = screen_width // 2, screen_height // 2
dx, dy = 3, 2  # bounce speed

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            face_color = random_color()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                x -= 20
            elif event.key == K_RIGHT:
                x += 20
            elif event.key == K_UP:
                y += 20
            elif event.key == K_DOWN:
                y -= 20

    # Update position for bouncing
    x += dx
    y += dy
    if x - 50 < 0 or x + 50 > screen_width:
        dx *= -1
    if y - 50 < 0 or y + 150 > screen_height:  # 150 to account for lower ellipses
        dy *= -1

    # Draw scene
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Draw character
    draw_circle(x, y, 50, face_color)              # Face
    draw_circle(x - 25, y + 25, 10, (0, 0, 0))      # Left eye
    draw_circle(x + 25, y + 25, 10, (0, 0, 0))      # Right eye
    draw_ellipse(x, y, 5, 10, (0, 1, 0))            # Nose
    draw_ellipse(x, y - 25, 20, 5, (0, 1, 0))       # Mouth
    draw_ellipse(x, y - 150, 200, 75, (1, 0, 1))    # Base
    draw_ellipse(x, y - 150, 50, 100, (0, 0, 1))    # Body

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
