import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))


while not done:
    for event in pygame.event.get():
        if evet.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
    