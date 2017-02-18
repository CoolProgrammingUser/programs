'''
This is a moderately simple recreation of a Mario game.
(I had big plans for this, but it was too time comsuming. Consequentially, there's a lot of things that aren't used.)
Local variables are generally preceeded by a "my" (not counting for loop variables).
Many of these things would be better done with classes, but I couldn't learn about them fast enough before I started this.
Consequentially, there are multiple standards scattered throughout the code.
I'd refine it now, but I don't have time; it'll be good practice for you anyway.
If you can overlook all the nonsense, there's actually a lot to learn here.
I don't know what the deal is with the errors in the traceback, but they don't affect the gameplay.
'''

try:  # tries this first
    from Tkinter import *  # Python2
except ImportError:  # does this if the exception matches
    from tkinter import *  # Python3
except :  # handles any remaining exceptions
    pass
finally :  # does this at the end no matter what
    pass

from random import choice as rc, randrange # as itself

__author__ = "Robert Benson"
__date__ = "2015-2016"

root = Tk()
root.wm_title("Super Duper Mario")

# have to be floats
cw = float(root.winfo_screenwidth())  # Canvas Width --- home computer=1363  school computer=1435
ch = float(root.winfo_screenheight())  # Canvas Height --- home computer=702  school computer=835

# This allows me to treat everything as if the height and width were always 255.
def rw(number) :  # resize width
    return int(number / cw * 255)
def rh(number) :  # resize height
    return int(number / ch * 255)
def uw(number) :  # undo width
    return int(cw / 255 * number)
def uh(number) :  # undo height
    return int(ch / 255 * number)

c = Canvas(root, width=cw, height=ch, bg="#45f")
c.grid()

def h(*numbers) :
    '''
    turns the numbers into hexadecimal and concatenates them with a preceeding "#"
    '''
    if numbers != () :
        digits = []
        lengths = 0
        hexadecimal = "#"
        for number in numbers :
            digits.append(hex(int(number))[2:])
        for number in digits :
            lengths += len(number)
        for number in digits :
            if lengths%len(numbers) != 0 and len(number) == 1 :
                hexadecimal += "0"+number
            else :
                hexadecimal += number
        return hexadecimal

'''
Tkinter is dumb and doesn't let you move lines.
def makeLine(x, y, direction, length, **extras) :
    if direction == "h" :
        c.create_line(x-length/2, y, x+length/2, y, extras)
    elif direction == "v" :
        c.create_line(x, y-length/2, x, y+length/2, extras)
'''

def makeCircle(x, y, r, fill="#000", **extras) :
    '''
    x = center x-coordinate
    y = center y-coordinate
    r = radius
    **extras = optional keyworded specifications
    default outline and fill is none
    '''
    if "outline" in extras :
        return c.create_oval(x-r, y-r, x+r, y+r, extras, fill=fill)
    else :
        return c.create_oval(x-r, y-r, x+r, y+r, extras, fill=fill, outline="")

def makeCircularArc(x, y, r, **extras) :
    '''
    x = center x-coordinate
    y = center y-coordinate
    r = radius
    **extras = optional keyworded specifications
    default outline and fill is none
    '''
    if "outline" in extras :
        return c.create_arc(x-r, y-r, x+r, y+r, extras)
    else :
        return c.create_arc(x-r, y-r, x+r, y+r, extras, outline="")

def makeOval(x, y, w, h, **extras) :
    '''
    x = center x-coordinate
    y = center y-coordinate
    w = width
    h = height
    **extras = optional keyworded specifications
    default outline and fill is none
    '''
    if "outline" in extras :
        return c.create_oval(x-w/2, y-h/2, x+w/2, y+h/2, extras)
    else :
        return c.create_oval(x-w/2, y-h/2, x+w/2, y+h/2, extras, outline="")

def makeOvalArc(x, y, w, h, **extras) :
    '''
    x = center x-coordinate
    y = center y-coordinate
    w = width
    h = height
    **extras = optional keyworded specifications
    default outline and fill is none
    '''
    if "outline" in extras :
        return c.create_arc(x-w/2, y-h/2, x+w/2, y+h/2, extras)
    else :
        return c.create_arc(x-w/2, y-h/2, x+w/2, y+h/2, extras, outline="")

def makeRectangle(x, y, w, h, **extras) :
    '''
    x = center x-coordinate
    y = center y-coordinate
    w = width
    h = height
    **extras = optional keyworded specifications
    default outline and fill is none
    '''
    if "outline" in extras :
        return c.create_rectangle(x-w/2, y-h/2, x+w/2, y+h/2, extras)
    else :
        return c.create_rectangle(x-w/2, y-h/2, x+w/2, y+h/2, extras, outline="")

def makePolygon(x, y, *points, **specifications) :
    '''
    x = x-coordinate center
    y = y-coordinate center
    points come in groups of 2: 1 x and 1 y coordinate
    all points are relative to center
    default outline and fill is none
    '''
    coordinates = []
    for point in range(0, len(points), 2) :
        coordinates += [points[point]+x, points[point+1]+y]
    if "outline" in specifications :
        return c.create_polygon(coordinates, specifications)
    else :
        return c.create_polygon(coordinates, specifications, outline="")

def makeRPolygon(x, y, *points, **specifications) :
    '''
    makes half of a polygon and reflects it over the y-axis
    x = x-coordinate center
    y = y-coordinate center
    points come in groups of 2: 1 x and 1 y coordinate
    all points are relative to center
    default outline and fill is none
    '''
    coordinates = []
    for point in range(0, len(points), 2) :
        coordinates += [points[point]+x, points[point+1]+y]
    reflectedCoordinates = []
    for point in range(1, len(points), 2) :
        coordinates += [-points[-point-1]+x, points[-point]+y]
    coordinates = coordinates + reflectedCoordinates
    if "outline" in specifications :
        return c.create_polygon(coordinates, specifications)
    else :
        return c.create_polygon(coordinates, specifications, outline="")

def makeBrick(x, y) :
    '''
    makes brick blocks uh(15) by uh(15) big
    '''
    return [
    makeRectangle(x, y, uh(15), uh(15), fill="#a62"),
    makeRectangle(x, y-uh(2.5), uh(15), uh(1.5), fill="#000"),
    makeRectangle(x, y+uh(2.5), uh(15), uh(1.5), fill="#000"),
    makeRectangle(x, y-uh(5), uh(1.5), uh(5), fill="#000"),
    makeRectangle(x, y+uh(5), uh(1.5), uh(5), fill="#000"),
    makeRectangle(x+uw(1.75), y, uh(1.5), uh(5), fill="#000"),
    makeRectangle(x-uw(1.75), y, uh(1.5), uh(5), fill="#000"),
    makeRectangle(x+uw(3.5), y-uh(5), uh(1.5), uh(5), fill="#000"),
    makeRectangle(x-uw(3.5), y-uh(5), uh(1.5), uh(5), fill="#000"),
    makeRectangle(x+uw(3.5), y+uh(5), uh(1.5), uh(5), fill="#000"),
    makeRectangle(x-uw(3.5), y+uh(5), uh(1.5), uh(5), fill="#000")]

def makeText(x, y, words, fontSize, **extras) :
    '''
    creates text on the canvas
    default justification is center
    '''
    if "justify" in extras :
        return c.create_text(x, y, extras, text=words, font=("",fontSize))
    else :
        return c.create_text(x, y, extras, text=words, font=("",fontSize), justify=CENTER)

def makeSpeechBubble(x1, y1, x2, y2, words, fontSize=uh(6), justification=CENTER, trigger=False, *time) :
    '''
    x1 = the x-coordinate of the point of the speech bubble (the part nearest the speaker)
    y1 = the y-coordinate of the point of the speech bubble (the part nearest the speaker)
    x2 = the x-coordinate of the center of the oval of the speech bubble (the part containing the text)
    y2 = the y-coordinate of the center of the oval of the speech bubble (the part containing the text)
    words = the text contained within the speech bubble
    trigger = whether this function should also return the value of the time
    *time = the time, in milliseconds, before the speech bubble is deleted (defaults to a function of the length of the text)
    '''
    if time == () :
        time = len(words)**.5*500
    global speech
    myText = words.split("\n")
    while "\n" in myText[-1] :
        myText.append(myText[-1].split("\n")[0])
        myText.append(myText[-2].split("\n")[1])
    if len(myText) < 2 :
        myText.append(myText[0])
    speech = [[[(x1+x2)/2, (y1+y2)/2]], [
        c.create_polygon(x2-uw(len(myText[0])/4), y2, x1, y1, x2+uw(len(myText[0])/4), y2, fill="#fff", outline="#000", width=uh(.5)),
        makeOval(x2, y2, uh(len(myText[0])*5+10), uh(len(myText)*10+10), fill="#fff", outline="#000", width=uh(.5)),
        makeText(x2, y2, words, fontSize, justify=justification)]]
    root.after(int(time), triggeredDelete, speech)
    if trigger :
        return int(time)

"""
This isn't used.
def ccollision(object1, radius1, object2, radius2) :  # circular collision
    '''
    determines if two circles have collided
    radii CAN'T be in an undone or resized format; they represent ratios not definate lengths
    '''
    if rh(((object1[0]-object2[0])**2+(object1[1]-object2[1])**2)**.5) <= radius1+radius2 :
        return True
    else :
        return False
# abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)/((y2-y1)**2+(x2-x1)**2)**.5
"""

def rr(start, stop, *step) :
    '''
    serves to include the stop number in the randrange function
    '''
    return randrange(start, stop+1, *step)  # the * has to be before step presumably because it can only be one argument (maybe)

def checkAll(list, *conditions, **stuff) : # I don't know why I have to have **stuff instead of thing="".
    '''
    This checks if any items in a list meet a certain condition.
    *conditions = a variable number of conditions typed as strings
        If a condition isn't typed as a string, the condition will have been changed to True or False by the time it gets here.
        Only one item in the list has to meet the conditions to return True.
        All conditions have to be met for a given item in order to fully meet the conditions.
    **stuff = set "thing" equal to something in order to be able to reference that thing in the conditions
        The value of "thing" CANNOT be a string in most scenarios.
            examples:
                thing = 10
                (20 > thing) == True
                thing = "10"
                (20 > thing) == False
                thing = "b"
                ("a" > thing) == False
                thing = "b"
                ("c" > thing) == True
        You could make "thing" a list of things which you could access by index.
    '''
    if "thing" in stuff :
        thing = stuff["thing"]
    myTrueFalse = False
    for item in list :
        myExecute = "if 1==1"
        for specification in conditions :
            myExecute += " and "+str(item)+specification
        myExecute += " :\n\tmyTrueFalse = True"
        exec myExecute
    return myTrueFalse


# lists have the contents of each item explained
# tester = makeText(cw/2, ch/2, "Tester", uh(10))
refresh = 20  # screen refreshes every 20 milliseconds
speech = []
pressed = {}
repeating = {}
inputEnabled = True
screen = ""
prompt = []
score = [0, []]
highScore = [0, []]
size = 1
background = []
ground = []
speechBubble = []
terrain = []  # [[[x-coordinate center, y-coordinate center], other], [foreground]]
# mario needs collisions with bricks fixed
mario = []    # [[[x-coordinate center, y-coordinate center], [[past x, past y], [x-velocity, y-velocity]], powerup], [parts]]
enemies = []  # [[[x-coordinate center, y-coordinate center], [[past x, past y], [x-velocity, y-velocity]], attack], [parts]]
boss = []     # [[[x-coordinate center, y-coordinate center], [[past x, past y], [x-velocity, y-velocity]], attack], [parts]]


def start() :
    global screen, prompt
    keyHandler()
    screen = "title"
    makeText(uw(127.5), uh(50), "Super Duper\nMario", uh(30), fill="#fff")
    prompt = [
        makeRectangle(uw(127.5), uh(180), uh(80), uh(60), fill="#fa0"),
        makeText(uw(127.5), uh(180), "Press\nEnter", uh(15), fill="#a0f")]
    root.after(500, flashPrompt)

def flashPrompt() :
    '''
    flashes "Press Enter"
    '''
    c.itemconfig(prompt[0], fill=("#ff0" if c.itemcget(prompt[0], "fill")=="#fa0" else "#fa0"))
    c.itemconfig(prompt[1], fill=("#f00" if c.itemcget(prompt[1], "fill")=="#a0f" else "#a0f"))
    repeating["flash"] = root.after(500, flashPrompt)

def codeRequest() :
    '''
    provides the opportunity to use a save code
    '''
    global screen
    screen = "load game"
    makeText(uw(127.5), uh(127.5), "Do you have a save code?\n(y or n)", uh(20), fill="#fff")

def beginning() :
    global inputEnabled, screen, background, ground, speechBubble
    inputEnabled = False
    screen = "beginning"
    createBackground(uh(0), uh(220))
    while background[-1][0][0][0] < cw :
        createBackground(background[-1][0][0][0]+uh(60), uh(220))
    ground = [
        makeRectangle(cw/2+uh(1), ch/2+uh(117.5), cw, uh(22), fill="#c84"),
        makeRectangle(cw/2+uh(1), ch/2+uh(105.5), cw, uh(4), fill="#0f0")]
    createTerrain(cw/2+uh(10), ch/2)
    createMario(cw/2-uh(150.5), ch/2+uh(103.5)-uh(22.3)*size)
    makeSpeechBubble(cw/2-uw(70), ch/2+uh(65), cw/2-uw(50), ch/2+uh(40), "I need to save\nPrincess Peach!")
    root.after(2800, initialize)

def initialize() :
    global speechBubble
    for item in speechBubble :
        c.delete(item)
    automate(mario, uh(4), uh(0), "mario[0][0][0] < cw/2", "reposition()")

def reposition() :
    global inputEnabled, screen, score, highScore
    screen = "outside"
    if terrain[0][0][0][0] > 0 :
        moveRight()
        root.after(refresh, reposition)
    else :
        score[1] = makeText(uw(10), uh(8), "Score: 0", uh(5), fill="#fff")
        highScore[1] = makeText(uw(241), uh(8), "High Score: {}".format(highScore[0]), uh(5), fill="#fff")
        inputEnabled = True
        fall(1)
        velocity()
        AI()
        play()

def play() :
    '''
    the main game loop
    '''
    global size
    # create the terrain
    if terrain[-1][0][0][0] <= cw/2 :
        createTerrain(cw*1.5, ch/2)
    # elif terrain[0][0][0][0] >= -cw/2 :
        # createTerrain(-cw*1.5, ch/2)
        if rr(1, 6) == 1 : # randomly determines whether a power up should be created
            PowerUp()
        if rr(1, 6) == 1 : # randomly determines where an enemy should be placed
            createEnemy(cw*1.5, ch/2-uh(15), "Goomba")
        elif rr(1, 6) == 1 :
            createEnemy(cw*1.5, ch/2-uh(15), "Goomba")
            createEnemy(rr(round(cw/2*2), round(cw*2)), ch/2+uh(97), "Goomba")
        else :
            createEnemy(rr(round(cw/2*2), round(cw*2)), ch/2+uh(97), "Goomba")
    
    # delete the terrain
    if terrain[0][0][0][0] < cw*-1.5 :
        for item in terrain[0][1] :
            c.delete(item)
        terrain.pop(0)
    # elif terrain[-1][0][0][0] > cw*1.5 :
        # for item in terrain[0][1] :
            # c.delete(item)
        # terrain.pop(0)
    
    if background[0][0][0][0] < cw*-1.5 :
        triggeredDelete(background[0], background)
    '''
    for powerUp in PowerUp.instances :
        for part in mario[0] :
            # if part in c.find_overlapping(powerUp.coords.x-uh(10), powerUp.coords.y-uh(10), powerUp.coords.x+uh(10), powerUp.coords.y+uh(10)) :
            ## if mario[0][0][1] < ch/2 :
                if size < 1.5 :
                    size +=.5
                for item in mario[1] :
                    c.delete(item)
                createMario(mario[0][0][0], mario[0][0][1])
                powerUp.delete()
    '''
    repeating["play"] = root.after(refresh, play)

def updateScore(change) :
    global score, highScore
    score[0] += change
    c.delete(score[1])
    score[1] = makeText(uw(10), uh(8), "Score: {}".format(score[0]), uh(5), fill="#fff")
    if score[0] > highScore[0] :
        highScore[0] = score[0]
        c.delete(highScore[1])
        highScore[1] = makeText(uw(241), uh(8), "High Score: {}".format(highScore[0]), uh(5), fill="#fff")

def fall(height) :
    '''
    causes Mario to fall back down
    '''
    # This is supposed to make falling look more natural.
    # (initial slow falling speeding up as the falling continues)
    # This was made before I came up with a way to collide with the bricks.
    '''
    global mario
    if mario[0][0][1] < ch/2+uh(103.5)-uh(22.3)*size :
        height *= 1.1
        if mario[0][0][1] + uh(1)*height < ch/2+uh(103.5)-uh(22.3)*size :
            move(mario, uh(0), uh(3)*height)
        else :
            for attribute in mario[1] :
                c.delete(attribute)
            mario = []
            createMario(cw/2, ch/2+uh(103.5)-uh(22.3)*size)
    else :
        falling = 1
    '''
    # This is my quick fix.
    if mario[0][1][1][1] >= 0 and mario[0][0][1] < ch/2+uh(103.5)-uh(22.3)*size and not checkAll(terrain, "[0][1]==1", "[0][0][1]-uh(0) > mario[0][0][1]+uh(22.3)*size", "[0][0][1]-uh(8) < mario[0][0][1]+uh(22.3)*size", "[0][0][0]-uh(46.5) < mario[0][0][0]+uh(13.5)*size", "[0][0][0]+uh(46.5) > mario[0][0][0]-uh(13.5)*size") :
        move(mario, uh(0), uh(8))
    repeating["fall"] = root.after(refresh, fall, height)

def velocity() :
    '''
    keeps track of the distance moved in the last move
    changes the ordered pair in Mario's velocity
    This is only used for jumping and may be able to be eliminated
    (although it might also be able to be used to change the direction Mario faces).
    '''
    #if mario[0][0][0] != mario[0][1][0][0] :
    mario[0][1][1][0] = mario[0][0][0]-mario[0][1][0][0]
    mario[0][1][0][0] = mario[0][0][0]
    #if mario[0][0][1] != mario[0][1][0][1] :
    mario[0][1][1][1] = mario[0][0][1]-mario[0][1][0][1]
    mario[0][1][0][1] = mario[0][0][1]
    repeating["velocity"] = root.after(refresh, velocity)

def keyHandler() :
    '''
    binds all used keys
    '''
    for key in ["Escape", "Return", "Right", "d", "D", "6", "Left", "a", "A", "4", "Down", "s", "S", "2", "Up", "w", "W", "8", "space", "5", "n", "N", "y", "Y", "r", "R", "e", "E"]:
        root.bind("<KeyPress-{}>".format(key), isPressed)
        root.bind("<KeyRelease-{}>".format(key), isReleased)
        pressed[key] = False
    check()

def isPressed(event):
    pressed[event.keysym] = True

def isReleased(event):
    pressed[event.keysym] = False

def check() :
    '''
    calls a certain function when a certain key is pressed
    '''
    if inputEnabled :
        if pressed["Escape"] :
            root.destroy()
        if pressed["Return"] :
            enter()
        if pressed["Right"] or pressed["d"] or pressed["D"] or pressed["6"] :
            moveRight()
        if pressed["Left"] or pressed["a"] or pressed["A"] or pressed["4"] :
            moveLeft()
        if pressed["Down"] or pressed["s"] or pressed["S"] or pressed["2"] :
            moveDown()
        if pressed["Up"] or pressed["w"] or pressed["W"] or pressed["8"] :
            moveUp()
        if pressed["space"] :
            jump(1) # I don't know why this has to be called a minimum of 2 times.
            jump(1) # When it wasn't called twice, Mario wouldn't jump when you hit the space bar too fast.
        if pressed["5"] :
            usePowerup()
        if pressed["n"] or pressed["N"] :
            no()
        if pressed["y"] or pressed["Y"] :
            yes()
        if pressed["r"] or pressed["R"] :
            restart()
        if pressed["e"] or pressed["E"] :
            easterEgg()
    root.after(refresh, check)

def enter() :
    if screen == "title" :
        c.delete("all")
        beginning()

def no() :
    if screen == "load game" :
        c.delete("all")
        beginning()

def yes() :
    pass

def restart() :
    '''
    restarts the game
    Some peculiar things happen (including with jumping, but I fixed it so it's not noticeable) after restarting, but I think I fixed it enough that gameplay won't be affected.
    ...I might have fixed all the problems...or maybe not
    '''
    global speech, repeating, screen, prompt, score, size, background, ground, speechBubble, terrain, mario, enemies, boss
    for loop in repeating :
        root.after_cancel(repeating[loop])
    c.delete("all")
    for instance in PowerUp.instances :
        del instance
    speech = []
    repeating = {}
    screen = ""
    score = [0, []]
    size = 1
    background = []
    ground = []
    speechBubble = []
    terrain = []
    mario = []
    enemies = []
    boss = []
    beginning()

def easterEgg() :
    for structure in background :
        if 0 <= structure[0][0][0] <= cw :
            c.itemconfig(structure[1], fill=h(rw(cw-structure[0][0][0]), 0, rw(structure[0][0][0])))
        elif structure[0][0][0] < 0 :
            c.itemconfig(structure[1], fill="#f00")
        elif structure[0][0][0] > cw :
            c.itemconfig(structure[1], fill="#00f")

def moveRight() :
    '''
    moves Mario right
    (really moves everthing else left)
    '''
    for structure in background :
        move(structure, uh(-2), uh(0))
    for structure in terrain :
        move(structure, uh(-4), uh(0))
    for enemy in enemies :
        move(enemy, uh(-4), uh(0))
    for powerUp in PowerUp.instances :
        powerUp.move(-4, 0)
    if speech[1] != [] :
        move(speech, uh(-4), uh(0))

def moveLeft() :
    '''
    moves Mario left
    (really moves everything else right)
    '''
    for structure in background :
        move(structure, uh(2), uh(0))
    for structure in terrain :
        move(structure, uh(4), uh(0))
    for enemy in enemies :
        move(enemy, uh(4), uh(0))
    for powerUp in PowerUp.instances :
        powerUp.move(4, 0)
    if speech[1] != [] :
        move(speech, uh(4), uh(0))

def jump(height) :  # work here too
    '''
    allows Mario to jump
    Mario doesn't like to jump when the space bar is pressed too quickly (but don't hold it).
    '''
    if (screen == "outside" or screen == "boss" or screen == "pipe" or screen == "underwater" or screen == "castle") and mario[0][1][1] != 0 :
        # This is supposed to make the jumping look more natural.
        # (initial fast movement slowing at the top)
        # This was made before I came up with a way to collide with the bricks.
        '''
        if mario[0][1][1][1] == 0 and not height > 10 :
            height *= 1.1
            move(mario, uh(0), uh(-25)/height)
            if 1 < height < 10 :
                root.after(refresh, jump, height)
        '''
        # This is my quick fix.
        # if  Mario's not moving   or   height is between 1 and 10   and   Mario isn't going to bump his head on terrain :
        if (mario[0][1][1][1] == 0 or 1 < height < 10) and not checkAll(terrain, "[0][1]==1", "[0][0][1]+uh(7) < mario[0][0][1]-uh(20.25)*size", "[0][0][1]+uh(14) > mario[0][0][1]-uh(20.25)*size", "[0][0][0]-uh(46.5) < mario[0][0][0]+uh(13.5)*size", "[0][0][0]+uh(46.5) > mario[0][0][0]-uh(13.5)*size") :
            move(mario, uh(0), uh(-8))
            root.after(refresh, jump, height+1)
        else :
            mario[0][1][1][1] == 0

def moveDown() :
    '''
    This is supposed to be used to go down pipes and stuff,
    but it's so much more fun to use it this way when there's no pipes.
    '''
    global refresh
    if not (pressed["Down"] or pressed["s"] or pressed["S"] or pressed["2"]) and refresh > 1 :
        refresh -= 1

def moveUp() :
    '''
    This is supposed to be used to go up ladders and stuff,
    but it's so much more fun to use it this way when there's no ladders.
    '''
    global refresh
    if not (pressed["Up"] or pressed["w"] or pressed["W"] or pressed["8"]) :
        refresh += 1

def usePowerup() :
    pass

def automate(entity, xDistance, yDistance, condition, *function) :
    '''
    entity = thing you want to automate
    xDistance = the x-distance to be moved
    yDistance = the y-distance to be moved
    condition = how you determine when the function should stop
                an integer input makes it loop that many times
                a conditional in a string makes it stop when the condition is false
    *function = optionally calls a function when it's finished (including itself)
    '''
    try :
        if condition > 0 :
            move(entity, xDistance, yDistance)
            root.after(refresh, automate, entity, xDistance, yDistance, condition-1, *function)
        elif function != () :
            exec function[0]  # arguments from a function are inherently a tuple, so an item needs to be selected
    except :
        if eval(condition) :
            move(entity, xDistance, yDistance)
            root.after(refresh, automate, entity, xDistance, yDistance, condition, *function)
        elif function != () :
            exec function[0]

def move(entity, xDistance, yDistance) :
    '''
    moves entities
    '''
    if size > 0 or entity is mario :
        entity[0][0][0] += xDistance
        entity[0][0][1] += yDistance
        for item in entity[1] :
            c.move(item, xDistance, yDistance)
        if background[-1][0][0][0] < cw :
            createBackground(background[-1][0][0][0]+uh(60), uh(220))

def AI() :
    '''
    provides artificial intelligence
    '''
    for enemy in enemies :
        if enemy[0][3] == 1 :
            if enemy[0][1] == "Goomba" :
                if enemy[0][2] == 1 :
                    # This makes an enemy move around back and forth.
                    if enemy[0][4] > 6 :
                        enemy[0][4] += rr(-5, 0)
                    elif enemy[0][4] < -6 :
                        enemy[0][4] += rr(0, 5)
                    else :
                        enemy[0][4] += rr(-5, 5)
                    if enemy[0][4] < -4 :
                        move(enemy, uh(-2), uh(0))
                    elif enemy[0][4] > 4 :
                        move(enemy, uh(2), uh(0))
                    if enemy[0][0][1] < ch/2 : # if the enemy is on terrain bricks :
                        if not checkAll(terrain, "[0][0][0]-uh(42) < thing", "[0][0][0]+uh(42) > thing", thing=enemy[0][0][0]) : # if the enemy isn't comfortably on the platform (about to fall off) :
                            if enemy[0][4] < -4 :
                                move(enemy, uh(2), uh(0))
                            elif enemy[0][4] > 4 :
                                move(enemy, uh(-2), uh(0))
                    
                    if mario[0][0][0]+uh(13.5)*size > enemy[0][0][0]-uh(9) and mario[0][0][0]-uh(13.5)*size < enemy[0][0][0]+uh(9) and mario[0][0][1]+uh(22.3)*size > enemy[0][0][1]-uh(30) and mario[0][0][1]-uh(20.25)*size < enemy[0][0][1] : # if Mario hits the top of the enemy :
                        triggeredDelete(enemy)
                        createEnemy(enemy[0][0][0], enemy[0][0][1]+uh(4.625), "Goomba", squish=.5)
                        enemies.pop(enemies.index(enemy))
                    elif mario[0][0][0]+uh(13.5)*size > enemy[0][0][0]-uh(14) and mario[0][0][0]-uh(13.5)*size < enemy[0][0][0]+uh(14) and mario[0][0][1]+uh(22.3)*size > enemy[0][0][1]-uh(21) and mario[0][0][1]-uh(15)*size < enemy[0][0][1]+uh(9.25) : # if Mario hits anywhere else on the enemy :
                        harmMario()
                else :
                    updateScore(10)
                    root.after(makeSpeechBubble(enemy[0][0][0]+uh(12), enemy[0][0][1]-uh(5), enemy[0][0][0]+uh(35), enemy[0][0][1]-uh(18), "*Squish*", trigger=True), triggeredDelete, enemy)
                    enemy[0][3] = 0
            elif enemy[0][1] == "Koopa Troopa" : # It would probably be better if you programmed the AI into the class of the enemy (if you use a class)
                pass
            elif enemy[0][1] == "Piranha Plant" : # It would probably be better if you programmed the AI into the class of the enemy (if you use a class)
                pass
    repeating["AI"] = root.after(refresh, AI)

def triggeredDelete(entity, *list) : ####################
    '''
    Use the "after" method to call this after a certain amount of time.
    Use the optional "list" argument to say that the entity comes from a list where it needs to get removed.
    '''
    for item in entity[1] :
        c.delete(item)
    if list != () :
        list[0].pop(list[0].index(entity))

def timedAppear(entity, *extras) : # might not need this since there's the function "automate"
    '''
    Use the "after" method to call this after a certain amount of time.
    '''
    pass

class Coords :
    '''
    gives coordinates to objects
    '''
    def __init__(self, x=rr(round(cw), round(cw*2)), y=ch/2+uh(97)) :
        self.x = x
        self.y = y

class PowerUp :
    
    '''
    creates various power ups
    '''
    
    instances = []
    
    def __init__(self, ID=rc(["grow"]), x=None, y=None) :
        self.instances.append(self)
        self.ID = ID
        self.coords = (Coords(x=x, y=y) if x!=None and y!=None else Coords())
        if self.ID == "grow" :
            self.shapes = [
                # top
                makeOval(self.coords.x, self.coords.y-uh(2), uh(18), uh(14), fill="#f00"),
                makeCircle(self.coords.x, self.coords.y-uh(4.5), uh(3.5), fill="#fff"),
                makeOval(self.coords.x-uh(8), self.coords.y-uh(2), uh(2), uh(5), fill="#fff"),
                makeOval(self.coords.x+uh(8), self.coords.y-uh(2), uh(2), uh(5), fill="#fff"),
                # stem
                makeOval(self.coords.x, self.coords.y+uh(4), uh(10), uh(7), fill="#fc8"),
                # eyes
                makeOval(self.coords.x-uh(1.5), self.coords.y+uh(3), uh(1), uh(3), fill="#000"),
                makeOval(self.coords.x+uh(1.5), self.coords.y+uh(3), uh(1), uh(3), fill="#000")
                ]
        elif self.ID == "1Up" :
            self.shapes = [
                # top
                makeOval(self.coords.x, self.coords.y-uh(2), uh(18), uh(14), fill="#0d0"),
                makeCircle(self.coords.x, self.coords.y-uh(4.5), uh(3.5), fill="#fff"),
                makeOval(self.coords.x-uh(8), self.coords.y-uh(2), uh(2), uh(5), fill="#fff"),
                makeOval(self.coords.x+uh(8), self.coords.y-uh(2), uh(2), uh(5), fill="#fff"),
                # stem
                makeOval(self.coords.x, self.coords.y+uh(4), uh(10), uh(7), fill="#fc8"),
                # eyes
                makeOval(self.coords.x-uh(1.5), self.coords.y+uh(3), uh(1), uh(3), fill="#000"),
                makeOval(self.coords.x+uh(1.5), self.coords.y+uh(3), uh(1), uh(3), fill="#000")
            ]
        self.touch()
    
    def touch(self, width=18, height=18) :
        '''
        determines if the power up is touching Mario
        width = hit box width
        height = hit box height
        '''
        if mario[0][0][0]+uh(13.5)*size > self.coords.x-uh(width/2) and mario[0][0][0]-uh(13.5)*size < self.coords.x+uh(width/2) and mario[0][0][1]+uh(22.3)*size > self.coords.y-uh(height/2) and mario[0][0][1]-uh(20.25)*size < self.coords.y+uh(height/2) :
            self.use()
            self.delete()
        else :
            repeating[self] = root.after(refresh, self.touch, width, height)
    
    def use(self) :
        global size
        if self.ID == "grow" :
            if size < 1.5 :
                triggeredDelete(mario)
                size += .5
                createMario(mario[0][0][0], mario[0][0][1])
            else :
                updateScore(10)
        elif self.ID == "1Up" :
            pass
    
    def move(self, xDistance, yDistance) :
        '''
        moves the power up
        '''
        if size > 0 :
            for shape in self.shapes :
                c.move(shape, uh(xDistance), uh(yDistance))
            self.coords.x += uh(xDistance)
            self.coords.y += uh(yDistance)
    
    def delete(self) :
        '''
        deletes the power up
        '''
        root.after_cancel(repeating[self])
        repeating.pop(self)
        for shape in self.shapes :
            c.delete(shape)
        self.instances.pop(self.instances.index(self))

class Coin :
    '''
    creates a coin
    increases the score by 1
    '''
    instances = []
    pass

class Yoshi :
    '''
    creates Yoshi
    '''
    pass

class Enemy :
    '''
    creates an enemy
    '''
    pass

class Boss :
    '''
    creates a boss
    '''
    def __init__(self, ID=rc(["Giant Goomba"]), x=None, y=None) :
        self.ID = ID
        self.life = 3
        self.coords = (Coords(x=x, y=y) if x!=None and y!=None else Coords())
        if self.ID == "Bowser" :
            pass
        elif self.ID == "Giant Goomba" :  # I didn't really want this boss, but animation takes forever, and this allows me to reuse the Goomba animation.
            myMultiplier = 4  # This was just to help me get a better size for the Giant Goomba: It doesn't change, so you don't really need it.
            self.shapes = [
                # stem/body
                makeOval(self.coords.x, self.coords.y+uh(2)*squish*myMultiplier, uh(8)*myMultiplier, uh(7)*squish*myMultiplier, fill="#ec8"),
                # top
                makeRPolygon(self.coords.x, self.coords.y-uh(8)*squish*myMultiplier, uh(8)*myMultiplier, uh(-4)*squish*myMultiplier, uh(11)*myMultiplier, uh(2)*squish*myMultiplier, uh(8)*myMultiplier, uh(8)*squish*myMultiplier, fill="#840"),
                makeOval(self.coords.x, self.coords.y-uh(10)*squish*myMultiplier, uh(16)*myMultiplier, uh(17)*squish*myMultiplier, fill="#840"),
                makeOval(self.coords.x-uh(8)*myMultiplier, self.coords.y-uh(4)*squish*myMultiplier, uh(7)*myMultiplier, uh(7)*squish*myMultiplier, fill="#840"),
                makeOval(self.coords.x+uh(8)*myMultiplier, self.coords.y-uh(4)*squish*myMultiplier, uh(7)*myMultiplier, uh(7)*squish*myMultiplier, fill="#840"),
                # eyes
                makeOvalArc(self.coords.x+uh(4)*myMultiplier, self.coords.y-uh(10)*squish*myMultiplier, uh(5)*myMultiplier, uh(7)*squish*myMultiplier, fill="#fff", start=190, extent=250, style="chord"),
                makeOval(self.coords.x+uh(4)*myMultiplier, self.coords.y-uh(10)*squish*myMultiplier, uh(2.5)*myMultiplier, uh(4)*squish*myMultiplier, fill="#000"),
                makeOvalArc(self.coords.x-uh(4)*myMultiplier, self.coords.y-uh(10)*squish*myMultiplier, uh(5)*myMultiplier, uh(7)*squish*myMultiplier, fill="#fff", start=100, extent=250, style="chord"),
                makeOval(self.coords.x-uh(4)*myMultiplier, self.coords.y-uh(10)*squish*myMultiplier, uh(2.5)*myMultiplier, uh(4)*squish*myMultiplier, fill="#000"),
                # mouth
                makeRectangle(self.coords.x, self.coords.y-uh(3)*squish*myMultiplier, uh(10)*myMultiplier, uh(1)*squish*myMultiplier, fill="#000"),
                # feet
                makeOval(self.coords.x+uh(5)*myMultiplier, self.coords.y+uh(5.25)*squish*myMultiplier, uh(6)*myMultiplier, uh(4)*squish*myMultiplier, fill="#421"),
                makeOval(self.coords.x-uh(5)*myMultiplier, self.coords.y+uh(5.25)*squish*myMultiplier, uh(6)*myMultiplier, uh(4)*squish*myMultiplier, fill="#421")
            ]
        self.talk(1)
        self.AI()
    
    def AI(self, width=40, height=40) :
        '''
        width = hit box width
        height = hit box height
        '''
        if mario[0][0][0]+uh(13.5)*size > self.coords.x-uh(width/2) and mario[0][0][0]-uh(13.5)*size < self.coords.x+uh(width/2) and mario[0][0][1]+uh(22.3)*size > self.coords.y-uh(height/2) and mario[0][0][1]-uh(20.25)*size < self.coords.y+uh(height/2) :
            self.talk(3)
            harmMario()
        elif False :
            self.hurt()
        else :
            if rr(1, 200) == 1 :
                self.talk(2)
            repeating[self] = root.after(refresh, self.AI, width, height)
    
    def move(self, xDistance, yDistance) :
        '''
        moves the boss
        '''
        if size > 0 :
            for shape in self.shapes :
                c.move(shape, uh(xDistance), uh(yDistance))
            self.coords.x += uh(xDistance)
            self.coords.y += uh(yDistance)
    
    def talk(self, speechNumber, trigger=False) :
        '''
        allows the boss to talk
        '''
        if speechNumber == 1 :
            pass
        elif speechNumber == 2 :
            pass
        elif speechNumber == 3 :
            pass
        elif speechNumber == 4 :
            pass
        elif speechNumber == 5 :
            pass
    
    def hurt(self) :
        '''
        handles what happens when the boss is hurt
        '''
        self.life -= 1
        if self.life > 0 :
            self.talk(4)
        else :
            self.talk(5)
            root.after(self.talk(5, trigger=True), self.delete) 
    
    def delete(self) :
        '''
        deletes the boss
        '''
        root.after_cancel(repeating[self])
        repeating.pop(self)
        for shape in self.shapes :
            c.delete(shape)

def harmMario() :
    global size, screen
    size -= .5
    triggeredDelete(mario)
    if size > 0 :
        createMario(mario[0][0][0], mario[0][0][1])
        for _ in range(1,40) :
            moveLeft()
    else :
        size = .5
        createMario(mario[0][0][0], mario[0][0][1])
        size = 0
        makeSpeechBubble(mario[0][0][0]+uh(10), mario[0][0][1]-uh(5), mario[0][0][0]+uh(30), mario[0][0][1]-uh(25), "Oh, no!")
        root.after_cancel(repeating["fall"])
        screen = "game over"
        root.after(1000, automate, mario, uh(0), uh(-2.5), 10, "automate(mario, uh(0), uh(2.5), 'mario[0][0][1]-uh(11) < ch', 'makeText(cw/2, ch/2, \"Game Over\", uh(20), fill=\"#fff\")')")

def createBackground(x, y) :
    '''
    creates the background
    '''
    background.append([[[x, y], 0]])
    myB = background[-1][0][0] # This is here in case I decide I want to add more stuff to the background.
    background[-1].append([
        # hill
        makeCircle(x, y, uh(40), fill="#0c0")])
    c.tag_lower(background[-1][1][0])

def createTerrain(x, y) :
    '''
    creates the terrain
    '''
    if screen == "beginning" :
        terrain.append([[[x, y], 0]])
        myT = terrain[-1][0][0]
        terrain[-1].append([
            # house
            # body
            makeRectangle(myT[0]-uw(78), myT[1]+uh(74), uh(120), uh(60), fill="#fff"),
            # door
            makeRectangle(myT[0]-uw(78), myT[1]+uh(79), uh(30), uh(50), fill="#b73"),
            makeCircle(myT[0]-uh(143), myT[1]+uh(79), uh(2), fill="#ff0"),
            # windows
            makeRectangle(myT[0]-uw(96), myT[1]+uh(71), uh(25), uh(25), fill="#6ff", outline="#444", width=uh(1)),
            makeRectangle(myT[0]-uw(60), myT[1]+uh(71), uh(25), uh(25), fill="#6ff", outline="#444", width=uh(1)),
            # roof
            makePolygon(myT[0]-uw(78), myT[1]+uh(22), uh(-62), uh(22), uh(0), uh(-22), uh(62), uh(22), fill="#fff", outline="#444", width=uh(1.5))])
    
    elif screen == "outside" :
        terrain.append([[[x, y], 1], []])
        myT = terrain[-1][0][0]
        for place in [-39, -26, -13, 0, 13, 26, 39] :
            terrain[-1][1] += makeBrick(myT[0]+uh(place), myT[1])
    
    elif screen == "boss" :
        pass
    elif screen == "pipe" :
        pass
    elif screen == "underwater" :
        pass
    elif screen == "castle" :
        pass

def createMario(x, y) :
    '''
    creates Mario
    
    width = uh(27)*size
    left = uh(-13.5)*size from the center
    right = uh(13.5)*size from the center
    height = uh(42.55)*size
    top = uh(-20.25)*size from the center
    bottom = uh(22.3)*size from the center
    '''
    global mario
    mario = [[[x, y], [[cw/2, y], [0, 0]], 0]]
    myM = mario[0][0]
    mario.append([
        # head
        makeOval(myM[0], myM[1]-uh(13.5)*size, uh(12)*size, uh(10.5)*size, fill="#fd9"),
        # nose
        makeOval(myM[0]+uh(6)*size, myM[1]-uh(13.75)*size, uh(4)*size, uh(2.5)*size, fill="#fd9"),
        # hair
        makeCircularArc(myM[0]-uh(1)*size, myM[1]-uh(13.5)*size, uh(6)*size, start=90, extent=100, fill="#951"),
        # ear
        makeOval(myM[0]-uh(3)*size, myM[1]-uh(14)*size, uh(2)*size, uh(4)*size, fill="#fd9", width=uh(.5), outline="#555"),
        # eye
        makeOval(myM[0]+uh(4)*size, myM[1]-uh(15.5)*size, uh(1)*size, uh(2)*size, fill="#000"),
        # mouth
        makeRectangle(myM[0]+uh(5)*size, myM[1]-uh(11.5)*size, uh(3)*size, uh(.5)*size, fill="#000"),
        # moustache
        makeOval(myM[0]+uh(5)*size, myM[1]-uh(12)*size, uh(4)*size, uh(1)*size, fill="#951"),
        # hat
        makeOvalArc(myM[0]-uh(1)*size, myM[1]-uh(15)*size, uh(12)*size, uh(10.5)*size, start=20, extent=140, style="chord", fill="#f00"),
        makeRectangle(myM[0]+uh(6)*size, myM[1]-uh(17)*size, uh(4)*size, uh(1)*size, fill="#f00"),
        # hands
        makeCircle(myM[0]-uh(11.5)*size, myM[1]+uh(6)*size, uh(2)*size, fill="#fd9"),
        makeCircle(myM[0]+uh(11.5)*size, myM[1]+uh(6)*size, uh(2)*size, fill="#fd9"),
        # shirt
        makeRPolygon(myM[0], myM[1]-uh(5)*size, uh(8)*size, uh(-4.5)*size, uh(12)*size, uh(2)*size, uh(13)*size, uh(9)*size, uh(10)*size, uh(9)*size, uh(9)*size, uh(5)*size, uh(7)*size, uh(3)*size, uh(7)*size, uh(5)*size, fill="#f00"),
        # overalls
        makeRPolygon(myM[0], myM[1], uh(3)*size, uh(-4)*size, uh(3)*size, uh(-9.25)*size, uh(6)*size, uh(-9.25)*size, uh(6)*size, uh(0)*size, uh(7)*size, uh(0)*size, uh(7)*size, uh(7)*size, uh(9)*size, uh(12)*size, uh(9)*size, uh(18)*size, uh(5)*size, uh(18)*size, uh(4)*size, uh(13)*size, uh(0)*size, uh(8)*size, fill="#00f"),
        makeCircle(myM[0]-uh(3)*size, myM[1], uh(1)*size, fill="#ff0"),
        makeCircle(myM[0]+uh(3)*size, myM[1], uh(1)*size, fill="#ff0"),
        # shoes
        makeRectangle(myM[0]+uh(7.5)*size, myM[1]+uh(20)*size, uh(6.5)*size, uh(4.6)*size, fill="#840"),
        makeCircle(myM[0]+uh(10.75)*size, myM[1]+uh(20)*size, uh(2.2)*size, fill="#840"),
        makeRectangle(myM[0]-uh(7.5)*size, myM[1]+uh(20)*size, uh(6.5)*size, uh(4.6)*size, fill="#840"),
        makeCircle(myM[0]-uh(10.75)*size, myM[1]+uh(20)*size, uh(2.2)*size, fill="#840")])

def createEnemy(x, y, variety, squish=1) :
    enemies.append([[[x, y], variety, squish, 1, 0]])
    myE = enemies[-1][0][0]
    if variety == "Goomba" :
        '''
        width = uh(23)
        height = uh(36.25)*squish
        top = uh(-27)*squish from center
        bottom = uh(9.25)*squish from center
        '''
        enemies[-1].append([
            # stem/body
            makeOval(myE[0], myE[1]+uh(2)*squish, uh(8), uh(7)*squish, fill="#ec8"),
            # top
            makeRPolygon(myE[0], myE[1]-uh(8)*squish, uh(8), uh(-4)*squish, uh(11), uh(2)*squish, uh(8), uh(8)*squish, fill="#840"),
            makeOval(myE[0], myE[1]-uh(10)*squish, uh(16), uh(17)*squish, fill="#840"),
            makeOval(myE[0]-uh(8), myE[1]-uh(4)*squish, uh(7), uh(7)*squish, fill="#840"),
            makeOval(myE[0]+uh(8), myE[1]-uh(4)*squish, uh(7), uh(7)*squish, fill="#840"),
            # eyes
            makeOvalArc(myE[0]+uh(4), myE[1]-uh(10)*squish, uh(5), uh(7)*squish, fill="#fff", start=190, extent=250, style="chord"),
            makeOval(myE[0]+uh(4), myE[1]-uh(10)*squish, uh(2.5), uh(4)*squish, fill="#000"),
            makeOvalArc(myE[0]-uh(4), myE[1]-uh(10)*squish, uh(5), uh(7)*squish, fill="#fff", start=100, extent=250, style="chord"),
            makeOval(myE[0]-uh(4), myE[1]-uh(10)*squish, uh(2.5), uh(4)*squish, fill="#000"),
            # mouth
            makeRectangle(myE[0], myE[1]-uh(3)*squish, uh(10), uh(1)*squish, fill="#000"),
            # feet
            makeOval(myE[0]+uh(5), myE[1]+uh(5.25)*squish, uh(6), uh(4)*squish, fill="#421"),
            makeOval(myE[0]-uh(5), myE[1]+uh(5.25)*squish, uh(6), uh(4)*squish, fill="#421")])
    elif variety == "Koopa Troopa" : # You may want to make an enemy class instead of filling this in.
        '''
        
        '''
        pass
    elif variety == "Piranha Plant" : # You may want to make an enemy class instead of filling this in.
        '''
        
        '''
        pass


root.focus_force()
root.attributes("-fullscreen", True)
root.after(0, start)
# root.bind_all("<Key>", keyHandler)
# root.bind("<space>", lambda event, height=0 : jump(height))
root.mainloop()