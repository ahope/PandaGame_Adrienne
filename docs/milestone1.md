# Milestone 1: Build the Game World

Our first step is to build our Game World. We have 3 things to build: 

* The field/background
* The hero/Panda
* The obstacles/spikes

## Outcomes for Milestone 1

When our game does the following, we're done with this milestone: 

* The game runs with no complaints
* A window shows the game field we painted
  * The field should fill the entire window
* A panda is shown on the game field in a desired location 
  * Could be at (0,0), or in the center of the field, or elsewhere
* One obstacle is shown on the game field, in a different location from the Panda

## Things we need to know 

### Loading images in PyGame

PyGame uses objects called (Surface)[https://www.pygame.org/docs/ref/surface.html] to represent images. 
The Surface is basically an array of pixels, where every pixel has a different color. We can 
set those pixel colors ourselves (and draw simple or complex images), or read in an existing image, 
where the pixels depend on that image. 

A Surface knows how to draw itself, either at its current size or different sizes. 

[docs](https://www.pygame.org/docs/ref/image.html#pygame.image.load)

```python
panda_img = pygame.image.load('imgs/panda1.png')
```

### Using Rect to keep track of locations and sizes

In graphical games, one of the most important and challenging things is to keep track of the things in our 
world: where they are, how big are they, and if they are colliding with anything else. 

PyGame provides [Rect](https://www.pygame.org/docs/ref/rect.html)s to help us manage this. 

In this game, all of our objects have 2 components: 
* The image (Surface) that holds the objects visual representation/what it looks like
* The rectangle (Rect) keeps track of where it is and how big it is

Here's an example, where we load an image, then create a rectangle to keep track of the location/size of the image: 

```python
panda_img = pygame.image.load('imgs/panda1.png')
panda_rect = panda_img.get_rect()
```

If our image doesn't match the size we want our panda to be in the game, we can resize it: 

```python
panda_img = pygame.image.load('imgs/panda1.png')
panda_img = pygame.transform.scale(panda_img, (100, 100))
panda_rect = panda_img.get_rect()
```

Then, as the game is played, we modify ```panda_rect``` to keep the updated location and size of our panda.

### Painting things on the Game Board

When we write code for the game, a lot goes into the game logic, but none of that matters if we can't 
see it on the screen! 

The way we show things on the screen is to use the [display](https://www.pygame.org/docs/ref/display.html). 
A display a special Surface; it is very much like the Surface we use for our objects in the game, but it does a 
little more to make it appear in a window on our computer. 

To get things to show in the game window: 

* Create a display
* Paint everything on the display
* **Tell the display to paint itself on the screen **

That last step is most important!! If we don't tell it to paint itself on the screen, our game will never 
update. 

Here's an example: 

```python
width = 800
height = 450
## Create a display: 
##   Get the Surface that is part of the window holding our game
screen = pygame.display.set_mode((width, height))

## Draw the Panda on the screen Surface
##   (using the panda image and rect we created earlier)
screen.blit(panda_img, panda_rect)

## Tell the game to update the game image in the window
pygame.display.flip()
```

Note the second step, ```screen.blit(panda_img, panda_rect)```: 
"blit" means to paint the thing we want (the panda image) at a specified place (the panda rect) on the destination 
(the screen). 
In graphics, "blit" is a word used to copy some pixels from one image to another. 

**Why do we have to flip()?** 

Why do we have to do this extra step of calling "flip()" to show the game screen? Let's think back to our game loop. 
Remember, in our game loop, we're going through the state of our game and updating the screen to show the new state of 
the game. Usually, we have a bunch of stuff we want to update in one iteration of the loop: maybe the Panda has changed 
locations, and an obstacle has moved. We are repainting the entire screen with every loops, so we want to update ALL of the 
things before we actually show it on the screen. It's a technique called "double-buffering": draw everything off-screen 
first, and when we're done drawing everything, THEN update the screen with the final image. 

## Putting everything together for Milestone 1

Our goal for Milestone 1 is to run the game with the game field, the panda, and an obstacle. Therefore, 
we need to do the following: 

* For every *thing*: 
  * Read in an image
  * Create a Rect to keep track of the size and location of everything
* Set up the display: 
  * Create the display and get the screen
* Set up the game loop: 
  * In every loop, do the following: 
    * Paint the background on the screen
    * Paint the Panda on the screen
    * Paint the obstacle on the screen
    * flip() the screen so it shows in the window




