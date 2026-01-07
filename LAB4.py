
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ORTHO_LEFT, ORTHO_RIGHT = 0, 1000
ORTHO_TOP, ORTHO_BOTTOM = 800, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Rectangle in OpenGL")

# Initialize Orthographic projection
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ORTHO_LEFT, ORTHO_RIGHT, ORTHO_BOTTOM, ORTHO_TOP)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Map value from one range to another
def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)

# Function to plot rectangles
def plot_rect(points):
    if len(points) < 4:
        return  # Not enough points to form a rectangle

    glColor4f(0, 1, 0, 1)  # Green color for filled quads
    glBegin(GL_QUADS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    glColor4f(1, 0, 0, 1)  # Red color for rectangle outline
    for i in range(0, len(points) - 3, 4):
        glBegin(GL_LINE_LOOP)
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(points[i + 1][0], points[i + 1][1])
        glVertex2f(points[i + 2][0], points[i + 2][1])
        glVertex2f(points[i + 3][0], points[i + 3][1])
        glEnd()

# Main Loop
def main():
    done = False
    points = []
    glLineWidth(3)
    
    init_ortho()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                mapped_x = map_value(0, SCREEN_WIDTH, ORTHO_LEFT, ORTHO_RIGHT, p[0])
                mapped_y = map_value(0, SCREEN_HEIGHT, ORTHO_TOP, ORTHO_BOTTOM, p[1])
                points.append((mapped_x, mapped_y))

        # Render
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        plot_rect(points)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
