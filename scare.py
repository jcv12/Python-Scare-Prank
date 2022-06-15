import pygame

from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('female_scream.wav')
pygame.mixer.music.play()
sleep(5)
image = pygame.image.load('scream.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)