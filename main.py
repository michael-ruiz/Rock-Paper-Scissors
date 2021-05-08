import pygame
import os

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BG_WHITE = (255, 255, 255)
FPS = 60
pygame.display.set_caption('Rock Paper Scissors Game')

ROCK_IMG = pygame.image.load(os.path.join('Assets', 'ROCK.png')) # 249 x 250
PAPER_IMG = pygame.image.load(os.path.join('Assets', 'PAPER.png'))
SCISSORS_IMG = pygame.image.load(os.path.join('Assets', 'SCISSORS.png'))

def draw():
    WINDOW.fill(BG_WHITE)
    WINDOW.blit(ROCK_IMG, (50, HEIGHT/2 - 125))
    WINDOW.blit(PAPER_IMG, (WIDTH/2 - 125, HEIGHT/2 - 125))
    WINDOW.blit(SCISSORS_IMG, (600, HEIGHT/2 - 125))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
        
    pygame.quit()

if __name__ == '__main__':
    main()