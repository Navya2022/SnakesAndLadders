#importing all modules
import turtle
import time
import random


#creating check variables
diceflag= 0
proof= 1
some = 0
life = 0
breakflag = 0
#main list for coordinates
coordinates=[(-160,-150)]
#appending the coordinates of the board
for j in range(0,10):
    if j%2==0:
        for i in range (0,10):
            coordinates.append((-130+29*i,-150+j*33))
    else:
        for i in range (0,10):
            coordinates.append((140-30*i,-150+j*33))

snake={coordinates[28]:coordinates[10],coordinates[48]:coordinates[16],coordinates[37]:coordinates[3],
       coordinates[75]:coordinates[32],coordinates[96]:coordinates[42],coordinates[94]:coordinates[71]}
ladder={coordinates[4]:coordinates[56],coordinates[12]:coordinates[50],coordinates[14]:coordinates[55],
       coordinates[22]:coordinates[58],coordinates[41]:coordinates[79],coordinates[54]:coordinates[88]}



def intro():
   turtle.addshape("b1.gif")
   turtle.addshape("b2.gif")
   turtle.addshape("b3.gif")
   turtle.addshape("b4.gif")
   turtle.addshape("b5.gif")
   turtle.shape("b5.gif")
   time.sleep(0.1)
   turtle.shape("b4.gif")
   time.sleep(0.1)
   turtle.shape("b3.gif")
   time.sleep(0.1)
   turtle.shape("b1.gif")
   time.sleep(0.1)
   turtle.shape("b2.gif")
   time.sleep(1)
   screen.clear()
#function to check if dice is pressed
def isDicePressed(x,y):
    global diceflag
    global proof
    if proof == 1:
        diceflag = 1
    if proof == 2:
        diceflag = 2
    if proof == 3:
        diceflag = 3
    if proof == 4:
        diceflag = 4
        
    return(diceflag)

def isAdvantage(i):
    global some
    global adv
    global life
    global proof
    
    if i ==1:
        l = coordinates.index((pawn1.xcor(),pawn1.ycor()))
        some = 1
    if i ==2:
        l = coordinates.index((pawn2.xcor(),pawn2.ycor()))
        some = 2
    if i ==3:
        l = coordinates.index((pawn3.xcor(),pawn3.ycor()))
        some = 3
        
    if l == 57 and life == 0 :
        ad = screen.textinput("Congrats you have collected an Advantage!!!",
                            "Enter ok to roll the dice once more")
        life = 1
        lif.ht()
        if ad.lower() == "ok":
            proof = 4


#main game code for 2 players
def players2():
    global some
    global proof
    global diceflag
    dice.onclick(isDicePressed)
    if diceflag == 1:
        l = coordinates.index((pawn1.xcor(),pawn1.ycor()))
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        if l+dice_coord > 100:
            dice_coord = 0
        elif l+dice_coord == 100:
            pawn1.goto(coordinates[100])
            win(1)
        else:
            pawn1.goto(coordinates[l+dice_coord])
            

        diceflag = 0
        proof = 2
        l = coordinates.index((pawn1.xcor(),pawn1.ycor()))
        for j in snake:
            if (pawn1.xcor(), pawn1. ycor())  == j:
                    pawn1.goto(snake[j])
        for t in ladder:
            if(pawn1.xcor(),pawn1.ycor())==t:
                    pawn1.goto(ladder[t])
        isAdvantage(1)
    dice.onclick(isDicePressed)
    if diceflag == 4 and some == 1 :
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        pawn1.goto(coordinates[57+dice_coord])
        diceflag = 0
        proof = 2
        some = 0

    if diceflag == 2:
        l = coordinates.index((pawn2.xcor(),pawn2.ycor()))
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        if l+dice_coord > 100:
            dice_coord = 0
        elif l+dice_coord == 100:
            pawn2.goto(coordinates[100])
            win(2)
        else:
            pawn2.goto(coordinates[l+dice_coord])
            
        diceflag = 0
        proof = 1
        for j in snake:
            if (pawn2.xcor(), pawn2. ycor())  == j:
                     pawn2.goto(snake[j])
        for t in ladder:
            if(pawn2.xcor(),pawn2.ycor())==t:
                    pawn2.goto(ladder[t])
        isAdvantage(2)
    dice.onclick(isDicePressed)
    if diceflag == 4 and some == 2 :
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        pawn2.goto(coordinates[57+dice_coord])
        diceflag = 0
        proof = 1
        some = 0
        
       

#main game code for 3 players
def players3():
    global lives
    global proof
    global diceflag
    dice.onclick(isDicePressed)
    if diceflag ==1 :
        l = coordinates.index((pawn1.xcor(),pawn1.ycor()))
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        if l+dice_coord > 100:
            dice_coord = 0
        elif l+dice_coord == 100:
            pawn1.goto(coordinates[100])
            win(1)
        else:
            pawn1.goto(coordinates[l+dice_coord])
        diceflag = 0
        proof = 2
        for j in snake:
            if (pawn1.xcor(), pawn1. ycor())  == j:
                     pawn1.goto(snake[j])
        for t in ladder:
            if(pawn1.xcor(),pawn1.ycor())==t:
                    pawn1.goto(ladder[t])
        isAdvantage(1)
    dice.onclick(isDicePressed)
    if diceflag == 4 and some == 1 :
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        pawn1.goto(coordinates[57+dice_coord])
        diceflag = 0
        proof = 2

    dice.onclick(isDicePressed)
    if diceflag ==2:
        l = coordinates.index((pawn2.xcor(),pawn2.ycor()))
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        if l+dice_coord > 100:
            dice_coord = 0
        elif l+dice_coord == 100:
            pawn2.goto(coordinates[100])
            win(2)
        else:
            pawn2.goto(coordinates[l+dice_coord])
        diceflag = 0
        proof = 3
        for j in snake:
            if (pawn2.xcor(), pawn2. ycor())  == j:
                     pawn2.goto(snake[j])
        for t in ladder:
            if(pawn2.xcor(),pawn2.ycor())==t:
                    pawn2.goto(ladder[t])
        isAdvantage(2)
    dice.onclick(isDicePressed)
    if diceflag == 4 and some == 2 :
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        pawn2.goto(coordinates[57+dice_coord])
        diceflag = 0
        proof = 3

    dice.onclick(isDicePressed)
    if diceflag ==3:
        l = coordinates.index((pawn3.xcor(),pawn3.ycor()))
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        if l+dice_coord > 100:
            dice_coord = 0
        elif l+dice_coord == 100:
            pawn3.goto(coordinates[100])
            win(3)
        else:
            pawn3.goto(coordinates[l+dice_coord])
        diceflag = 0
        proof = 1
        for j in snake:
            if (pawn3.xcor(), pawn3. ycor())  == j :
                pawn3.goto(snake[j])
        for t in ladder:
            if(pawn3.xcor(),pawn3.ycor())==t:
                    pawn3.goto(ladder[t])
        isAdvantage(3)
    dice.onclick(isDicePressed)
    if diceflag == 4 and some == 3 :
        dice_coord = random.randint(1,6)
        dice_img(dice_coord)
        pawn3.goto(coordinates[57+dice_coord])
        diceflag = 0
        proof = 1
        
def dice_img(roll):
    if roll==1:
        turtle.addshape("1.gif")
        dice.shape("1.gif")
    if roll==2:
        turtle.addshape("2.gif")
        dice.shape("2.gif")
    if roll==3:
        turtle.addshape("3.gif")
        dice.shape("3.gif")
    if roll==4:
        turtle.addshape("4.gif")
        dice.shape("4.gif")
    if roll==5:
        turtle.addshape("5.gif")
        dice.shape("5.gif")
    if roll==6:
        turtle.addshape("6.gif")
        dice.shape("6.gif")
    
    

def win(o):
    global breakflag
    turtle.pu()
    turtle.ht()
    turtle.goto(-30,-100)
    turtle.pd()
    pawn1.ht()
    pawn2.ht()
    pawn3.ht()
    dice.ht()
    if o ==1:
        screen.bgpic("youwin.gif")
        turtle.write("Pawn 1 wins!!!", move=False, align='left', font=('Times New Roman', 23, 'bold')) 
    
    if o ==2:
        screen.bgpic("youwin.gif")
        turtle.write("Pawn 2 wins!!!", move=False, align='left', font=('Times New Roman', 23, 'bold')) 

    if o ==3:
        screen.bgpic("youwin.gif")
        turtle.write("Pawn 3 wins!!!", move=False, align='left', font=('Times New Roman', 23, 'bold')) 
    time.sleep(2)
    breakflag = 1

        
while True:
    print("select the suitable options")
    print("1.if 2 players")
    print("2.if 3 players")
    print("3.exit the game")

    choice = int(input("enter the number"))\

    turtle.addshape("pawn1.gif")
    turtle.addshape("pawn2.gif")
    turtle.addshape("pawn3.gif")
    turtle.addshape("life.gif")
    
    turtle.addshape("6.gif")
    #setting turtle screen
    screen = turtle.Screen()
    screen.setup(800,700)
    screen.setworldcoordinates(-200,-200,200,200)
    intro()
    
    

    #creatting python turtles
    pawn1 = turtle.Turtle()
    pawn1.pu()
    pawn1.ht()
    pawn1.goto(-160,-150)
    pawn1.shape("pawn1.gif")

    dice = turtle.Turtle()
    dice.pu()
    dice.ht()
    dice.goto(-170,0)
    
    dice.shape("6.gif")

    lif = turtle.Turtle()
    lif.pu()
    lif.st()
    lif.goto(coordinates[57])
    lif.shape("life.gif")

    pawn2 = turtle.Turtle()
    pawn2.pu()
    pawn2.ht()
    pawn2.goto(-160,-150)
    pawn2.shape("pawn2.gif")

    pawn3 = turtle.Turtle()
    pawn3.pu()
    pawn3.ht()
    pawn3.goto(-160,-150)
    pawn3.shape("pawn3.gif")

    if choice == 1:
        screen.bgpic("board.gif")
        pawn1.st()
        pawn2.st()
        dice.st()
        while breakflag == 0:
            players2()
        else:
            screen.clear()
            screen.setup(0,0)

    if choice == 2:
        screen.bgpic("board.gif")
        pawn3.st()
        pawn1.st()
        pawn2.st()
        dice.st()
        choice = 0
        while breakflag == 0:
            players3()
        else:
            screen.clear()
            screen.setup(0,0)

    if choice == 3:
        screen.bye()
        break

    
    











    
