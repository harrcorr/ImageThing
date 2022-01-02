import PIL
import numpy
from lib.ImageLib import Save,StartCycle

imageX = 255
imageY = 255
output = r"./examples/(x+y)(y+x)_high_res_colors.png"
if(output == ""):
    print("Please specify output")
    exit()

data = numpy.zeros((1000,1000,3),'uint8')
def Math(RGB,x,y,time):
    r =  (x + y) * (y + x) #also x^2 + y^2 is interesting
    b =  (x - y) * (y - x)
    g =  (x - y) * (y + x)
    if(r % 2 != 0):
        g = r % 2
    else:
        b = r % 1
    
    RGB = r,g,b
    return RGB

#Save saves what start cycle returns
#Math is the name of the per pixel callback
#output is save location
Save(StartCycle(data,Math),output)

