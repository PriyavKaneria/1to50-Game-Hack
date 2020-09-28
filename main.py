# Thank you for checking out my project. Hope you like it. The comments might help you for understanding. 
# Read the readme.md file for successful run of this program.

# ALL IMPORTS

from pynput.mouse import Button, Controller
import time
import numpy as np
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Listener
from PIL import Image,ImageOps,ImageFilter
import imagetiling as tile
import os

# Mouse Control Variable
mouse = Controller()
    
def on_press(key):
    pass

# Function to recognise characters from image using tesseract installed in your PC using cmd.
def ocr(img):
    os.system(f'tesseract.exe {img} output.txt --psm 8')
    file = open(r'output.txt.txt','r')
    out=file.readline()
    file.close()
    return (out)

def joinimg(listofimg):
    imgs    = [ Image.open(i) for i in listofimg ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save that beautiful picture
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( 'all.png' )

def loop(h):
    global outp,ls,outls,X1,X2,Y1,Y2
    X1=720 #fixed do not change for a screen resolution of 1536 by 864.........IT IS THE DISTANCE OF LAPTOP'S LEFT EDGE TO THE FIRST BOX COLOUMN OF THE GAME GRID IN px
    X2=1180 #fixed do not change for a screen resolution of 1536 by 864.........IT IS THE DISTANCE OF LAPTOP'S LEFT EDGE TO THE LAST BOX COLOUMN OF THE GAME GRID IN px
    Y1=430 #JUST CHANGE THIS NUMBER IF REQUIRED.........IT IS THE DISTANCE OF LAPTOP'S TOP EDGE TO THE FIRST BOX ROW OF THE GAME GRID IN px
    Y2=Y1+460
    img = ImageGrab.grab(bbox=(X1,Y1,X2,Y2))  # X1,Y1,X2,Y2
    print('strted')
    img.save('myimg.png')
    img=Image.open('myimg.png').convert('L')                    #_
    img=ImageOps.invert(img)                                    # |
    img = img.point(lambda p: p > 100 and 255)                  # |
    img = img.filter(ImageFilter.GaussianBlur(radius=1))        # } This all is pre-processing of the image for accurate ocr output.
    img.save('grayscale.png')                                   # |
    tile.tileimage('grayscale.png',1)                           #_|
    ls=[]
    outp=''
    imglist=[]
    for k in range(1,26):
        imgmini = f'{k}.png'
        imglist.append(imgmini)
        imglist.append('buffer.png')
    joinimg(imglist)
    out=ocr('all.png')
    for i in out:
        if i.isdigit():
            outp+=i
    outls=outp.split('123')
    print(outls)
    os.remove('myimg.png')
    os.remove('grayscale.png')
    os.remove('all.png')
    print('done')
    return [outls,h]

def mousemain(ls):
    global poslist,Y1
    poslist=()
    h=ls[1]
    ls=ls[0]
    for i in range((25*h)+1,(25*h)+26):
        posx=ls.index(str(i))
        posy=posx//5
        posx%=5
        mouse.position=(577+35+(posx*70),Y1-35+(posy*70)) # Moving mouse to calculated coordinates
        poslist+=((posx,posy),)
        mouse.click(Button.left,1) # Mouse click

# Check which keys are pressed
def on_release(key):
    if key == key.ctrl_l:  # Change to whatever key you want for initiating the process.
        for h in range(2):
            mousemain(loop(h))
        for k in range(1,26):
            os.remove(f'{k}.png')
        return False
    elif key == key.esc:  # To terminate the program in between
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()