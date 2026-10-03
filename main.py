import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 857)) # i just set to diemsions of picture, can change  
clock = pygame.time.Clock()
pygame.display.set_caption("Frog") # name of window  
running = True
test_font = pygame.font.Font(None,100) # default font, size 100 maybe pixels idk


frog_surface = pygame.image.load('graphics/frog.jpg').convert()
text_surface = test_font.render('Frog', True, 'green') # text, anti-aliasing, color
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
#charectars 

mini_frog_surface = pygame.image.load('graphics/mini_frog.png').convert_alpha()
mini_frog_rect = mini_frog_surface.get_rect(midbottom = (800, 700))

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (200, 700))


while running: # this is just a while true loop because running  = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # on quit this cancells the while True loop and thus pygame.quit is called
                            # could replace with exit() but this is better i think  

    screen.fill((40, 33, 80)) # useless rn cause picture covers whole display surface  
    screen.blit(frog_surface,(0,0))
    screen.blit(ground_surface,(0,700))
    screen.blit(ground_surface,(510,700))
    screen.blit(text_surface,(500,100))

    mini_frog_rect.left -= 4
    screen.blit(mini_frog_surface,mini_frog_rect) # this is the mini frog moving across the screen
    if mini_frog_rect.left < -300: # screen wrap around 
        mini_frog_rect.left = 1270

    screen.blit(player_surface,player_rect) # this is the player charectar, not moving rn but will be in future


    pygame.display.update() # refreshed display to schow what we added  
    clock.tick(60) # max fps, min fps is just based on comp so optimise  #


pygame.quit()