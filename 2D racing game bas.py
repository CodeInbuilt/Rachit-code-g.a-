# Creating a polished 2D racing game base with scoreboard, UI elements, and a simple AI opponent using Pygame and OpenGL.

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import time

# Initialize Pygame and fonts
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

# Window setup
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluOrtho2D(0, width, 0, height)

# Lap timing
lap_start_time = time.time()
lap_times = []
best_lap = None
lap_count = 0

# Car position
car_x, car_y, car_angle = 400, 100, 0
car_speed = 0
is_boosting = False
is_drifting = False

# AI car
ai_x, ai_y, ai_angle = 400, 80, 0
ai_speed = 2
ai_checkpoint_index = 0

# Checkpoints (circular)
checkpoints = [(400, 500), (700, 300), (400, 100), (100, 300)]
checkpoint_radius = 30

# Simple track lines
track_lines = [(100, 300, 700, 300), (700, 300, 400, 500),
               (400, 500, 100, 300), (100, 300, 400, 100),
               (400, 100, 700, 300)]

# Draw text UI
def draw_text(text, x, y):
    surface = font.render(text, True, (255, 255, 255))
    text_data = pygame.image.tostring(surface, "RGBA", True)
    glWindowPos2d(x, height - y)
    glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

# Draw car
def draw_car(x, y, angle, color):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 0, 1)
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(-10, -20)
    glVertex2f(10, -20)
    glVertex2f(10, 20)
    glVertex2f(-10, 20)
    glEnd()
    glPopMatrix()

# Draw checkpoints
def draw_checkpoints():
    for cx, cy in checkpoints:
        glColor3f(0, 0, 1)
        glBegin(GL_POLYGON)
        for i in range(20):
            theta = 2 * math.pi * i / 20
            glVertex2f(cx + checkpoint_radius * math.cos(theta),
                       cy + checkpoint_radius * math.sin(theta))
        glEnd()

# Move AI car toward next checkpoint
def update_ai():
    global ai_x, ai_y, ai_angle, ai_checkpoint_index
    cx, cy = checkpoints[ai_checkpoint_index]
    dx, dy = cx - ai_x, cy - ai_y
    target_angle = math.degrees(math.atan2(dy, dx))
    angle_diff = (target_angle - ai_angle + 360) % 360
    if angle_diff > 180:
        angle_diff -= 360
    ai_angle += max(-5, min(5, angle_diff))
    ai_angle %= 360
    rad = math.radians(ai_angle)
    ai_x += ai_speed * math.cos(rad)
    ai_y += ai_speed * math.sin(rad)
    if math.hypot(ai_x - cx, ai_y - cy) < checkpoint_radius:
        ai_checkpoint_index = (ai_checkpoint_index + 1) % len(checkpoints)

# Main loop
clock = pygame.time.Clock()
running = True
checkpoint_index = 0
while running:
    glClear(GL_COLOR_BUFFER_BIT)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        car_angle += 5
    if keys[K_RIGHT]:
        car_angle -= 5
    if keys[K_UP]:
        car_speed += 0.2
    else:
        car_speed *= 0.98

    rad = math.radians(car_angle)
    car_x += car_speed * math.cos(rad)
    car_y += car_speed * math.sin(rad)

    # Check checkpoint
    cx, cy = checkpoints[checkpoint_index]
    if math.hypot(car_x - cx, car_y - cy) < checkpoint_radius:
        checkpoint_index = (checkpoint_index + 1) % len(checkpoints)
        if checkpoint_index == 0:
            lap_time = time.time() - lap_start_time
            lap_start_time = time.time()
            lap_times.append(lap_time)
            lap_count += 1
            best_lap = min(lap_times) if best_lap is None else min(best_lap, lap_time)

    # Draw track
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_LINES)
    for x1, y1, x2, y2 in track_lines:
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

    draw_checkpoints()
    draw_car(car_x, car_y, car_angle, (1, 0, 0))  # player
    update_ai()
    draw_car(ai_x, ai_y, ai_angle, (0, 1, 0))  # AI

    # UI
    draw_text(f"Lap: {lap_count}", 10, 20)
    if lap_times:
        draw_text(f"Last: {lap_times[-1]:.2f}s", 10, 50)
    if best_lap:
        draw_text(f"Best: {best_lap:.2f}s", 10, 80)
    draw_text(f"Speed: {car_speed:.1f}", 10, 110)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
