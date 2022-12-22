import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_pos = 0
    clock = pygame.time.Clock()
    running = True
    v = 10
    s = 0
    screen.fill((0, 0, 255))
    pygame.display.flip()
    print('fw')
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 255))
                x_pos = 0
                pygame.display.flip()
                coord = event.pos
                s += 1
        if s >= 1:
            pygame.draw.circle(screen, (255, 255, 0), coord, x_pos)
            pygame.display.flip()

            x_pos += v * clock.tick() / 1000

        pygame.display.flip()
    pygame.quit()
