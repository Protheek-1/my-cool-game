import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 857)) # i just set to diemsions of picture, can change  
clock = pygame.time.Clock()
pygame.display.set_caption("Frog") # name of window  
running = True
test_font = pygame.font.Font(None,100) # default font, size 100 maybe pixels idk

frog_surf = pygame.image.load('graphics/frog.jpg').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

#score text
score_surf = test_font.render('Frog', True, (180,180,180)) # text, anti-aliasing, color
score_rect = score_surf.get_rect(center = (600,100)) # this is the text position, center of screen, 100 pixels down

#charectars 
mini_frog_surface = pygame.image.load('graphics/mini_frog.png').convert_alpha()
mini_frog_rect = mini_frog_surface.get_rect(midbottom = (800, 700))

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (200, 700))
player_gravity = 0

while running: # this is just a while true loop because running  = True  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # on quit this cancells the while True loop and thus pygame.quit is called
     
        if event.type == pygame.MOUSEBUTTONDOWN: # jump imput method  
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 700: 
                player_gravity = -20
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 700:
                player_gravity = -20 

    screen.fill((40, 33, 80))  
    screen.blit(frog_surf,(0,0))
    screen.blit(ground_surf,(0,700))
    screen.blit(ground_surf,(510,700))
    pygame.draw.rect(screen,((20,20,20)),score_rect)
    pygame.draw.rect(screen,(130,230,180),score_rect,5, 8)
    screen.blit(score_surf,score_rect)

    mini_frog_rect.left -= 4
    screen.blit(mini_frog_surface,mini_frog_rect) # this is the mini frog moving across the screen
    if mini_frog_rect.left < -300: mini_frog_rect.left = 1270
    
    #player
    player_gravity += 0.7
    player_rect.y += player_gravity
    if player_rect.bottom >= 700: player_rect.bottom = 700 # this is the ground collision, so player doesn't fall through ground
    screen.blit(player_surface,player_rect) # this is the player charectar, not moving rn but will be in future
    
    # keys = pygame.key.get_pressed()
    # keys[pygame.K_SPACE]

    # if player_rect.colliderect(mini_frog_rect):
    #     print('collision') # this is the collision detection, not doing anything rn but will be in future
    # mouse_pos = pygame.mouse.get_pos() 
    # if player_rect.collidepoint(mouse_pos): 
    #     print(pygame.mouse.get_pressed()) 
        
    pygame.display.update() # refreshed display to schow what we added  
    clock.tick(60) # max fps, min fps is just based on comp so optimise  #


pygame.quit()