#import dependencies
import PIL
import numpy as np
from PIL import Image  
import random
#does wit it says
def Open(path):
    try:
        arr = Image.open(path)
        arr = np.asarray(arr)
    except:
        print("invalid path returning what i have")
        arr = path
    return arr
def Save(arr,path):
    #again it does wot it says
    img = Image.fromarray(arr)
    img.save(path)
#takes rgb into a variable and parses it into the math func
def getrgb(arr,x,y,time,func):
    r = 0
    g = 0
    b = 0
    RGB = r,g,b
    RGB = arr[x,y]
    try:
        arr[x,y] = func(RGB,x,y,time)
    except Exception as e:
        print("error please confirm math function accepts RGB x y and time")
        print(str(e))
def StartCycle(arr,MathFunc):
    sx,sy,rgbdimensions = arr.shape #rgb dimensions will always = 3 or 4 if u stick an alpha in there
    y = 0
    x = 0
    time = 0
    #cycles through every pixel in array and sticks it in get rgb to cleanly pull rgb values
    while(y < sy):
        while(x < sx):
                getrgb(arr,x,y,time,MathFunc)
                x = x + 1
                time = time + 1
        y = y + 1
        time = time + 1
        x = 0
    return arr
