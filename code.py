
#Rectangles using OOP concept

#import and initialize pygame 
import pygame
pygame.init()
#set dimensions of the screen
screen=pygame.display.set_mode((800,800))
running=True
#Colors
#screen fil

#creating a Rectangle class
class polygon():
    def __init__(self,c,d):
        self.surface=screen
        self.color=c
        self.dimetions=(d) 
    def rectangle(self):
        self.draw=pygame.draw.rect(self.surface,self.color,self.dimetions)


#creating Instances  

bluerectangle=polygon("blue",(200,200,100,100))  
bluerectangle.rectangle()

redrectangle=polygon("red",(300,300,200,200))
redrectangle.rectangle()
#accessing methods 
#Display update to reflect the things on screeen

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
