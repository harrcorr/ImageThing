#                  COPYRIGHT, YOUR DAD. jk idgaf about copyright                 #
import PIL
import numpy
from ImageLib import *
a = numpy.zeros((255,255,3),'uint8')
def Math(RGB,x,y,time):
    #Math function here 
    r = x*abs(y)^2 #also x^2 + y^2 is interesting
    g = 0
    b = 0
    RGB = r,g,b
    return RGB
#Save saves what start cycle returns
#Math is the function called with data for pixel values and the position 
#path is save location
path = r"TO SAVE OUTPUTTED IMAGE HERE"
Save(StartCycle(a,Math),path)

