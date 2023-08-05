import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player bike dimensions
BIKE_WIDTH, BIKE_HEIGHT = 50, 100

# Obstacle dimensions
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bike Game")

# Clock to control the game speed
clock = pygame.time.Clock()

def draw_bike(x, y):
    pygame.draw.rect(window, RED, (x, y, BIKE_WIDTH, BIKE_HEIGHT))

def draw_obstacle(x, y):
    pygame.draw.rect(window, BLACK, (x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def game():
    bike_x = WIDTH // 2
    bike_y = HEIGHT - BIKE_HEIGHT - 10

    obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    obstacle_y = -OBSTACLE_HEIGHT

    speed = 5
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bike_x > 0:
            bike_x -= speed
        if keys[pygame.K_RIGHT] and bike_x < WIDTH - BIKE_WIDTH:
            bike_x += speed

        window.fill(WHITE)

        draw_bike(bike_x, bike_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Move the obstacle
        obstacle_y += speed

        # Check for collision
        if (obstacle_y + OBSTACLE_HEIGHT >= bike_y and obstacle_y <= bike_y + BIKE_HEIGHT) and (
            obstacle_x + OBSTACLE_WIDTH >= bike_x and obstacle_x <= bike_x + BIKE_WIDTH
        ):
            running = False

        # Generate new obstacle if it goes off the screen
        if obstacle_y >= HEIGHT:
            score += 1
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
            obstacle_y = -OBSTACLE_HEIGHT

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    print(f"Game Over! Your score: {score}")

if __name__ == "__main__":
    game()