#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:53:49 2021

@author: isabellamancini
"""
# my pseudocode looks very different but basically I made a wavey almost 
# checker pattern line in the middle then I made 2 lines of arrows on either
# side of it which have randomized colors also its a little slow so patience is key
import turtle 
import math 
import random

turtle.colormode(255)

panel= turtle.Screen()
w=600
h=600
panel.setup(width=w, height=h)

panel.bgcolor((0,0,0))

y= 585

background = turtle.Turtle()
background.up()
background.setpos(-600,585)
background.speed(10)
background.color(250,250,250)

   # sin formula from https://stackoverflow.com/questions/20918749/how-to-draw-sine-in-python-turtle
    #this formula draws the sin line in the background and i modified the values to get the shape i desired
background.down()
for x in range(-600,600):
    background.goto(x,15*math.sin((x/100)*2*math.pi)) 
    background.goto(x,20*math.sin((x/100)*2*math.pi))
    background.goto(x,100*math.sin((x/100)*2*math.pi))
    
    #background.forward(180)
background.up()   

# the colors in the arrows below are random because I used random.choice of the 
# palette I made for the color
A1= turtle.Turtle()
A1.shape("arrow")

palette= ["firebrick","pale violet red","salmon","tomato","light coral" ]
A1.goto(-120,200)
size= 4

for i in range(3):
    A1.turtlesize(size)
    A1.down()
    A1.color(random.choice(palette))
    A1.stamp()
    A1.up()
    A1.forward(60)
    
A1.up()
A2= turtle.Turtle()
A2.shape("arrow")
A2.goto(-120,-200)

for i in range(3):
    A2.turtlesize(size)
    A2.down()
    A2.color(random.choice(palette))
    A2.stamp()
    A2.up()
    A2.forward(60)







