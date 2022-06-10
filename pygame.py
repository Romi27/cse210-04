# Importing the pygame module
import pygame
import sys
 
# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()
 
# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((500,400))

pygame.display.set_caption('Mi primer juego :D')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
 
 
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
 
# Variable to store the
# velocity of the platform
platform_vel = 5
 
# Starting coordinates of the platform
x = 100
y = 150
 
# Creating a rect with width
# and height
rect = Rect(x, y, 200, 50)
 
# Creating a boolean variable that
# we will use to run the while loop
run = True
 
 
# Creating an infinite loop
# to run our game
while run:
 
    # Setting the framerate to 30fps
    clock.tick(30)
 
    # Multiplying platform_vel with -1
    # if its x coordinate is less then 100
    # or greater than or equal to 300.
    if rect.left >=300 or rect.left<100:
        platform_vel*= -1
 
    # Adding platform_vel to x
    # coordinate of our rect
    rect.left += platform_vel
 
    # Drawing the rect on the screen using the
    # draw.rect() method
    pygame.draw.rect(window, (255,   0,   0),rect)
 
    # Updating the display surface
    pygame.display.update()
 
    # Filling the window with white color
    window.fill((255,255,255))