##################################################
# my standard set-up (not especially game-related)

try:
    from Tkinter import *  # Python2
except ImportError:
    from tkinter import *  # Python3

from random import randint as ri

root = Tk()
root.wm_title("Circle Mover 2")

cw = 200.0  # canvas width (has to be a float)
ch = 200.0  # canvas height (has to be a float)

# This allows me to treat everything as if the height and width were always 255.
def rw(number) :  # resize width
    return int(number / cw * 255)
def rh(number) :  # resize height
    return int(number / ch * 255)
def uw(number) :  # undo width
    return int(cw / 255 * number)
def uh(number) :  # undo height
    return int(ch / 255 * number)

canvas = Canvas(root, width=cw, height=ch, bg="white")
canvas.grid()

def h(*numbers) :
    '''
    turns the numbers into hexadecimal and concatenates them with a preceeding "#"
    '''
    if numbers != None :
        digits = []
        for number in numbers :
            digits.append(hex(number)[2:])
        hexadecimal = "#"
        for number in digits :
            hexadecimal += number
        return hexadecimal

def makeCircle(x,y,r,**extras) :
    '''
    makes a circle centered on a certain coordinate value with a given radius and optional specifications
    '''
    return canvas.create_oval(x-r, y-r, x+r, y+r, extras)

def makeCircularArc(x,y,r,**extras) :
    return canvas.create_arc(x-r, y-r, x+r, y+r, extras)

def c(obj) :  # center (of object)
    '''
    finds the center of an object
    returns center as an ordered pair in a non-resized format in a list
    '''
    x1,y1,x2,y2 = canvas.coords(obj)
    return [(x1+x2)/2, (y1+y2)/2]

collide = True
def ccollision(object1, radius1, object2, radius2) :  # circular collision
    '''
    determines if two circles have collided
    radii CAN'T be in an undone or resized format; they represent ratios not definate lengths
    '''
    global collide
    object1 = c(object1)
    object2 = c(object2)
    if rh(((object1[0]-object2[0])**2+(object1[1]-object2[1])**2)**.5) <= radius1+radius2 and collide :
        return True
    else :
        return False
# abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)/((y2-y1)**2+(x2-x1)**2)**.5

##################################################
##################################################


# The preferable way to do this would be [[center x-value, center y-value, radius, x-multiplier, y-multiplier], [circle, left eye, right eye, mouth]].
# I already made things differently, and it's too much work to change.
circles = []  # each item = [[circle, left eye, right eye, mouth], x multiplier, y multiplier]

def move() :
    for circle in circles :
        x1,y1,x2,y2 = canvas.coords(circle[0][0])
        if x1 < 0 :
            circle[1] *= -1
        if x2 > cw :
            circle[1] *= -1
        if y1 < 0 :
            circle[2] *= -1
        if y2 > ch :
            circle[2] *= -1
        '''                                         # This is my attempt to prevent it from crashing.
        while c(circle[0][0])[0] < uw(20) :
            for item in circle[0] :
                canvas.move(item, 1, 0)
        while c(circle[0][0])[0] > cw-uw(20) :
            for item in circle[0] :
                canvas.move(item, -1, 0)
        while c(circle[0][0])[1] < uh(20) :
            for item in circle[0] :
                canvas.move(item, 0, 1)
        while c(circle[0][0])[1] > ch-uw(20) :
            for item in circle[0] :
                canvas.move(item, 0, -1)
        '''
        for item in circles :  # starts determining if 2 faces have collided
            if circle != item :
                if ccollision(circle[0][0], 20, item[0][0], 20) :  # checks if colliding
                    # swaps the velocities of colliding faces
                    velocity = [circle[1], circle[2]]
                    circle[1] = item[1]
                    circle[2] = item[2]
                    item[1] = velocity[0]
                    item[2] = velocity[1]
        for item in circle[0] :  # actually moves the faces
            canvas.move(item, uh(10)*circle[1], uh(10)*circle[2])
        try :  # This stops the error saying it got an invalid color name but doesn't stop the crashing.
            canvas.itemconfig(circle[0][0], fill=h(int(rh(c(circle[0][0])[1])/16), int(rw(c(circle[0][0])[0])/16), 0))  # changes face color based on position
        except :
            return
    root.after(50, move)

def keyHandler(event) :
    
    # create or delete smiley faces
    if event.keysym == "Right" :
        
        circles.append([ri(uw(20),uw(255)-uw(20)), ri(uh(20),uh(255)-uh(20))])  # [center x-value, center y-value]
        circles[-1] = [[
        makeCircle(circles[-1][0], circles[-1][1], uh(20), fill=h(int(rh(circles[-1][1])/16), int(rw(circles[-1][0])/16), 0), outline=""),
        makeCircle(circles[-1][0]-uh(8), circles[-1][1]-uh(10), uh(5), fill="#000", outline=""),
        makeCircle(circles[-1][0]+uh(8), circles[-1][1]-uh(10), uh(5), fill="#000", outline=""),
        makeCircularArc(circles[-1][0], circles[-1][1], uh(12), start=210, extent=120, width=uh(5), style=ARC)],
        ri(-1, 1), ri(-1, 1)]
        
        while circles[-1][1] == 0 and circles[-1][2] == 0 :  # makes sure the faces aren't stationary
            circles[-1][1] = ri(-1, 1)
            circles[-1][2] = ri(-1, 1)
    
    if event.keysym == "Left" and len(circles) > 0 :
        for item in circles[-1][0] :
            canvas.delete(item)
        circles.pop()  # defaults to -1
    
    
    # turn collisions off or on
    global collide
    if event.keysym == "o" :
        if collide :
            collide = False
        else :
            collide = True
    
    
    # resize the canvas
    global cw
    global ch
    if event.keysym == "Up" :
        cw *= 1.05
        ch *= 1.05
        canvas.config(width=cw, height=ch)
        for face in circles :
            for feature in face[0] :
                "This is where I'd reconfigure each feature of the smiley faces."
    if event.keysym == "Down" :
        cw *= .95
        ch *= .95
        canvas.config(width=cw, height=ch)
        for face in circles :
            for feature in face[0] :
                "This is where I'd reconfigure each feature of the smiley faces."

'''
coords(item, *coords) [#]
Returns the coordinates for an item.

item
    Item specifier (tag or id).
*coords
    Optional list of coordinate pairs.
    If given, the coordinates will replace the current coordinates for all matching items.
Returns:
    If no coordinates are given, this method returns the coordinates for the matching item.
    If the item specifier matches more than one item, the coordinates for the first item found is returned.
'''

root.after(0, move)
root.bind_all("<Key>", keyHandler)
root.mainloop()