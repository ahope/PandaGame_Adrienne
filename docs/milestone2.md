# Milestone 2: Moving our hero, Panda!

Now that we've got the game structure in place, let's start controlling our hero! 

## Outcomes for Milestone 2: 

* Make the Panda move on the screen (not with user input)
* Ensure the Panda does not go OFF the screen

## Things we need to know

In Milestone 1, the focus was on getting things on the screen, which included loading in images, 
creating Rects to keep track of locations, painting on the screen in the game loop, and flip()-ing 
the display so it can show on the screen. 

Now, we're going to make things move. 

### Make things move

The key here is for us to think about "what does it mean for the Panda to move?". In our game 
world, the answer is that we paint it in a different location on the screen. 

How do we paint our Panda in a different location on the screen? Well, right now, we paint the 
Panda using ```panda_rect```, since that is the Rect that is keeping track of where the Panda is 
in our game. 

Therefore: to move the Panda, we change the ```panda_rect``! 

### Moving a ```Rect```

Our ```Rect``` is the thing we update to change the location; how do we change our Rect? 

[[docs](https://www.pygame.org/docs/ref/rect.html)]

First, a note about Rect: 

A ```Rect``` is a tuple (group) of numbers: (left, top, width, height).
* ```left``` is basically x-coordinate of the 
rectangle, or the left edge
* ```top``` is the y-coordinate (top edge)
* ```width``` is how wide the rectangle is
   * The right edge of the rectangle is at ```left + width```
* ```height``` is the tall the rectangle is
   * The bottom edge of the rectangle is at ```top + height```

**REMEMBER**: the screen coordinate system is (0, 0) at the upper left corner of the screen. 
Increasing x goes to the right of the screen; increasing y goes to the bottom of the screen. 
Negative x and y are off the screen to the left and top. 

```
x = 2
y = 2
panda_rect = panda_rect.move(x, y)

## OR
panda_rect.move_ip(move(x, y))
```

This is showing us 2 ways to move. The first one (```panda_rect = panda_rect.move(x, y)```) is because 
```move()``` creates a new Rect with the updated values; the second shows that ```move_ip()``` just 
updates the values of the same Rect. 

If ```panda_rect = (0, 0, 5, 5)```, then ```panda_rect.move_ip(2, 2)``` changes ```panda_rect``` to be ```2, 2, 5, 5```. 


### Checking for boundaries

We now know how to move our Panda by moving the Rectangle representing the Panda. But: we want to make sure 
that the Panda stays on the game field. 

Because everything in our game is represented by a Rect, we can make sure the locations stay valid by 
comparing Rects. Thankfully, pyGame makes it easy for us to do that! 

```python
screen_rect = screen.get_rect()

if (panda_rect.left < screen_rect.left):
  print("Panda went off the left side of the screen!!")
if (panda_rect.right > screen_rect.right):
  print("Panda went off the right side of the screen!!") 
if (panda_rect.top < screen_rect.top):
  print("Panda went off the top side of the screen!!")
if (panda_rect.bottom > screen_rect.bottom):
  print("Panda went off the bottom side of the screen!!")
```

## Putting it all together

We're going to move our Panda by telling it to keep moving in the same direction until it hits an 
edge of the screen. When it hits the edge of the screen, we reverse the direction. 

The direction the Panda is moving is just an x, y step. If x is positive, Panda moves to the right. If it's 
negative, Panda moves to the left. If y is positive, it moves to the bottom of the screen; if it's negative, 
it moves toward the top. 

To get our Panda moving and staying on the screen, here's what we need to do in our loop: 

* Tell the Panda to move by moving the panda_rect a certain amount (x, y)
* Check to see if the Panda went off the screen 
   * If it did, change the direction of x or y to get it back on the screen. 
   * Change the direction of x/y by setting it negative. (```x = -x```). 

```python
x = 2
y = 2

screen_rect = screen.get_rect()

## The Game Loop
while True: 
  ## Check to see if the Panda is off the screen 
  if (panda_rect.left < screen_rect.left):
    print("Panda went off the left side of the screen!!")
    x = -x 
  if (panda_rect.right > screen_rect.right):
    print("Panda went off the right side of the screen!!") 
    x = -x
  if (panda_rect.top < screen_rect.top):
    print("Panda went off the top side of the screen!!")
    y = -y
  if (panda_rect.bottom > screen_rect.bottom):
    print("Panda went off the bottom side of the screen!!")
    y = -y
    
  ## Move the Panda by moving the rect
  panda_rect.move_ip(x, y)
    
  ## Paint the Panda on the screen 
  screen.blit(panda_img, panda_rect)
  pygame.display.flip()

```

