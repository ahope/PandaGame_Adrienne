#import basic pygame modules
import pygame
from pygame.locals import *

SCREENRECT     = Rect(0, 0, 640, 480)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    width = 800
    height = 450
    screen = pygame.display.set_mode((width, height))
    
    bgdtile = pygame.image.load('imgs/Forest.png')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((100, 250, 50))
    background.blit(bgdtile, (0,0))

    ## Step 1: Load panda image
    panda_img = pygame.image.load('imgs/panda1.png')
    sad_panda_img = pygame.image.load('imgs/sad_panda.png')

    ## Step LAST: Resize our panda!
    panda_img = pygame.transform.scale(panda_img, (100, 100))
    sad_panda_img = pygame.transform.scale(sad_panda_img, (100, 100))

    ## Step 2: Get bounding rectangle
    panda_rect = panda_img.get_rect()

    ## Create Spike obstacle
    spike_img = pygame.image.load('imgs/Spikes_built.png')
    spike_img = pygame.transform.scale(spike_img, (100, 100))
    spike_rect = spike_img.get_rect()
    spike_rect = spike_rect.move(0, 240)


     # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    x = 0
    y = 0

    step_size = 10
    panda_is_hurt = False

    # Event loop
    while 1:
      x = 0
      y = 0
      panda_is_hurt = False
      screen.blit(background, (0, 0))

      ## Paint obstacle on the screen
      screen.blit(spike_img, spike_rect)

      ## Process Game Events
      # print(pygame.event.get())
      for event in pygame.event.get():
        if event.type == KEYDOWN: 
          ## Up arrow key 
          if event.key == K_UP: 
            x = 0
            y = -step_size
          ## Down arrow key 
          if event.key == K_DOWN: 
            x = 0
            y = step_size
          ## Left arrow key 
          if event.key == K_LEFT: 
            x = -step_size
            y = 0
          ## Right arrow key 
          if event.key == K_RIGHT: 
            x = step_size
            y = 0

      ## Step 4: Move the rectangle to move the panda
      panda_rect = panda_rect.move(x, y)

      if panda_rect.colliderect(spike_rect):
        # print("ARGGGGGHHHHH")
        # scream_sound.play()
        panda_is_hurt = True
        print ('x\a')

      # ## Step 5: Check that we're not off the screen
      # if (panda_rect.right > width or panda_rect.left < 0): 
      #   x = -x
      # if (panda_rect.bottom > height or panda_rect.top < 0):
      #   y = -y

      ## Step 3: Paint panda on gameboard
      if panda_is_hurt: 
        screen.blit(sad_panda_img, panda_rect)
      else: 
        screen.blit(panda_img, panda_rect)

      
      
      pygame.display.flip()



#call the "main" function if running this script
if __name__ == '__main__': main()