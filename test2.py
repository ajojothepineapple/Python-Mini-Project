from turtle import Turtle
from random import randint
import tkinter as _

pic = Turtle()
pic.speed(1)

bic = pic.clone()
bic.speed(40)

sic = bic.clone()
sic.speed(40)


kic = sic.clone()
kic.speed(20)

while True:
    colorid = round(randint(100000,900000)) #get a random color using color id
    colorid = str(colorid)
    colors = ['white','#00CED1']

    WIDTH, LENGTH = 25, 125
    pic.width(WIDTH)
    #pic.hideturtle()
    pic.color("#" + colorid)
    pic.left(180)
    pic.backward(90)
    pic.left(90)
    pic.forward(90)
    pic.right(90)
    pic.forward(90)
    pic.left(90)
    pic.backward(90)
    
    
    WIDTH, LENGTH = 25, 125


    pic.width(WIDTH)

    pic.forward(LENGTH)
    
    #make multiples of square measurements by multilplying using limits for multiplier

    #the center square
    # bic.hideturtle()
    # bic.fillcolor("#" + colorid)
    # bic.begin_fill()
    # bic.left(180)
    # bic.backward(90)
    # bic.left(90)
    # bic.forward(90)
    # bic.right(90)
    # bic.forward(90)
    # bic.left(90)
    # bic.backward(90)
    # bic.end_fill()


    
    # kic.hideturtle()
    # kic.fillcolor("#" + colorid)
    # kic.begin_fill()
    # kic.color(colors[0])
    # kic.left(200)
    # kic.backward(110)
    # kic.left(110)
    # kic.forward(110)
    # kic.right(110)
    # kic.forward(110)
    # kic.left(110)
    # kic.backward(110)
    # kic.end_fill()


    # kic.hideturtle()
    # kic.fillcolor("#" + colorid)
    # kic.begin_fill()
    # kic.color(colors[1])
    # kic.left(200)
    # kic.backward(110)
    # kic.left(110)
    # kic.forward(110)
    # kic.right(110)
    # kic.forward(110)
    # kic.left(110)
    # kic.backward(110)
    # kic.end_fill()

 

   
  

    
    

