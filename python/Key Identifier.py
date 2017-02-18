'''
This tells you how you can refer to the keyboard keys.
'''


try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def key(event):
    '''
    shows key or tk code for the key
    all things returned by event.keysym are strings
    '''
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:  # normal number and letter characters
        print( 'Normal Key %r' % event.char )  # You can also format this like print( 'Normal Key {0}'.format(event.char) )
    elif len(event.char) == 1:  # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:  # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )


root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
root.focus_force()
# root.withdraw()  # don't show the tk window
    # Don't make this not a comment:
    # You won't be able to click on the window to make it work or ex it out to stop.
root.mainloop()