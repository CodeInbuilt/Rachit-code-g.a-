# advanced_snake_full.py
# Single-player Advanced Snake Game with:
# Skins, Animations, Moving Obstacles, Levels/Maps, High Score, Start Menu, Restart
# No sound included.

import pygame
import random
import sys
import os

pygame.init()

# -------------------------
# Configuration
# -------------------------
WIDTH, HEIGHT = 640, 480
CELL = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake - Single Player")
CLOCK = pygame.time.Clock()

HS_FILE = "highscore.txt"
if not os.path.exists(HS_FILE):
    with open(HS_FILE, "w") as f:
        f.write("0")

with open(HS_FILE, "r") as f:
    try:
        HIGH_SCORE = int(f.read().strip())
    except:
        HIGH_SCORE = 0

# Colors and skins
SKINS = {
    "green": (34, 177, 76),
    "yellow": (255, 242, 0),
    "purple": (163, 73, 164),
    "white": (255, 255, 255),
    "orange": (255, 127, 39)
}
DEFAULT_SKIN = "green"

# Palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_GRAY = (50, 50, 50)
FOOD_COLOR = (200, 30, 30)
OBSTACLE_COLOR = (0, 162, 232)
WALL_COLOR = (120, 120, 120)
TEXT_COLOR = (240, 240, 240)
HIGHLIGHT = (0, 200, 70)

# Game maps: list of wall cell coordinates (multiples of CELL)
MAPS = {
    "easy": [],
    "medium": [
        # horizontal barrier in middle
        *[[x * CELL, HEIGHT//2] for x in range(5, (WIDTH//CELL)-5)]
    ],
    "hard": [
        # two crossing walls + a block cluster
        *[[WIDTH//4 + x * CELL, HEIGHT//4] for x in range(0, 10)],
        *[[WIDTH//4 + x * CELL, HEIGHT//4 + 6 * CELL] for x in range(0, 10)],
        *[[WIDTH//2, HEIGHT//6 + y * CELL] for y in range(0, 12)],
        *[[WIDTH//2 + 8*CELL + x*CELL, HEIGHT//3 + 4*CELL + y*CELL] for x in range(0,4) for y in range(0,4)]
    ]
}

# -------------------------
# Utility functions
# -------------------------
def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(SCREEN, GRID_GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(SCREEN, GRID_GRAY, (0, y), (WIDTH, y))

def show_text(text, size, color, x, y, center=False):
    font = pygame.font.SysFont("Arial", size)
    surf = font.render(text, True, color)
    rect = surf.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    SCREEN.blit(surf, rect)

def random_cell():
    return [random.randrange(0, WIDTH//CELL) * CELL,
            random.randrange(0, HEIGHT//CELL) * CELL]

def clamp_to_cells(pos):
    """Return a position snapped to grid cells."""
    return [ (pos[0]//CELL)*CELL, (pos[1]//CELL)*CELL ]

# -------------------------
# Animated start menu / selection
# -------------------------
def start_menu(current_skin, current_map_key):
    blink = True
    blink_timer = 0
    selected_map = current_map_key
    skin = current_skin

    while True:
        SCREEN.fill(BLACK)
        draw_grid()
        show_text("ADVANCED SNAKE", 56, HIGHLIGHT, WIDTH//2, HEIGHT//6, center=True)
        show_text("Press ENTER to Play", 28, WHITE, WIDTH//2, HEIGHT//2, center=True)
        show_text("Press M to change Map (current: {})".format(selected_map.capitalize()), 20, TEXT_COLOR, WIDTH//2, HEIGHT//2+60, center=True)
        show_text("Press S to change Skin (current: {})".format(skin), 20, TEXT_COLOR, WIDTH//2, HEIGHT//2+92, center=True)
        show_text("Arrow keys to move", 18, TEXT_COLOR, WIDTH//2, HEIGHT//2+130, center=True)
        show_text("Press Q to Quit", 18, TEXT_COLOR, WIDTH//2, HEIGHT//2+156, center=True)
        show_text(f"High Score: {HIGH_SCORE}", 20, WHITE, 10, 10)

        # Animate blinking text
        blink_timer += 1
        if blink_timer % 30 == 0:
            blink = not blink
        if blink:
            show_text("Press ENTER to Play", 28, WHITE, WIDTH//2, HEIGHT//2, center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return skin, selected_map
                if event.key == pygame.K_s:
                    skins = list(SKINS.keys())
                    i = skins.index(skin)
                    skin = skins[(i+1) % len(skins)]
                if event.key == pygame.K_m:
                    maps = list(MAPS.keys())
                    j = maps.index(selected_map)
                    selected_map = maps[(j+1) % len(maps)]
                if event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

        pygame.display.update()
        CLOCK.tick(15)

# -------------------------
# Obstacles (moving)
# Each obstacle: [x, y, vx, vy]
# vx/vy are in multiples of CELL
# -------------------------
def spawn_moving_obstacles(n, forbidden_positions):
    obs = []
    attempts = 0
    while len(obs) < n and attempts < n * 50:
        attempts += 1
        x = random.randrange(0, WIDTH // CELL) * CELL
        y = random.randrange(0, HEIGHT // CELL) * CELL
        if [x, y] in forbidden_positions:
            continue
        # random direction: horizontal or vertical
        if random.random() < 0.5:
            vx = random.choice([-1, 1]) * CELL
            vy = 0
        else:
            vx = 0
            vy = random.choice([-1, 1]) * CELL
        obs.append([x, y, vx, vy])
    return obs

# -------------------------
# Game over screen
# -------------------------
def game_over_screen(score):
    global HIGH_SCORE
    if score > HIGH_SCORE:
        HIGH_SCORE = score
        with open(HS_FILE, "w") as f:
            f.write(str(HIGH_SCORE))

    while True:
        SCREEN.fill(BLACK)
        draw_grid()
        show_text("GAME OVER", 64, (200, 40, 40), WIDTH//2, HEIGHT//4, center=True)
        show_text(f"Score: {score}", 28, WHITE, WIDTH//2, HEIGHT//2, center=True)
        show_text(f"High Score: {HIGH_SCORE}", 24, TEXT_COLOR, WIDTH//2, HEIGHT//2 + 40, center=True)
        show_text("Press ENTER to Restart", 20, WHITE, WIDTH//2, HEIGHT//2 + 90, center=True)
        show_text("Press ESC to Quit", 20, TEXT_COLOR, WIDTH//2, HEIGHT//2 + 120, center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
        pygame.display.update()
        CLOCK.tick(15)

# -------------------------
# Main game
# -------------------------
def main_game(initial_skin, map_key):
    # initial snake
    snake_pos = [CELL * 5, CELL * 5]
    snake_body = [ [CELL * 5 - i*CELL, CELL * 5] for i in range(3) ]
    direction = "RIGHT"
    change_to = direction
    skin_color = SKINS.get(initial_skin, SKINS[DEFAULT_SKIN])

    score = 0
    base_speed = 8  # base ticks per second
    speed = base_speed

    # food
    food_pos = random_cell()
    while food_pos in snake_body:
        food_pos = random_cell()

    # walls / map
    walls = [ [x, y] for x, y in MAPS.get(map_key, []) ]
    # Make sure walls are unique and within grid
    walls = [clamp_to_cells(w) for w in walls]

    # obstacles spawn avoiding snake spawn and initial food and walls
    forbidden = set(tuple(p) for p in snake_body + [food_pos] + walls)
    obstacles = spawn_moving_obstacles(n=6 if map_key=="easy" else 9 if map_key=="medium" else 14,
                                       forbidden_positions=[list(x) for x in forbidden])

    # animation for food (pulsing)
    food_pulse = 0
    food_pulse_dir = 1

    # for smoother movement visual we will draw rectangles; movement is cell-by-cell
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"
                # quick-skin switch during game
                elif event.key == pygame.K_s:
                    skins = list(SKINS.keys())
                    idx = skins.index(initial_skin) if initial_skin in skins else 0
                    initial_skin = skins[(idx + 1) % len(skins)]
                    skin_color = SKINS[initial_skin]

        direction = change_to

        # move snake head
        if direction == "UP":
            snake_pos[1] -= CELL
        elif direction == "DOWN":
            snake_pos[1] += CELL
        elif direction == "LEFT":
            snake_pos[0] -= CELL
        elif direction == "RIGHT":
            snake_pos[0] += CELL

        # insert new head to body
        snake_body.insert(0, list(snake_pos))

        # check food eaten
        if snake_pos == food_pos:
            score += 1
            # increase speed modestly (not too wild)
            speed = base_speed + score // 2
            # respawn food ensuring not on snake, walls, or obstacles
            forbidden_positions = set(tuple(p) for p in snake_body + walls + [[o[0], o[1]] for o in obstacles])
            new_food = random_cell()
            tries = 0
            while tuple(new_food) in forbidden_positions and tries < 200:
                new_food = random_cell()
                tries += 1
            food_pos = new_food
        else:
            # remove tail
            snake_body.pop()

        # update obstacles positions
        for ob in obstacles:
            ob[0] += ob[2]  # x += vx
            ob[1] += ob[3]  # y += vy
            # bounce off borders
            if ob[0] < 0:
                ob[0] = 0
                ob[2] *= -1
            if ob[0] >= WIDTH:
                ob[0] = WIDTH - CELL
                ob[2] *= -1
            if ob[1] < 0:
                ob[1] = 0
                ob[3] *= -1
            if ob[1] >= HEIGHT:
                ob[1] = HEIGHT - CELL
                ob[3] *= -1
            # ensure obstacle stays on grid (snap)
            ob[0] = (ob[0]//CELL)*CELL
            ob[1] = (ob[1]//CELL)*CELL

        # -------------------------
        # Collision checks
        # -------------------------
        # wall collision (map walls)
        if snake_pos in walls:
            game_over_screen(score)
            return

        # boundary collision
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            game_over_screen(score)
            return

        # self collision (head with body excluding head)
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over_screen(score)
                return

        # obstacles collision
        for ob in obstacles:
            if snake_pos[0] == ob[0] and snake_pos[1] == ob[1]:
                game_over_screen(score)
                return

        # -------------------------
        # Drawing
        # -------------------------
        SCREEN.fill(BLACK)
        draw_grid()

        # draw map walls
        for w in walls:
            pygame.draw.rect(SCREEN, WALL_COLOR, pygame.Rect(w[0], w[1], CELL, CELL))

        # draw obstacles (moving)
        for ob in obstacles:
            pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(ob[0], ob[1], CELL, CELL))

        # draw snake with head highlight
        for idx, block in enumerate(snake_body):
            rect = pygame.Rect(block[0], block[1], CELL, CELL)
            if idx == 0:
                # head slightly brighter / outlined
                pygame.draw.rect(SCREEN, skin_color, rect)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)  # outline
            else:
                pygame.draw.rect(SCREEN, skin_color, rect)

        # food pulsing animation
        # compute small size variation
        food_pulse += food_pulse_dir
        if food_pulse > 6 or food_pulse < -6:
            food_pulse_dir *= -1
        extra = food_pulse // 2  # small integer offset
        fp_rect = pygame.Rect(food_pos[0]+extra, food_pos[1]+extra, CELL-2*extra, CELL-2*extra)
        pygame.draw.rect(SCREEN, FOOD_COLOR, fp_rect)

        # HUD
        show_text(f"Score: {score}", 20, TEXT_COLOR, 10, 10)
        show_text(f"High Score: {HIGH_SCORE}", 18, TEXT_COLOR, 10, 36)
        show_text(f"Map: {map_key.capitalize()}", 18, TEXT_COLOR, WIDTH-140, 10)
        show_text(f"Skin: {initial_skin}", 18, TEXT_COLOR, WIDTH-140, 34)

        pygame.display.update()
        CLOCK.tick(speed)

# -------------------------
# Entry point
# -------------------------
def main():
    skin, map_key = start_menu(DEFAULT_SKIN, "easy")
    while True:
        main_game(skin, map_key)
        # after game over, show game over screen and then return to menu
        skin, map_key = start_menu(skin, map_key)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        print("An error occurred:", e)
        sys.exit()
