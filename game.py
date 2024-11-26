import pygame

pygame.init()

icon = pygame.image.load('pong.png')

pygame.display.set_caption('Pong Game')
pygame.display.set_icon(icon)

size = width, height = 900, 600
screen = pygame.display.set_mode(size)

# Colours
black = [0, 0, 0]
white = [255, 255, 255]
blue  = [57, 203, 255]

# Score card
font = pygame.font.Font('freesansbold.ttf', 32)
scoreA = 0
scoreB = 0

# Paddle dimensions
paddle_width = 5
paddle_height = 50

# Paddle speed
v = 5

# Starting position for Paddle A
padA_x = 800
padA_y = 250

# Starting position for Paddle B
padB_x = 100
padB_y = 250

# Ball properties
radius = 10
speed = [2, 2]
ball_pos = [450, 300]

# Line properties
line_width = 2
line_height = 50
line_x = 450
line_segment = [y for y in range(0, height, line_height + 20)]

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    if ball_pos[0] - radius < 0:  # Ball hits the left side
        scoreB += 1
        ball_pos = [450, 300]
        speed = [2, 2]

    if ball_pos[0] + radius > width:  # Ball hits the right side
        scoreA += 1
        ball_pos = [450, 300]
        speed = [-2, 2]

    if ball_pos[1] - radius < 0 or ball_pos[1] + radius > height:
        speed[1] = -speed[1]

    # Paddle collision
    if padA_x - radius < ball_pos[0] < padA_x + paddle_width and padA_y < ball_pos[1] < padA_y + paddle_height:
        speed[0] = -speed[0]
    if padB_x - radius < ball_pos[0] < padB_x + paddle_width and padB_y < ball_pos[1] < padB_y + paddle_height:
        speed[0] = -speed[0]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and padA_y > 0:
        padA_y -= v
    if keys[pygame.K_DOWN] and padA_y < height - paddle_height:
        padA_y += v

    if keys[pygame.K_w] and padB_y > 0:
        padB_y -= v
    if keys[pygame.K_s] and padB_y < height - paddle_height:
        padB_y += v

    screen.fill(black)

    # Draw paddles
    pygame.draw.rect(screen, white, (padA_x, padA_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (padB_x, padB_y, paddle_width, paddle_height))
    # Draw ball
    pygame.draw.circle(screen, white, ball_pos, radius)

    # Draw the line in the middle
    for segment_y in line_segment:
        pygame.draw.rect(screen, white, (line_x, segment_y, line_width, line_height))

    # Draw the scorecard
    scorecardA = font.render(f'Score A: {scoreA}', True, white, black)
    scorecardB = font.render(f'Score B: {scoreB}', True, white, black)
    screen.blit(scorecardA, (50, 50))
    screen.blit(scorecardB, (width - 200, 50))

    pygame.display.update()

pygame.quit()