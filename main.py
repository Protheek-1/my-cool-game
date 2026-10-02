import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Awesomsauce Game")
running = True

while running: # this is just a while true loop because running  = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # on quit this cancells the while True loop and thus pygame.quit is called
                            # could replace with exit() but this is better i think  

    screen.fill((40, 33, 80))
    pygame.display.update()
    clock.tick(60) # max fps, min fps is just based on comp so optimise  

pygame.quit() 