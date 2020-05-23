## This program is a Turtle Artist that draws the following code


def fill_color(color):      ## function with parameter that fills colors
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    return

def random_color():     ## function generates random colors
    red = m.randint(0, 255)
    green = m.randint(0, 255)
    blue = m.randint(0, 255)
    colorToReturn = (red, green, blue)
    return colorToReturn

def ears():     ## draw both ears on the pig
    for i in range(1):
        t.circle(-40, 125)
    fill_color("#ffe6d9")
    t.left(70)
    t.pendown()
    t.fd(30)        ## draw left ear
    t.right(130)
    t.fd(28)
    
    t.penup()
    t.left(60)
    t.fd(30)
    
    t.pendown()     ## draw right ear
    t.left(40)
    t.fd(25)
    t.right(130)
    t.fd(35)
    t.end_fill()
    return

def eye():      ## draw eyes
    for i in range(2):
        fill_color("#000000")
        t.circle(-3, 90)
        t.circle(-8, 90)
        t.end_fill()
    return    

def face():     # draw face
    for i in range(2):
       fill_color("#ffe6d9")
       t.circle(-40, 90)
       t.circle(-85, 90)
       t.end_fill()
    return

def nose():     ## draw nose
    for i in range(2):
        fill_color("#ffac95")
        t.circle(30, 90)
        t.circle(9, 90)
        t.end_fill()
    return

def nostril():      ## draw nostrils
    t.dot(8, "black")    
    return

def blush():        ## draw blush
    t.dot(16, "#fdcdca")
    t.dot(13, "#ff9690")
    t.dot(10, "#ff7d76")
    return

def left_arm():     ## draw left arm
    fill_color("#ffe6d9")
    t.fd(20)
    for i in range(1):
        t.circle(10, 130)
    t.fd(15)
    for i in range(1):
        t.circle(6, 155)
    t.fd(12)
    t.end_fill()
    return

def right_arm():        ## draw right arm
    fill_color("#ffe6d9")
    t.fd(12)
    t.right(10)
    for i in range(1):
        t.circle(6, 180)
    t.fd(23)
    for i in range(1):
        t.circle(8, 140)
    t.fd(33)
    t.end_fill()
    return

def big_heart():        ## draw the heart the pig is holding
    fill_color(heart_color)     ## heart color is random each time
    t.fd(18)
    t.penup()
    t.fd(18)
    t.pendown()
    t.fd(10)
    for i in range(1):      ##right half of the heart
        t.circle(13, 180)
    t.fd(22)

    t.setheading(90)
    t.left(45)
    t.fd(18)
    for i in range(1):
        t.circle(13, 180)
    t.fd(8)

    t.penup()
    t.fd(10)
    t.pendown()
    t.fd(29)
    return


def other_heart(r):     ## draw hearts with parameter r that gives a different radius to each heart
    t.setheading(0)
    t.left(47)
    t.pendown()
    fill_color(heart_color)     ## heart color is random each time
    t.fd(48)
    for i in range(1):      ##right half of the heart
        t.circle(r, 180)
    t.fd(22)

    t.setheading(90)
    t.left(45)
    t.fd(18)
    for i in range(1):
        t.circle(r, 180)
    t.fd(46)    
    return


################################ TOP LEVEL BELOW

import turtle as t
import random as m

t.colormode(255)

heart_color = random_color()        ## set heart color to random

t.speed(10)

## draw face
t.penup()
t.fd(80)
t.left(90)
t.fd(30)
t.left(45)
t.pendown()
face()

## draw ears
t.penup()
ears()

## draw eyes
t.penup()
t.fd(22)
t.right(90)
t.fd(24)
t.left(20)
t.pendown()
eye()

t.penup()
t.setheading(180)
t.fd(45)
t.pendown()
t.left(50)
eye()

## draw nose
t.penup()
t.setheading(-90)
t.fd(30)
t.pendown()
t.left(45)

nose()
t.setheading(0)

## draw nostrils
t.penup()
t.fd(13)
t.setheading(90)
t.fd(5)
t.pendown()
nostril()

t.penup()
t.setheading(0)
t.fd(18)
nostril()

## draw blush
t.penup()
t.fd(35)
blush()

t.penup()
t.setheading(180)
t.fd(85)
blush()

t.penup()
t.setheading(270)
t.fd(30)
t.setheading(0)
t.fd(10)
t.setheading(270)
t.right(40)

## draw arms
t.pendown()
left_arm()

t.penup()
t.goto(170, -5)
t.setheading(180)
t.pendown()
right_arm()

## draw the heart the pig is holding
t.penup()
t.goto(140, -30)
t.setheading(0)
t.left(47)
t.pendown()
fill_color(heart_color)
big_heart()
t.end_fill()

t.penup()


## draw other 4 hearts at the end 
for i in range(4):
    t.goto(m.randint(-300, 0), m.randint(-250, 250))        ## each heart is at different position
    other_heart(m.randint(10, 13))      ## each heart is different size
    t.end_fill()
    t.penup()
