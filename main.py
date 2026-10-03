import pygame
import sys

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = test_font.render(f'Score: {current_time}', True, (250,250,250))
    score_rect = score_surf.get_rect(center = (600,100))
    pygame.draw.rect(screen,((130,150,240)),score_rect, 0, 10)
    screen.blit(score_surf,score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((1200, 857)) # i just set to diemsions of picture, can change  
clock = pygame.time.Clock()
pygame.display.set_caption("Frog") # name of window at the top  
running = True
test_font = pygame.font.Font(None,100) # default font, size 100 maybe pixels idk#

game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load('graphics/sky.jpg').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

#charectars 
frog_surface = pygame.image.load('graphics/frog.png').convert_alpha()
frog_surface = pygame.transform.rotozoom(frog_surface, 0, 0.6)
frog_rect = frog_surface.get_rect(midbottom = (800, 700))

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_surface = pygame.transform.rotozoom(player_surface, 0, 0.6)
player_rect = player_surface.get_rect(midbottom = (200, 700))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/player.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (580,420))

title_surface = test_font.render('The Frog Game', True, '#D9423A') # kinda wanna change the colour  
title_rect = title_surface.get_rect(center = (600,100))

start_surface = test_font.render('Press Space to Start', True, '#D9423A')
start_rect = start_surface.get_rect(center = (600,750))


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
                frog_rect.left = 1270
                player_rect.midbottom = (200, 700)
                start_time = pygame.time.get_ticks() # resets score to 0
    

    if game_active:
        screen.fill((40, 33, 80))  
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,700))
        screen.blit(ground_surf,(510,700))
        # pygame.draw.rect(screen,((20,20,20)),score_rect)
        # pygame.draw.rect(screen,(130,230,180),score_rect,5, 8)
        # screen.blit(score_surf,score_rect)

        score = display_score()

        frog_rect.left -= 6
        screen.blit(frog_surface,frog_rect) # this is the mini frog moving across the screen
        if frog_rect.left < -300: frog_rect.left = 1270
        
        #player
        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom >= 700: player_rect.bottom = 700 # this is the ground collision, so player doesn't fall through ground
        screen.blit(player_surface,player_rect) # this is the player charectar, not moving rn but will be in future


        if player_rect.colliderect(frog_rect):
            game_active = False
        
    
    else:
        screen.fill((120, 153, 210))
        screen.blit(player_stand, player_stand_rect)

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