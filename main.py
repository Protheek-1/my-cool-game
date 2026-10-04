import pygame
import sys
from random import randint
#start variables
game_active = False
start_time = 0
score = 0

# score system, making it a function makes it more usable and easier to change  
def display_score(): 
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = test_font.render(f'Score: {current_time}', False, (50,50,50))
    score_rect = score_surf.get_rect(center = (600,100))
    pygame.draw.rect(screen,('#74BAF5'),score_rect,)
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6.7

            if obstacle_rect.bottom == 400: screen.blit(sword_surf,obstacle_rect)
            else: screen.blit(frog_surface,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] # 
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

# ui setup
pygame.init()
screen = pygame.display.set_mode((1200, 857)) # i just set to diemsions of picture, can change  
clock = pygame.time.Clock()
pygame.display.set_caption("Frog") # name of window at the top  
running = True
test_font = pygame.font.Font('fonts/pixeltype.ttf',100) # default font, size 100 maybe pixels idk#

#bg
sky_surf = pygame.image.load('graphics/sky.jpg').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

#charectars 
frog_surface = pygame.image.load('graphics/frog.png').convert_alpha()
frog_surface = pygame.transform.rotozoom(frog_surface, 0, 0.6)

sword_surf = pygame.image.load('graphics/sword.png').convert_alpha()
sword_surf = pygame.transform.rotozoom(sword_surf, 0, 1.3)

obstacle_rect_list = []

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_surface = pygame.transform.rotozoom(player_surface, 0, 0.6)
player_rect = player_surface.get_rect(midbottom = (200, 700))
player_gravity = 0

# intro/end screen
player_stand = pygame.image.load('graphics/player.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (580,420))

title_surface = test_font.render('The Frog Game', False, '#D9423A') # kinda wanna change the colour  
title_rect = title_surface.get_rect(center = (600,100))

start_surface = test_font.render('Press Space to Start', False, '#D9423A')
start_rect = start_surface.get_rect(center = (600,750))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1550)

# game code
while running: # this is just a while true loop because running  = True  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # on quit this cancells the while True loop and thus pygame.quit is called
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: # jump imput method  
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 695: 
                    player_gravity = -25
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 695:
                    player_gravity = -25
        else: # reset after game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() # resets score to 0
                
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(frog_surface.get_rect(midbottom = (randint(1300,1600), 700))) 
            else:
                obstacle_rect_list.append(sword_surf.get_rect(midbottom = (randint(1300,1600), 400)))
    

    if game_active:
        screen.fill((40, 33, 80))  
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,700))
        screen.blit(ground_surf,(510,700))

        score = display_score()
        
        #player
        player_gravity += 0.825
        player_rect.y += player_gravity
        if player_rect.bottom >= 700: player_rect.bottom = 700 # this is the ground collision, so player doesn't fall through ground
        screen.blit(player_surface,player_rect) # this is the player charectar, not moving rn but will be in future

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((50, 73, 110))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear() # clears the obstacles so they don't stay on screen when game is restarted
        player_rect.midbottom = (200, 700)
        player_gravity = 0


        screen.blit(title_surface, title_rect)
        if score == 0: 
            screen.blit(start_surface, start_rect)
        else:
            score_message = test_font.render(f'Score: {score}', True, "#D9423A")
            score_message_rect = score_message.get_rect(center = (600, 750))
            screen.blit(score_message, score_message_rect)

       
    pygame.display.update() # refreshed display to schow what we added  
    clock.tick(60) # max fps, min fps is just based on comp so optimise  #


pygame.quit()