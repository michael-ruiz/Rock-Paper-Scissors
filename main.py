import pygame
import os
import random
from Button import Button

pygame.font.init()
pygame.display.set_caption('Rock Paper Scissors Game')

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
npc_points = 0
player_points = 0
clock = pygame.time.Clock()

ROCK_IMG = pygame.image.load(os.path.join('Assets', 'ROCK.png'))
PAPER_IMG = pygame.image.load(os.path.join('Assets', 'PAPER.png'))
SCISSORS_IMG = pygame.image.load(os.path.join('Assets', 'SCISSORS.png'))
POINT_FONT = pygame.font.SysFont('Arial', 25, bold=True)
TITLE_FONT = pygame.font.SysFont('Arial', 35, bold=True)

rock_btn = Button(WHITE, 50, (HEIGHT/2 - 125), 249, 250, '')
paper_btn = Button(WHITE, (WIDTH/2 - 125), (HEIGHT/2 - 125), 249, 250, '')
scissors_btn = Button(WHITE, (WIDTH - 300), (HEIGHT/2 - 125), 249, 250, '')

LOSE_IMG = pygame.image.load(os.path.join('Assets', 'lose.png'))
WIN_IMG = pygame.image.load(os.path.join('Assets', 'win.png'))
TIE_IMG = pygame.image.load(os.path.join('Assets', 'tie.png'))

quit_btn = Button(RED, 250, 300, 150, 75, 'Quit')
retry_btn = Button(GREEN, 450, 300, 150, 75, 'Retry')

def draw_start():
    global player_points, npc_points
    WINDOW.fill(WHITE)
    title_font = TITLE_FONT.render('Welcome to Rock Paper Scissors!', True, BLACK)
    WINDOW.blit(title_font, (210, 10))

    player_font = POINT_FONT.render('Player Score: ' + str(player_points), True, BLACK)
    WINDOW.blit(player_font, (10, 10))
    npc_font = POINT_FONT.render('NPC Score: ' + str(npc_points), True, BLACK)
    WINDOW.blit(npc_font, (WIDTH-140, 10))

    rock_btn.draw(WINDOW)
    paper_btn.draw(WINDOW)
    scissors_btn.draw(WINDOW)

    WINDOW.blit(ROCK_IMG, (50, HEIGHT/2 - 125))
    WINDOW.blit(PAPER_IMG, (WIDTH/2 - 125, HEIGHT/2 - 125))
    WINDOW.blit(SCISSORS_IMG, ((WIDTH - 300), HEIGHT/2 - 125))

    pygame.display.update()

def draw_end(end_type):
    run = True

    while run:
        global player_points, npc_points
        WINDOW.fill(WHITE)
        player_font = POINT_FONT.render('Player Score: ' + str(player_points), True, BLACK)
        WINDOW.blit(player_font, (10, 10))
        npc_font = POINT_FONT.render('NPC Score: ' + str(npc_points), True, BLACK)
        WINDOW.blit(npc_font, (WIDTH-170, 10))

        if end_type == 0:
            WINDOW.blit(LOSE_IMG, (0, 0))
        elif end_type == 2:
            WINDOW.blit(WIN_IMG, (0, 0))
        else:
            WINDOW.blit(TIE_IMG, (0, 0))

        quit_btn.draw(WINDOW, (0,0,0))
        retry_btn.draw(WINDOW, (0,0,0))
        
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if quit_btn.is_over(mouse_pos):
                    pygame.quit()
                if retry_btn.is_over(mouse_pos):
                    main()
        
        clock.tick(FPS)
        pygame.display.update()

def is_winner(player_choice):
    choices = ['rock', 'paper', 'scissors']
    global player_points, npc_points
    num = random.randint(0,2)
    npc_choice = choices[num]
    end_type = 1

    if npc_choice == 'rock' and player_choice == 'paper':
        end_type = 2
        player_points += 1
    elif npc_choice == 'rock' and player_choice == 'scissors':
        end_type = 0
        npc_points += 1
    elif npc_choice == 'paper' and player_choice == 'scissors':
        end_type = 2
        player_points += 1
    elif npc_choice == 'paper' and player_choice == 'rock': 
        end_type = 0
        npc_points += 1
    elif npc_choice == 'scissors' and player_choice == 'rock':
        end_type = 2
        player_points += 1
    elif npc_choice == 'scissors' and player_choice == 'paper':
        end_type = 0
        npc_points += 1
    return end_type
    
def main():
    run = True

    while run:
        draw_start()
        clock.tick(FPS)
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if rock_btn.is_over(mouse_pos):
                    player_choice = 'rock'
                    draw_end(is_winner(player_choice))
                if paper_btn.is_over(mouse_pos):
                    player_choice = 'paper'
                    draw_end(is_winner(player_choice))
                if scissors_btn.is_over(mouse_pos):
                    player_choice = 'scissors'
                    draw_end(is_winner(player_choice))
        
    pygame.quit()

if __name__ == '__main__':
    main()