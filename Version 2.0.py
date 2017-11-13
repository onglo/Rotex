from tkinter import *
import time
import math
from random import randint
import random
import threading
count = 1
triangleFills1 = ['yellow','light sky blue','red','green','purple','orange']
triangleFills2 = ['yellow','light sky blue','red','green','purple','orange']
triangleFills3 = ['yellow','light sky blue','red','green','purple','orange']
triangleFills4 = ['yellow','light sky blue','red','green','purple','orange']
colours = ['yellow','lightskyblue','red','green','purple','orange']
colourNames = ['yellow','lightskyblue','red','green','purple','orange']
count = 1
window = Tk()
canvasOne = Canvas(window,width = 550, height = 700)
canvasOne.pack()
window.geometry('550x700')
window.wm_title('Rotation-Sensation')
menuFinished = False
gameOver = False
secondMenu = True
score = 0
highScore = 0
hexagonColor = 0
rightButton = False
leftButton = False



def getHighScore():
    global highScore
    file = open('highscore.txt', 'r')
    highScore = int(file.readline())
    file.close()

def rotateRight(window,canvasOne):
    for count in range(1,5):
        global triangleFills1
        global triangleFills2
        global triangleFills3
        global triangleFills4
        global triangleOne
        global triangleTwo
        global triangleThree
        global triangleFour
        global triangleFive
        global triangleSix
        if count % 4 == 1:
            triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
            triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
            triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
            window.update()
            time.sleep(0.016666666666666666)
            temp = triangleFills1[5]
            for i in range(0,5):
                triangleFills1[5 - i] = triangleFills1[4 - i]
            triangleFills1[0] = temp
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)


        elif count % 4 == 2:
            triangleOne = canvasOne.create_polygon(275,450,275 - 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),275 + 75*math.sin(45*(math.pi)/180),450 - 75*math.sin(45*(math.pi)/180),fill=triangleFills2[0], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,275 + 75*math.sin(45*(math.pi)/180),450 - 75*math.sin(45*(math.pi)/180),275 + 75*math.cos(15*(math.pi)/180),450 + 75*math.sin(15*(math.pi)/180),fill=triangleFills2[1], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,275 + 75*math.cos(15*(math.pi)/180),450 + 75*math.sin(15*(math.pi)/180),275 + 75*math.sin(15*(math.pi)/180),450 + 75*math.cos(15*(math.pi)/180),fill=triangleFills2[2], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,275 + 75*math.sin(15*(math.pi)/180),450 + 75*math.cos(15*(math.pi)/180),275 - 75*math.sin(45*(math.pi)/180), 450 + 75*math.cos(45*(math.pi)/180),fill=triangleFills2[3], tags = 'green')
            triangleFive = canvasOne.create_polygon(275,450,275 - 75*math.sin(45*(math.pi)/180),450 + 75*math.cos(45*(math.pi)/180),275 - 75*math.cos(15*(math.pi)/180),450 - 75*math.sin(15*(math.pi)/180),fill=triangleFills2[4], tags = 'purple')
            triangleSix = canvasOne.create_polygon(275,450,275 - 75*math.cos(15*(math.pi)/180),450 - 75*math.sin(15*(math.pi)/180),275 - 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),fill=triangleFills2[5], tags = 'orange')
            window.update()
            temp = triangleFills2[5]
            for i in range(0,5):
                triangleFills2[5 - i] = triangleFills2[4 - i]
            triangleFills2[0] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)


        elif count % 4 == 3:
            triangleOne = canvasOne.create_polygon(275,450,275 + (75**2-37.5**2)**(1/2),487.5,275 + (75**2-37.5**2)**(1/2),412.5,fill=triangleFills3[1], tags = 'lightskyblue')
            triangleTwo = canvasOne.create_polygon(275,450,275,525,275 + (75**2-37.5**2)**(1/2),487.5,fill=triangleFills3[2], tags = 'red')
            triangleThree = canvasOne.create_polygon(275,450,275 - (75**2-37.5**2)**(1/2),487.5,275,525,fill=triangleFills3[3], tags = 'green')
            triangleFour = canvasOne.create_polygon(275,450,275 - (75**2-37.5**2)**(1/2),412.5,275 - (75**2-37.5**2)**(1/2),487.5,fill=triangleFills3[4], tags = 'purple')
            triangleFive = canvasOne.create_polygon(275,450,275,375,275 - (75**2-37.5**2)**(1/2),412.5,fill=triangleFills3[5], tags = 'orange')
            triangleSix = canvasOne.create_polygon(275,450,275 + (75**2-37.5**2)**(1/2),412.5,275,375,fill=triangleFills3[0], tags = 'yellow')
            window.update()
            temp = triangleFills3[5]
            for i in range(0,5):
                triangleFills3[5 - i] = triangleFills3[4 - i]
            triangleFills3[0] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)
        elif count % 4 == 0:
            triangleOne = canvasOne.create_polygon(275,450,275 + 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),275 + 75*math.cos(15*(math.pi)/180), 450 - 75*math.sin(15*(math.pi)/180),fill=triangleFills4[0], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,275 + 75*math.cos(15*(math.pi)/180), 450 - 75*math.sin(15*(math.pi)/180),275 + 75*math.cos(45*(math.pi)/180), 450 + 75*math.sin(45*(math.pi)/180),fill=triangleFills4[1], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,275 + 75*math.cos(45*(math.pi)/180), 450 + 75*math.sin(45*(math.pi)/180),275 - 75*math.sin(15*(math.pi)/180), 450 + 75*math.cos(15*(math.pi)/180),fill=triangleFills4[2], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,275 - 75*math.sin(15*(math.pi)/180), 450 + 75*math.cos(15*(math.pi)/180),275 - 75*math.cos(15*(math.pi)/180), 450 + 75*math.sin(15*(math.pi)/180),fill=triangleFills4[3], tags = 'green')
            triangleFive = canvasOne.create_polygon(275,450,275 - 75*math.cos(15*(math.pi)/180), 450 + 75*math.sin(15*(math.pi)/180),275 - 75*math.cos(45*(math.pi)/180), 450 - 75*math.sin(45*(math.pi)/180),fill=triangleFills4[4], tags = 'purple')
            triangleSix = canvasOne.create_polygon(275,450,275 - 75*math.cos(45*(math.pi)/180), 450 - 75*math.sin(45*(math.pi)/180),275 + 75*math.sin(15*(math.pi)/180), 450 - 75*math.cos(15*(math.pi)/180),fill=triangleFills4[5], tags = 'orange')
            window.update()
            temp = triangleFills4[5]
            for i in range(0,5):
                triangleFills4[5 - i] = triangleFills4[4 - i]
            triangleFills4[0] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)


def rotateLeft(window,canvasOne):
    for count in range(1,5):
        global triangleFills1
        global triangleFills2
        global triangleFills3
        global triangleFills4
        global triangleOne
        global triangleTwo
        global triangleThree
        global triangleFour
        global triangleFive
        global triangleSix
        if count % 4 == 1:
            triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
            triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
            triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
            window.update()
            time.sleep(0.016666666666666666)
            temp = triangleFills1[0]
            for i in range(0,6):
                try:
                    triangleFills1[i] = triangleFills1[i + 1]
                except IndexError:
                    triangleFills1[i] = temp
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)


        elif count % 4 == 0:
            triangleOne = canvasOne.create_polygon(275,450,275 - 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),275 + 75*math.sin(45*(math.pi)/180),450 - 75*math.sin(45*(math.pi)/180),fill=triangleFills2[1], tags = 'lightskyblue')
            triangleTwo = canvasOne.create_polygon(275,450,275 + 75*math.sin(45*(math.pi)/180),450 - 75*math.sin(45*(math.pi)/180),275 + 75*math.cos(15*(math.pi)/180),450 + 75*math.sin(15*(math.pi)/180),fill=triangleFills2[2], tags = 'red')
            triangleThree = canvasOne.create_polygon(275,450,275 + 75*math.cos(15*(math.pi)/180),450 + 75*math.sin(15*(math.pi)/180),275 + 75*math.sin(15*(math.pi)/180),450 + 75*math.cos(15*(math.pi)/180),fill=triangleFills2[3], tags = 'green')
            triangleFour = canvasOne.create_polygon(275,450,275 + 75*math.sin(15*(math.pi)/180),450 + 75*math.cos(15*(math.pi)/180),275 - 75*math.sin(45*(math.pi)/180), 450 + 75*math.cos(45*(math.pi)/180),fill=triangleFills2[4], tags = 'purple')
            triangleFive = canvasOne.create_polygon(275,450,275 - 75*math.sin(45*(math.pi)/180),450 + 75*math.cos(45*(math.pi)/180),275 - 75*math.cos(15*(math.pi)/180),450 - 75*math.sin(15*(math.pi)/180),fill=triangleFills2[5], tags = 'orange')
            triangleSix = canvasOne.create_polygon(275,450,275 - 75*math.cos(15*(math.pi)/180),450 - 75*math.sin(15*(math.pi)/180),275 - 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),fill=triangleFills2[0], tags = 'yellow')
            window.update()
            temp = triangleFills2[0]
            for i in range(0,6):
                try:
                    triangleFills2[i] = triangleFills2[i + 1]
                except IndexError:
                    triangleFills2[i] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)


        elif count % 4 == 3:
            triangleOne = canvasOne.create_polygon(275,450,275 + (75**2-37.5**2)**(1/2),487.5,275 + (75**2-37.5**2)**(1/2),412.5,fill=triangleFills3[2], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,275,525,275 + (75**2-37.5**2)**(1/2),487.5,fill=triangleFills3[3], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,275 - (75**2-37.5**2)**(1/2),487.5,275,525,fill=triangleFills3[4], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,275 - (75**2-37.5**2)**(1/2),412.5,275 - (75**2-37.5**2)**(1/2),487.5,fill=triangleFills3[5], tags = 'green')
            triangleFive = canvasOne.create_polygon(275,450,275,375,275 - (75**2-37.5**2)**(1/2),412.5,fill=triangleFills3[0], tags = 'purple')
            triangleSix = canvasOne.create_polygon(275,450,275 + (75**2-37.5**2)**(1/2),412.5,275,375,fill=triangleFills3[1], tags = 'orange')
            window.update()
            temp = triangleFills3[0]
            for i in range(0,6):
                try:
                    triangleFills3[i] = triangleFills3[i + 1]
                except IndexError:
                    triangleFills3[i] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)
        elif count % 4 == 2:
            triangleOne = canvasOne.create_polygon(275,450,275 + 75*math.sin(15*(math.pi)/180),450 - 75*math.cos(15*(math.pi)/180),275 + 75*math.cos(15*(math.pi)/180), 450 - 75*math.sin(15*(math.pi)/180),fill=triangleFills4[1], tags = 'yellow')
            triangleTwo = canvasOne.create_polygon(275,450,275 + 75*math.cos(15*(math.pi)/180), 450 - 75*math.sin(15*(math.pi)/180),275 + 75*math.cos(45*(math.pi)/180), 450 + 75*math.sin(45*(math.pi)/180),fill=triangleFills4[2], tags = 'lightskyblue')
            triangleThree = canvasOne.create_polygon(275,450,275 + 75*math.cos(45*(math.pi)/180), 450 + 75*math.sin(45*(math.pi)/180),275 - 75*math.sin(15*(math.pi)/180), 450 + 75*math.cos(15*(math.pi)/180),fill=triangleFills4[3], tags = 'red')
            triangleFour = canvasOne.create_polygon(275,450,275 - 75*math.sin(15*(math.pi)/180), 450 + 75*math.cos(15*(math.pi)/180),275 - 75*math.cos(15*(math.pi)/180), 450 + 75*math.sin(15*(math.pi)/180),fill=triangleFills4[4], tags = 'red')
            triangleFive = canvasOne.create_polygon(275,450,275 - 75*math.cos(15*(math.pi)/180), 450 + 75*math.sin(15*(math.pi)/180),275 - 75*math.cos(45*(math.pi)/180), 450 - 75*math.sin(45*(math.pi)/180),fill=triangleFills4[5])
            triangleSix = canvasOne.create_polygon(275,450,275 - 75*math.cos(45*(math.pi)/180), 450 - 75*math.sin(45*(math.pi)/180),275 + 75*math.sin(15*(math.pi)/180), 450 - 75*math.cos(15*(math.pi)/180),fill=triangleFills4[0])
            window.update()
            temp = triangleFills4[0]
            for i in range(0,6):
                try:
                    triangleFills4[i] = triangleFills4[i + 1]
                except IndexError:
                    triangleFills4[i] = temp
            time.sleep(0.016666666666666666)
            canvasOne.delete(triangleOne)
            canvasOne.delete(triangleTwo)
            canvasOne.delete(triangleThree)
            canvasOne.delete(triangleFour)
            canvasOne.delete(triangleFive)
            canvasOne.delete(triangleSix)

def rotateLeftOnce(window,canvasOne):
    global triangleOne
    global triangleTwo
    global triangleThree
    global triangleFour
    global triangleFive
    global triangleSix
    canvasOne.delete(triangleOne)
    canvasOne.delete(triangleTwo)
    canvasOne.delete(triangleThree)
    canvasOne.delete(triangleFour)
    canvasOne.delete(triangleFive)
    canvasOne.delete(triangleSix)
    if menuFinished == True and secondMenu == True:
        rotateLeft(window, canvasOne)
        """
        rotateLeftThread = threading.Thread(name = 'rotateLeftThread',  target=rotateLeft, args=(window, canvasOne))
        rotateLeftThread.daemon = True
        rotateLeftThread.start()
        """
    else:
        rotateLeft(window, canvasOne)
    triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
    triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
    triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red') 
    triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green') 
    triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
    triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
def rotateRightOnce(window,canvasOne):
    global triangleOne
    global triangleTwo
    global triangleThree
    global triangleFour
    global triangleFive
    global triangleSix
    canvasOne.delete(triangleOne)
    canvasOne.delete(triangleTwo)
    canvasOne.delete(triangleThree)
    canvasOne.delete(triangleFour)
    canvasOne.delete(triangleFive)
    canvasOne.delete(triangleSix)
    if menuFinished == True and secondMenu == False:
        rotateLeft(window, canvasOne)
        """
        rotateRightThread = threading.Thread(name = 'rotateRightThread',  target=rotateRight, args=(window, canvasOne))
        rotateRightThread.daemon = True
        rotateRightThread.start()
        """
    else:
        rotateRight(window, canvasOne)
    triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
    triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
    triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red') 
    triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green') 
    triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
    triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')

def hexagonMenu():
    global menuFinished
    global gameName
    global pressToPlay
    global secondMenu
    gameName = canvasOne.create_text(275, 50, text = 'Welcome to Rotation Sensation!', justify = CENTER, font = ('Avenir Next', 30))
    pressToPlay = canvasOne.create_text(275, 600, text = 'Press Left or Right to begin!', justify = CENTER, font = ('Avenir Next', 20))
    window.update()
    while not menuFinished and secondMenu == True:
                rotateRightOnce(window,canvasOne)
                time.sleep(0.01)

def leftButtonPressed(window, canvasOne):
    global menuFinished
    global triangleOne
    global triangleTwo
    global triangleThree
    global triangleFour
    global triangleFive
    global triangleSix
    global secondMenu
    global triangleFills1
    global triangleFills2
    global triangleFills3
    global triangleFills4
    global hexagonColor
    global leftButton
    if menuFinished == False:
        menuFinished = True
        while triangleFills1[0] != 'yellow' and triangleFills2[0] != 'yellow' and triangleFills3[0] != 'yellow' and triangleFills4[0] != 'yellow':
            rotateRightOnce(window,canvasOne)
        triangleFills1 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills2 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills3 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills4 = ['yellow','light sky blue','red','green','purple','orange']
        hexagonColor = 0
        canvasOne.delete(triangleOne)
        canvasOne.delete(triangleTwo)
        canvasOne.delete(triangleThree)
        canvasOne.delete(triangleFour)
        canvasOne.delete(triangleFive)
        canvasOne.delete(triangleSix)
        canvasOne.delete(ALL)
        triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
        triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
        triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
        triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
        triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
        triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
        window.update()
        scoreLabel = canvasOne.create_text(500, 25, text = str(0), justify = CENTER, font = ('Avenir Next', 40))
        canvasOne.update()
        countdown()
        canvasOne.delete(scoreLabel)
        spawnBalls()
    elif secondMenu == False:
        hexagonColor = 0
        secondMenu = True
        while triangleFills1[0] != 'yellow' and triangleFills2[0] != 'yellow' and triangleFills3[0] != 'yellow' and triangleFills4[0] != 'yellow':
            rotateRightOnce(window,canvasOne)
        triangleFills1 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills2 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills3 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills4 = ['yellow','light sky blue','red','green','purple','orange']
        canvasOne.delete(triangleOne)
        canvasOne.delete(triangleTwo)
        canvasOne.delete(triangleThree)
        canvasOne.delete(triangleFour)
        canvasOne.delete(triangleFive)
        canvasOne.delete(triangleSix)
        canvasOne.delete(ALL)
        triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
        triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
        triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
        triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
        triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
        triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
        window.update()
        scoreLabel = canvasOne.create_text(500, 25, text = str(0), justify = CENTER, font = ('Avenir Next', 40))
        canvasOne.update()
        countdown()
        canvasOne.delete(scoreLabel)
        spawnBalls()
    else:
        rotateLeftOnce(window,canvasOne)


def rightButtonPressed(window, canvasOne):
    global menuFinished
    global triangleOne
    global triangleTwo
    global triangleThree
    global triangleFour
    global triangleFive
    global triangleSix
    global secondMenu
    global triangleFills1
    global triangleFills2
    global triangleFills3
    global triangleFills4
    global hexagonColor
    global rightButton
    if menuFinished == False:
        menuFinished = True
        canvasOne.delete(triangleOne)
        canvasOne.delete(triangleTwo)
        canvasOne.delete(triangleThree)
        canvasOne.delete(triangleFour)
        canvasOne.delete(triangleFive)
        canvasOne.delete(triangleSix)
        while triangleFills1[0] != 'yellow' and triangleFills2[0] != 'yellow' and triangleFills3[0] != 'yellow' and triangleFills4[0] != 'yellow':
            rotateRightOnce(window,canvasOne)
        triangleFills1 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills2 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills3 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills4 = ['yellow','light sky blue','red','green','purple','orange']
        hexagonColor = 0
        canvasOne.delete(ALL)
        triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
        triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
        triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
        triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
        triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
        triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
        window.update()
        scoreLabel = canvasOne.create_text(500, 25, text = str(0), justify = CENTER, font = ('Avenir Next', 40))
        canvasOne.update()
        countdown()
        canvasOne.delete(scoreLabel)
        spawnBalls()
    elif secondMenu == False:
        hexagonColor = 0
        secondMenu = True
        while triangleFills1[0] != 'yellow' and triangleFills2[0] != 'yellow' and triangleFills3[0] != 'yellow' and triangleFills4[0] != 'yellow':
            rotateRightOnce(window,canvasOne)
        triangleFills1 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills2 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills3 = ['yellow','light sky blue','red','green','purple','orange']
        triangleFills4 = ['yellow','light sky blue','red','green','purple','orange']
        canvasOne.delete(triangleOne)
        canvasOne.delete(triangleTwo)
        canvasOne.delete(triangleThree)
        canvasOne.delete(triangleFour)
        canvasOne.delete(triangleFive)
        canvasOne.delete(triangleSix)
        canvasOne.delete(ALL)
        triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
        triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
        triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
        triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
        triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
        triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')
        window.update()
        scoreLabel = canvasOne.create_text(500, 25, text = str(0), justify = CENTER, font = ('Avenir Next', 40))
        canvasOne.update()
        countdown()
        canvasOne.delete(scoreLabel)
        spawnBalls()
    else:
            rotateRightOnce(window,canvasOne)



def countdown():
    getReady = canvasOne.create_text(275, 250, text = 'Get Ready!', justify = CENTER, font = ('Avenir Next', 20))
    canvasOne.update()
    initialiseBalls()
    canvasOne.delete(getReady)
    canvasOne.update()
    go = canvasOne.create_text(275, 250, text = 'Go!', justify = CENTER, font= ('Avenir Next', 20))
    time.sleep(0.5)
    canvasOne.delete(go)
    canvasOne.update()
# TODO ask group if i should make it impossible to have two of the same colours in a row
def initialiseBalls():
    global firstCircle
    global secondCircle
    global thirdCircle
    global currentCircle
    global colours
    global colourNames
    currentCircle = 1
    random1 = randint(0,5)
    random2 = randint(0,5)
    random3 = randint(0,5)
    firstCircle = canvasOne.create_oval(20, 45, -20, 5, fill = colours[random1], outline = colours[random1], tags = colourNames[random1])
    moved = False
    while not moved:
        canvasOne.update()
        canvasOne.move(firstCircle, 2, 0)
        if canvasOne.coords(firstCircle)[2] == 162:
            canvasOne.update()
            break
    secondCircle = canvasOne.create_oval(20, 45, -20, 5, fill = colours[random2], outline = colours[random2], tags = colourNames[random2])
    moved = False
    while not moved:
        canvasOne.update()
        canvasOne.move(secondCircle, 2, 0)
        if canvasOne.coords(secondCircle)[2] == 108:
            canvasOne.move(secondCircle,1,0)
            canvasOne.update()
            break
    time.sleep(0.3)
    thirdCircle = canvasOne.create_oval(20, 45, -20, 5, fill = colours[random3], outline = colours[random3], tags = colourNames[random3])
    moved = False
    while not moved:
        canvasOne.update()
        canvasOne.move(thirdCircle,2,0)
        if canvasOne.coords(thirdCircle)[2]  == 54:
            canvasOne.move(thirdCircle,1,0)
            canvasOne.update()
            break
    canvasOne.update()
    """
    time.sleep(1)
    animateBalls()
    """
"""
def animateBalls():
    global firstCircle
    global secondCircle
    global thirdCircle
    global fourthCircle
    global currentCircle
    global colours
    global colourNames
    randomNumber = randint(0,5)
    if currentCircle == 1:
        fourthCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
        # firstOval one is in the 1st position
        currentCircle = 2
        movedAcross = False
        movedUp = False
        while not movedAcross:
            if movedUp == False:
                canvasOne.move(firstCircle,0,-2)
            canvasOne.move(secondCircle,2,0)
            canvasOne.move(thirdCircle,2,0)
            canvasOne.move(fourthCircle,2,0)
            canvasOne.update()
            distance =  162**2-canvasOne.coords(secondCircle)[2]**2
            if distance < 1:
                movedAcross = True
                break
            elif canvasOne.coords(firstCircle)[3] == 0:
                canvasOne.delete(firstCircle)
                canvasOne.update()
                movedUp = True
    elif currentCircle == 2:
        # firstOval one is in the 2st position
        firstCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
        currentCircle = 3
        movedAcross = False
        movedUp = False
        while not movedAcross:

            if movedUp == False:
                canvasOne.move(secondCircle,0,-2)
            canvasOne.move(thirdCircle,2,0)
            canvasOne.move(fourthCircle,2,0)
            canvasOne.move(firstCircle,2,0)
            canvasOne.update()
            distance = 162**2-canvasOne.coords(thirdCircle)[2]**2
            if distance < 1:
                movedAcross = True
                break
            elif canvasOne.coords(secondCircle)[3] == 0:
                canvasOne.delete(secondCircle)
                canvasOne.update()
                movedUp = True
    elif currentCircle == 3:
        # firstOval one is in the 3st position
        secondCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
        currentCircle = 4
        movedAcross = False
        movedUp = False
        canvasOne.update()
        while not movedAcross:

            if movedUp == False:
                canvasOne.move(thirdCircle,0,-2)
            canvasOne.move(fourthCircle,2,0)
            canvasOne.move(firstCircle,2,0)
            canvasOne.move(secondCircle,2,0)
            canvasOne.update()
            distance = 162**2-canvasOne.coords(fourthCircle)[2]**2
            if distance < 1:
                movedAcross = True
                break
            elif canvasOne.coords(thirdCircle)[3] == 0:
                canvasOne.delete(thirdCircle)
                canvasOne.update()
                movedUp = True
    else:
        # firstOval one is in the 4st position
        thirdCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
        currentCircle = 1
        movedAcross = False
        movedUp = False
        while not movedAcross:

            if movedUp == False:
                canvasOne.move(fourthCircle,0,-2)
            canvasOne.move(firstCircle,2,0)
            canvasOne.move(secondCircle,2,0)
            canvasOne.move(thirdCircle,2,0)
            canvasOne.update()
            distance = 162**2-canvasOne.coords(firstCircle)[2]**2
            if distance < 1:
                movedAcross = True
                break
            elif canvasOne.coords(fourthCircle)[3] == 0:
                canvasOne.delete(fourthCircle)
                canvasOne.update()
                movedUp = True


    ## for testing only
    time.sleep(1)
    animateBalls()

"""

# TODO ask if you can move the hexagon while it says get ready


def spawnBalls():
    global triangleFills1
    global gameOver
    global colours
    global menuFinished
    global playAgainText
    global scoreRectangeScore
    global scoreRectangeHighScore
    global scoreRectange
    global secondMenu
    global score
    global highScore
    global hexagonColor
    global currentCircle
    global firstCircle
    global secondCircle
    global thirdCircle
    global fourthCircle
    global colours
    global colourNames
    score = 0
    counter = 0
    difficulty = 2
    scoreLabel = canvasOne.create_text(275, 30, text = str(score), justify = CENTER, font = ('Avenir Next', 40))
    while gameOver == False:
        counter += 1
        if difficulty != 8:
            if counter % 4 == 0:
                difficulty += 1
        if currentCircle == 1:
            colour = canvasOne.gettags(firstCircle)[0]
            print(colour)
        elif currentCircle ==2:
            colour = canvasOne.gettags(secondCircle)[0]
            print(colour)
        elif currentCircle == 3:
            colour = canvasOne.gettags(thirdCircle)[0]
            print(colour)
        else:
            colour = canvasOne.gettags(fourthCircle)[0]
            print(colour)

        firstOval = canvasOne.create_oval(295,44,255,4, fill = colour, outline = colour, tags = colour)

        canvasOne.delete(scoreLabel)
        scoreLabel = canvasOne.create_text(500, 25, text = str(score), justify = CENTER, font = ('Avenir Next', 40))
        canvasOne.update()
        randomNumber = randint(0,5)

        if currentCircle == 1:
            fourthCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
            # firstOval one is in the 1st position
            currentCircle = 2
            movedAcross = False
            movedUp = False
            circleArray = [fourthCircle, thirdCircle, secondCircle, firstCircle]

        elif currentCircle == 2:
            # firstOval one is in the 2st position
            firstCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
            currentCircle = 3
            movedAcross = False
            movedUp = False
            circleAtFront = secondCircle
            circleArray = [firstCircle, fourthCircle, thirdCircle, secondCircle]

        elif currentCircle == 3:
            # firstOval one is in the 3st position
            secondCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
            currentCircle = 4
            movedAcross = False
            movedUp = False
            circleArray = [secondCircle, firstCircle, fourthCircle, thirdCircle]

        else:
            # firstOval one is in the 4st position
            thirdCircle = canvasOne.create_oval(0, 45, -40, 5, fill = colours[randomNumber], outline = colours[randomNumber], tags = colours[randomNumber])
            currentCircle = 1
            movedAcross = False
            movedUp = False
            circleArray = [thirdCircle, secondCircle, firstCircle, fourthCircle]

        hasHit = False
        while not hasHit:
            distance = 385**2 - canvasOne.coords(firstOval)[3]**2
            canvasOne.move(firstOval,0,difficulty)
            if movedAcross == False:
                canvasOne.move(circleArray[2],2,0)
                canvasOne.move(circleArray[1],2,0)
                canvasOne.move(circleArray[0],2,0)
                distance1 = 162**2-canvasOne.coords(circleArray[2])[2]**2
                if distance1 < 1:
                    movedAcross = True
            if movedUp == False:
                canvasOne.move(circleArray[3],0,-2)
                if canvasOne.coords(circleArray[3])[3] == 0:
                    movedUp = False
            time.sleep(0.01)
            window.update()
            if distance < 1:
                temp = canvasOne.gettags(firstOval)
                itemid = canvasOne.find_below(firstOval)
                hexColour = triangleFills1[0]
                if hexColour == 'light sky blue':
                    hexColour = 'lightskyblue'
                if temp[0] == 'light':
                    temp[0] = 'lightskyblue'
                print(temp[0])
                print(hexColour)
                if temp[0] != hexColour:
                    canvasOne.delete(firstOval)
                    canvasOne.delete(firstCircle)
                    canvasOne.delete(secondCircle)
                    canvasOne.delete(thirdCircle)
                    canvasOne.delete(fourthCircle)
                    window.unbind('<Left>')
                    window.unbind('<Right>')
                    canvasOne.delete(scoreLabel)
                    oldHighScore = highScore
                    if highScore < score:
                        highScore = score
                        file = open('highscore.txt', 'w')
                        file.write(str(highScore))
                    secondMenu = False
                    # a first game over tag that appears when the user looses
                    gameOverTag = canvasOne.create_text(275, 10, text = 'Game Over', justify = CENTER, font = ('Avenir Next', 40))
                    # make the tag move down
                    tagMoved = False
                    while not tagMoved:
                        canvasOne.move(gameOverTag,0,2)
                        canvasOne.update()
                        time.sleep(0.01)
                        if canvasOne.coords(gameOverTag)[1] == 250:
                            time.sleep(1)
                            canvasOne.delete(gameOverTag)
                            tagMoved = True

                    # put the recanangle that has the score and highscore into the window
                    scoreRectange = canvasOne.create_rectangle(30, 20, 510, 300)
                    #put some text in the rectange (score)
                    scoreRectangeScore = canvasOne.create_text(275, 100, text = 'Score: ' + str(score), justify = CENTER, font = ('Avenir Next', 40))

                    # check if it is a new highscore
                    if score > oldHighScore:
                        #put some text in the rectange (highscore)
                        scoreRectangeHighScore = canvasOne.create_text(275, 200, text = 'New High Score: ' + str(highScore), justify = CENTER, font = ('Avenir Next', 40))
                    else:
                        #put some text in the rectange (highscore)
                        scoreRectangeHighScore = canvasOne.create_text(275, 200, text = 'High Score: ' + str(highScore), justify = CENTER, font = ('Avenir Next', 40))

                    # put the text at the bottom of the screen that tells the user to press left or right to play again
                    playAgainText = canvasOne.create_text(275, 600, text = 'Press Left or Right to play again!', justify = CENTER, font = ('Avenir Next', 20))

                    window.bind('<Left>',lambda event:leftButtonPressed(window, canvasOne))
                    window.bind('<Right>',lambda event:rightButtonPressed(window,canvasOne))
                    return
                else:
                    canvasOne.delete(firstOval)
                    score += 1
                    hasHit = True
                    colourOfCircle = colour


        time.sleep(0.1)

triangleOne = canvasOne.create_polygon(275,450,312.5,450 - (75**2-37.5**2)**(1/2),235.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[0], tags = 'yellow')
triangleTwo = canvasOne.create_polygon(275,450,350,450,312.5,450 - (75**2-37.5**2)**(1/2),fill=triangleFills1[1], tags = 'lightskyblue')
triangleThree = canvasOne.create_polygon(275,450,312.5,450 + (75**2-37.5**2)**(1/2),350,450,fill=triangleFills1[2], tags = 'red')
triangleFour = canvasOne.create_polygon(275,450,235.5,450 + (75**2-37.5**2)**(1/2),312.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[3], tags = 'green')
triangleFive = canvasOne.create_polygon(275,450,200,450,235.5,450 + (75**2-37.5**2)**(1/2),fill=triangleFills1[4], tags = 'purple')
triangleSix = canvasOne.create_polygon(275,450,235.5,450 - (75**2-37.5**2)**(1/2),200,450,fill=triangleFills1[5], tags = 'orange')

window.update()
window.bind('<Left>',lambda event:leftButtonPressed(window, canvasOne))
window.bind('<Right>',lambda event:rightButtonPressed(window,canvasOne))

getHighScore()
hexagonMenu()

window.update()

window.mainloop()
