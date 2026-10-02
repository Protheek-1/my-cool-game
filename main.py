import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 857)) # i just set to diemsions of picture, can change  
clock = pygame.time.Clock()
pygame.display.set_caption("Frog") # name of window  
running = True
test_font = pygame.font.Font(None,100) # default font, size 100 maybe pixels idk

frog_surface = pygame.image.load('graphics/frog.jpg')
text_surface = test_font.render('Frog', True, 'green') # text, anti-aliasing, color

while running: # this is just a while true loop because running  = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # on quit this cancells the while True loop and thus pygame.quit is called
                            # could replace with exit() but this is better i think  

    screen.fill((40, 33, 80)) # useless rn cause picture covers whole display surface  
    screen.blit(frog_surface,(0,0))
    screen.blit(text_surface,(500,100))


    pygame.display.update()
    clock.tick(60) # max fps, min fps is just based on comp so optimise  

pygame.quit()