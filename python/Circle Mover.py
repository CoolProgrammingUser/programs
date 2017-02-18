'''
You move a green smiley face around on the screen with the arrow keys, and you can make smaller circles by pressing the space bar.
'''

try:
    from Tkinter import *  # Python2
except ImportError:
    from tkinter import *  # Python3

from random import randint as ri

__author__ = "Robert Benson"
__date__ = "2015-2016"

root = Tk()
root.wm_title("Circle Mover")
cw = root.winfo_screenwidth()  # Canvas Width
ch = root.winfo_screenheight()  # Canvas Height
canvas = Canvas(root, width=cw, height=ch, bg="white")
canvas.grid()

def h(*numbers) :
    if numbers != None :
        digits = []
        for number in numbers :
            digits.append(hex(number)[2:])
        hexadecimal = "#"
        for number in digits :
            hexadecimal += number
        return hexadecimal

# This allows me to treat everything as if the height and width were always 255.
def rw(number) :  # resize width
    return int(number / cw * 255)
def rh(number) :  # resize height
    return int(number / ch * 255)
def uw(number) :  # undo width
    return int(cw / 255 * number)
def uh(number) :  # undo height
    return int(ch / 255 * number)

def makeText(x, y, words, fontSize, justify=CENTER, **extras) :
    '''
    creates text on the canvas
    default justification is center
    '''
    return canvas.create_text(uw(x), uh(y), extras, text=words, font=("",uh(fontSize)), justify=justify)

def makeCircle(x,y,r,**extras) :
    '''
    makes a circle centered on a certain coordinate value with a given radius and optional specifications
    '''
    return canvas.create_oval(uw(x)-uh(r), uh(y)-uh(r), uw(x)+uh(r), uh(y)+uh(r), extras)

def makeCircularArc(x,y,r,**extras) :
    return canvas.create_arc(uw(x)-uh(r), uh(y)-uh(r), uw(x)+uh(r), uh(y)+uh(r), extras)

def projectile() :
    projectiles.append(makeCircle(ri(0,255), ri(0,255), ri(2,8), fill=h(0,0,ri(0,15)), outline="#00f", activefill=h(ri(0,15),ri(0,15),ri(0,15)), activeoutline=h(ri(0,15),ri(0,15),ri(0,15))))

def keyHandler() :
    '''
    binds all used keys
    '''
    for key in ["Escape", "Right", "6", "Left", "4", "Down", "2", "Up", "8", "space", "r"]:
        root.bind("<KeyPress-{}>".format(key), isPressed)
        root.bind("<KeyRelease-{}>".format(key), released)
        pressed[key] = False

def isPressed(event):
    pressed[event.keysym] = True

def released(event):
    pressed[event.keysym] = False

def check() :
    '''
    calls a certain function when a certain key is pressed
    '''
    global text, circle, projectiles, pressed
    if pressed["Escape"] :
        root.destroy()
    if pressed["Right"] or pressed["6"] :
        for item in circle :
            canvas.move(item, uh(2), 0)
        if len(projectiles) > 0 :
            for item in projectiles :
                a = canvas.coords(item)[0]
                b = canvas.coords(item)[2]
                canvas.move(item, uh(30)/abs(a-b), 0)
    if pressed["Left"] or pressed["4"] :
        for item in circle :
            canvas.move(item, uh(-2), 0)
        if len(projectiles) > 0 :
            for item in projectiles :
                a = canvas.coords(item)[0]
                b = canvas.coords(item)[2]
                canvas.move(item, uh(-30)/abs(a-b), 0)
    if pressed["Down"] or pressed["2"] :
        for item in circle :
            canvas.move(item, 0, uh(2))
    if pressed["Up"] or pressed["8"] :
        for item in circle :
            canvas.move(item, 0, uh(-2))
    if pressed["space"] :
        projectile()
    if pressed["r"] :
        canvas.delete("all")
        text = [
            makeText(127.5, 20, 'Press "Escape" to exit.', 10),
            makeText(127.5, 235, 'Experiment with arrow keys, space bar, and "r".', 10)
            ]
        circle = [127.5, 127.5]
        circle = [
            makeCircle(circle[0], circle[1], 25, fill=h(0,15,0), activefill="#ff0", outline=""),
            makeCircle(circle[0]-7, circle[1]-8, 5, fill=h(0,0,0), activefill="#0f0"),
            makeCircle(circle[0]+7, circle[1]-8, 5, fill=h(0,0,0), activefill="#0f0"),
            makeCircularArc(circle[0], circle[1]-2, 20, fill=h(0,0,0), start=210, extent=120, width=5, style=ARC, activefill="#0f0")
            ]
        projectiles = []
    root.after(20, check)

text = [
    makeText(127.5, 20, 'Press "Escape" to exit.', 10),
    makeText(127.5, 235, 'Experiment with arrow keys, space bar, and "r".', 10)
    ]
circle = [127.5, 127.5]  # center of the circle
circle = [
    makeCircle(circle[0], circle[1], 25, fill=h(0,15,0), activefill="#ff0", outline=""),
    makeCircle(circle[0]-7, circle[1]-8, 5, fill=h(0,0,0), activefill="#0f0"),
    makeCircle(circle[0]+7, circle[1]-8, 5, fill=h(0,0,0), activefill="#0f0"),
    makeCircularArc(circle[0], circle[1]-2, 20, fill=h(0,0,0), start=210, extent=120, width=5, style=ARC, activefill="#0f0")
    ]
projectiles = []
pressed = {}

'''
RWidth=Root.winfo_screenwidth()
RHeight=Root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (RWidth, RHeight))
'''

root.focus_force()  # makes the window take focus
root.attributes("-fullscreen", True)  # makes the window fill up the screen
# root.wm_state("zoomed")
root.after(0, keyHandler)
root.after(0, check)
root.mainloop()