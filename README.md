# Creating our PandaGame, based on Preppie! 

This project is inspired by a game, [Preppie!](https://en.wikipedia.org/wiki/Preppie!_(video_game)), 
we used to play on our Atari 800 when I was a kid. It's a fun game for kids to build, with lots of ways 
to customize the story, graphics, and game play. 

We're building this game using PyGame on ReplIt. It's a bit constrained (can't play music with the PyGame/ReplIt 
combo yet), but easy to get started. 


## Intro to PyGame 

[PyGame](https://www.pygame.org/news) is a Python library that is designed to make it easy to build games. 
It's been around for a while (you can tell from the graphics in the docs!) but provides solid basics for 
game building. 

The core concept to be familiar with is the ***Game Loop***. Our game happens on a loop: every time we 
go through the loop, our code decides the current state of the game and what happens next. 

Some of the things we do in the game loop: 
* Check to see if there is any input from the user, and what it is
* Determine if anything has moved or changed
* Determine what gets painted on the screen, and where
* Update the state of anything we want to keep track of 


At the end of our loop, we **paint the current game board on the screen**. 

Other than that, we use PyGame for also: 
* Loading up images
* Doing geometric math for us
  *  In games, there's a lot of math-- in this Preppie game we're building, it's primarily about 
      whether rectangles intersect, meaning did one thing run into another thing
* Painting graphics on the screen
* Reading input from the keyboard

## A Simple PyGame

The PyGame we're building has a fairly simple structure: 

* Set up the Game world
   * Load in images
   * Decide how big they need to be and where on the screen they are
* Set up the Game Loop
   * Our Game Loop will do the following: 
     * Paint the background/game field
     * Read in the keyboard to get user input
     * Update locations of things in the game world
     * Check to see if the new locations should cause something else to happen
     * Paint the things in their new locations
     * Tell the game to paint the updated world on the screen 


# Intro to Building the Game

There are a few concrete steps we'll take to build this game: 

1. Watch the [Preppie! video](https://www.youtube.com/watch?v=ut32gM6SmoE) 
2. Decide on our own version of the game
   * We broke the game down into the following components: 
      * A hero on a quest! 
      * A quest
      * Obstacles we need to beat to achieve the quest
   * We decided our game had the following: 
      * The hero: A Panda
      * The quest: Collect bamboo
      * The obstacles: 
         * Spikes (littered in the field) that injure the panda
         * Battering Rams (that move across the field) that injure the panda
3. Find some artwork for our game
4. Iterate on building the game: 
   * Build the game with the world
   * Add the Panda to the world and make it move
   * Control the movement of the Panda
   * Add obstacles to the world
   * Make something happen when the Panda hits the obstacles

# Milestones

* [Milestone 1](docs/milestone1.md): Getting the game loop going 
* [Milestone 2](docs/milestone2.md): Moving the Panda

