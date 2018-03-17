# from turtle import Turtle
# Leonardo = Turtle()  
# userinput = input("Enter a number. ")


# userinput = int(userinput)
# #makes string into int

# print(userinput>10 and userinput < 47 or userinput == 54)
# Leonardo.forward(userinput)

# from random import randint

# RPS = randint(1,15)
# #rand int between 1 and 15 inclusive

# userchoice = input("Choose rock paper or scissors...")
# print(userchoice)

# print(RPS)
# print("Rock is..." + str(RPS <=5))
# print("Paper is..." + str((RPS<= 10) and (RPS> 5)))
# print("Scissors is ..." +str((RPS <= 15) and (RPS > 10)))


# if RPS == 1 and userchoice == "rock":
#     print("Computer chose rock. And you tied.")
# elif RPS == 1 and userchoice == "paper":
#     print("Computer chose paper. And you win.")
# elif RPS == 1 and userchoice == "scissors":
#     print("Computer chose scissors. And you lose.")

# #elif runs code till true

# if RPS <= 5 and userchoice == "rock":
#     print("Computer chose rock. And you tied")
# elif ((RPS <= 10) and (RPS > 5)):
#     print("Computer chose paper.")
# elif ((RPS <= 15) and (RPS > 10)):
#     print("Computer chose scissors.")



# number = input("Enter a number. ")

#if x % 2 == 0

#     print("x is even")
# else:
#     print("Odd")




from random import randint
from turtle import Turtle, Screen
import time
 #import time library for sleep function for delay

screen = Screen() 
pic = Turtle()
pic.speed(2)
 # determines speed of turtle drawing

RPS = randint(1,3)
  #random number between 1 and 3 inclusive

userchoice = input("Choose r, p, or s. ")
print(userchoice)
breaks = True
while userchoice != "r" and userchoice != "p" and userchoice!= "s":
      print("Type again! This time r, p, or s!") 
      userchoice = input("Choose r, p, or s. ") 
      userchoice == "r" and userchoice == "s" and userchoice == "p"
      breaks = False
   #forces user to input r, p or s, using while loop
if RPS == 1:
      computerchoice = "p"
if RPS == 2:
      computerchoice = "s"
if RPS == 3:
      computerchoice = "r"
   #establishing computer choice in string

      print(computerchoice)

if userchoice == computerchoice:
      print("You Tied!")
      time.sleep(2)
      pic.begin_fill()
      pic.fillcolor("gray")
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
   #prints gray square for tie

elif  computerchoice == "p" and userchoice == "s":
      print("Computer chose paper. You win!")
      time.sleep(2)            
      pic.begin_fill() 
      pic.fillcolor("green")   #draws green square for win
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
elif computerchoice == "p" and userchoice == "s":
      print("Computer chose paper. You Win!")
      time.sleep(2)
      pic.begin_fill() 
      pic.fillcolor("green")
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
elif computerchoice == "r" and userchoice == "p":
      print("Computer chose rock. You Win!")
      time.sleep(2)
      pic.begin_fill() 
      pic.fillcolor("green")
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
elif computerchoice == "r" and userchoice == "s":
      print("Computer chose rock. You Lose!")
      time.sleep(2)
      pic.begin_fill() 
      pic.fillcolor("red")  #draws red square for loss
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
elif computerchoice == "s" and userchoice == "p":
      print("Computer chose scissors. You Lose!")
      time.sleep(2)
      pic.begin_fill() 
      pic.fillcolor("red")
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
elif computerchoice == "s" and userchoice == "r":
      print("Computer chose scissors. You Win!")
      time.sleep(2)
      pic.begin_fill() 
      pic.fillcolor("green")
      pic.left(180)
      pic.backward(90)
      pic.left(90)
      pic.forward(90)
      pic.right(90)
      pic.forward(90)
      pic.left(90)
      pic.backward(90)
      pic.end_fill()
      screen.exitonclick()
#all the possible situations excluding ties and draws corresponding colored square



#while loop for turtle 

# while True:
#     x = randint(-50,50) 
#     y = randint(-50,50)

#     pic.forward(x)
#     pic.left(y)
#     pic.backward(y)
#     print(pic.pos())
#     # need to add parameters of edge of turtle screen




# runloop = True 


# pic.shape("arrow") #makes turtle an arrow
# pic.speed(20) #changes speed

# bic = pic.clone() #makes another turtle
# bic.shape("turtle") #changes turtle shape
# bic.speed(20)  #changes speed

# iterationsN = 0 #setting to 0 

# while runloop:
#     x = randint(10,1000)
#     y = randint(10,100)

#     colorid = round(randint(100000,600000)) #get a random color using color id
#     colorid = str(colorid)
#     print("Color id " + colorid)
#     iterationsN = iterationsN + 1 #each iter. will add 1 signifying the numb. of iters.
#     pic.begin_fill()
#     pic.fillcolor("#" + colorid)
#     pic.left(180)
#     pic.backward(90)
#     pic.left(90)
#     pic.forward(90)
#     pic.right(90)
#     pic.forward(90)
#     pic.left(90)
#     pic.backward(90)
#     pic.end_fill()
#     pic.penup() #stops drawing to go to x,y
#     pic.goto(x,y)
#     pic.hideturtle()

    
#     bic.begin_fill()
#     bic.fillcolor("#" + colorid) #random color fills
#     bic.left(x)
#     bic.backward(y)
#     bic.left(x)
#     bic.forward(90)
#     bic.right(90)
#     bic.forward(y)
#     bic.left(90)
#     bic.backward(90)
#     bic.end_fill()
#     bic.penup()
#     bic.goto(x,y) 
#     bic.hideturtle() #hides turtle

#     print("Number of iterations " + str(iterationsN)) #prints number if times program has run
    
#     interationsN = int(iterationsN) #casting str to int
#     if iterationsN == 28:
#         runloop = False #terminates when program runs 28 times
#         screen = Screen()
#         screen.exitonclick()

