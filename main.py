import pygame
import pygame
import os

Width, Height = 900, 500
Win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("First Game!")

White = (255, 255, 255)
FPS = 60

Yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

def draw_window():
        Win.fill(White)
        pygame.display.update()


def main(): 
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()