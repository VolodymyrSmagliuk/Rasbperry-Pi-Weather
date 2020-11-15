from tkinter import *

R = 0
G = 0
B = 0
A = 0


def SetNodeColor():
    #some code
    changeColor()
    return 0

def get_valueR(val):
    global R
    R = val
    SetNodeColor()

def get_valueG(val):
    global G
    G = val
    SetNodeColor()

def get_valueB(val):
    global B
    B = val
    SetNodeColor()  
    
def get_valueAlpha(val):
    global A
    A = val
    SetNodeColor()
    
def getColor(rgb):
    return "#%02x%02x%02x" % rgb  
    
root = Tk()
root.title("The simplest GUI")
root.geometry("500x500")

mainFrame = Frame(root)
mainFrame.grid()

#R###############################
frameR = Frame(root)
frameR.grid()

labelR = Label(frameR, text=u'R')
labelR.pack(side = 'left')

scaleR = Scale(frameR, from_=0, to=255, orient=HORIZONTAL, command=get_valueR)
scaleR.pack(side = 'right')
##########################

#G###############################
frameG = Frame(root)
frameG.grid()

labelG = Label(frameG, text=u'G')
labelG.pack(side = 'left')

scaleG = Scale(frameG, from_=0, to=255, orient=HORIZONTAL, command=get_valueG)
scaleG.pack(side = 'right')
##########################

#B###############################
frameB = Frame(root)
frameB.grid()

labelB = Label(frameB, text=u'B')
labelB.pack(side = 'left')

scaleB = Scale(frameB, from_=0, to=255, orient=HORIZONTAL, command=get_valueB)
scaleB.pack(side = 'right')
##########################

#ALPHA###############################
frameALPHA = Frame(root)
frameALPHA.grid()

labelALPHA = Label(frameALPHA, text=u'Alpha')
labelALPHA.pack(side = 'left')

scaleALPHA = Scale(frameALPHA, from_=0, resolution = 0.01, to=1, orient=HORIZONTAL, command=get_valueAlpha)
scaleALPHA.pack(side = 'right')
##########################

#ColorPrewiev###############################
framePrewiev = Frame(root, bg='red', width = 100, height = 100)
framePrewiev.configure(bg=getColor((R, G, B))) 
framePrewiev.grid()

def changeColor():
    global R
    global G
    global B
    global A
    hexcolour = getColor((round(float(R) * float(A)), round(float(G) * float(A)), round(float(B) * float(A))))
    framePrewiev.configure(bg=hexcolour)
 
##########################


root.mainloop()



