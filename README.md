import pgzrun
import random

#flappy ball

# Pygame Standard for deciding the title of your game window
TITLE="Flappy ball:1"
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH=1000
HEIGHT=800
#variables to set up random colors
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
clr=(red,green,blue)

#BLUE = 0, 128, 255
GRAVITY = 2000.0  # pixels per second per second
#Create a class for Ball
class ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_y
        self.radius= 40
    def circ(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,clr)


        cir
