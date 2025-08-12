import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Click the Box")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
RED = (255, 80, 80)
BG = (30, 30, 30)

box_size = random.randint(10,30)
box_x = random.randint(0, 400 - box_size)
box_y = random.randint(0, 400 - box_size)
box = pygame.Rect(box_x, box_y, box_size, box_size)

score = 0

game_time = 10_000 
start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(BG)

    time_passed = pygame.time.get_ticks() - start_time
    time_left = max(0, game_time - time_passed)
    seconds = time_left // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if box.collidepoint(mouse_x, mouse_y):
                score += 1
                box.x = random.randint(0, 400 - box_size)
                box.y = random.randint(0, 400 - box_size)

    pygame.draw.rect(screen, RED, box)

    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {seconds}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (400 - 130, 10))

    pygame.display.update()
    clock.tick(60)

    if time_left == 0:
        running = False


screen.fill(BG)
final_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(final_text, (400 // 2 - 100, 400 // 2 - 20))
pygame.display.update()
pygame.time.delay(3000)
pygame.quit()

